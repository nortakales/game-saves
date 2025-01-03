#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple utility to translate among the SRAM/EEPROM/Flash dump formats for
Nintendo 64 cartridges as supported by various dumpers, emulators, and flash
cartridges.
--snip--
A simple Python reimplementation of saturnu's ED64-Saveswap utility as posted
at https://github.com/sanni/cartreader/tree/master/extras/saveswap
The purpose of this tool is to achieve the following additional goals:
1. Be scriptable
2. Also run on non-Windows platforms
3. Don't trigger false positives for malware on VirusTotal.com
4. Be a very well-documented example for anyone who might want to switch
   from AutoIt to Python for this sort of tool.
I have chosen the name "N64-Saveswap" in recognition that the EverDrive 64
is not the only piece of hardware which may require the use of this tool
and to avoid confusion with saturnu's original utility.
While I did not engage in clean-room reverse-engineering, I believe this to be
its own work in the eyes of the law for the following combination of reasons:
1. Not only is the code in an entirely different language and relying heavily
   on constructs which AutoIt's scripting language has no equivalent for,
   the similarities which do exist are so fundamental to the task being
   performed that they CANNOT be eliminated.
   (eg. Yes, I swap bytes and pad files, but even those basic operations are
    done differently, owing to flaws and ugliness in AutoIt's language which
    I was able to avoid in Python.)
2. My efforts to replicate the program's UI have been done entirely by working
   from the screenshots in this thread:
   http://krikzz.com/forum/index.php?topic=1396.0
Copyright 2017 Stephan Sokolow
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

__author__ = "Stephan Sokolow"
__license__ = "MIT"
__appname__ = "N64-Saveswap"
__version__ = "0.1"

# A list of valid dump sizes, used for safety checks and padding
VALID_SIZES = [512, 2048, 32768, 131072]

import logging, os, shutil, sys, textwrap
log = logging.getLogger(__name__)

if sys.version_info.major > 2:  # pragma: nocover
    def reload(_):  # pylint: disable=redefined-builtin
        """Silence a spurious 'Undefined variable' error in Landscape.io"""
        pass

# A little safety guard against programmer error
assert all(x % 4 == 0 for x in VALID_SIZES), "VALID_SIZES contains bad value"
VALID_SIZES.sort()

class FileTooBig(Exception):
    """Exception raised for files bigger than the last entry in VALID_SIZES"""

class FileIncomplete(Exception):
    """Exception raised for files not a multiple of the swap increment."""

def rejoin_bytes(sequence):  # type: (...) -> bytes
    """Create a bytestring from whatever you get by iterating on one.
    This is a workaround for the following situation:
        1. In Python 2.7, iterating on a bytestring will give you a sequence of
           characters, which you rejoin with ``b''.join(sequence)`` and calling
           ``bytes([65 , 66, 67])`` gives you a string containing
           ``[65, 66, 67]``.
        2. In Python 3.x, iterating on a bytestring will give you a sequence of
           integers, which you rejoin with ``bytes(sequence)`` and
           ``b''.join(sequence)`` will raise an error because it doesn't know
           how to join integers.
    ...just be thankful I didn't get fed up enough to use
    .decode('latin1') and .encode('latin1') to side-step it by pretending that
    the Unicode codepoints corresponding to the latin-1 encoding are raw byte
    values.
    (Not a good idea, if you can avoid it, because it wastes memory supporting
     values you'll never use, wastes CPU time converting both ways, and, if you
     pick an encoding that can't represent all 256 possible byte values or
     accidentally introduce Unicode values that can't be mapped back, you'll
     set yourself up for unpleasant surprises.)
    """
    if sys.version_info.major < 3:
        # Python 2.7
        return b''.join(sequence)  # pragma: nocover
    else:
        # Python 3.x and beyond
        return bytes(sequence)     # pragma: nocover

def calculate_padding(path):  # type: (str) -> int
    """Calculate the size that a dump file should be padded to.
    :Parameters:
      path : `str`
        The path to the file to be rewritten.
    :rtype: `int`
    :returns: The target file size after padding
    :raises OSError: ``path`` does not exist.
    :raises FileTooBig: The file is already bigger than the largest valid size.
    """
    # Get the file size in bytes or raise OSError
    file_size = os.path.getsize(path)

    # Walking from smallest to largest (see definition of VALID_SIZES),
    # return the first value from VALID_SIZES that matches or exceeds
    # the file's current size
    for size in VALID_SIZES:
        if size >= file_size:
            return size

    # If we got this far, file_size is bigger than the biggest size in the list
    raise FileTooBig("File already exceeds largest valid size."
            "({} > {})".format(file_size, VALID_SIZES[-1]))

def assert_stride(data, stride_len):
    """Helper to deduplicate check that data length is a multiple of an int"""
    file_len = len(data)
    if not file_len % stride_len == 0:
        raise FileIncomplete("File length is not divisible by {}: {}"
                             "".format(stride_len, file_len))

def byteswap(path, swap_bytes=True, swap_words=True, pad_to=0):
    # type: (str, bool, bool, int) -> None
    """Perform requested swapping operations on the given file.
    A backup file will be generated by appending ``.bak`` to the path.
    :Parameters:
      path : `str`
        The path to the file to be rewritten.
      swap_bytes : `bool`
        If ``True``, treat the file as a sequence of 16-bit words and swap
        their endianness.
      swap_words : `bool`
        If ``True`` treat the file as a sequence of 32-bit words made of 16-bit
        components and swap those. May be combined with ``swap_bytes`` for a
        traditional "reverse the endianness of 32-bit words made of bytes"
        operation.
      pad_to : `int`
        If specified, append null bytes before writing to ensure the file is
        at least this length.
    :raises TypeError: The value of ``path`` is not a string.
    :raises IOError: Failure when attempting to read/write a file.
    :raises FileIncomplete:
        The length of the file isn't a multiple of the requested swapping
        increment.
    """
    # Given how small these are, let's just load the entire thing into memory,
    # manipulate it there, and then write the whole thing out again.
    #
    # It's less error-prone and it's (comparatively) slow to keep switching
    # into the OS kernel for a lot of little read() calls.
    with open(path, 'rb') as fobj_in:
        data = fobj_in.read()

    # OK, this is a little fancy, so I'll explain the parts in detail:
    #
    #   [0::4] means "take every fourth character starting with the first.
    #   [1::4] means "take every fourth character starting with the second.
    #     "123412341234" becomes "111" and "222" and so on.
    #
    #   zip() turns a list of rows into a list of columns
    #     [["4","4","4"], ["3","3","3"], ["2","2","2"], ["1","1","1"]]
    #       becomes
    #     [["4","3","2","1"], ["4","3","2","1"], ["4","3","2","1"]]
    #
    #   rejoin_bytes() turns a list of bytes into a bytestring.
    #
    #   b''.join() turns a list of bytestrings into a single bytestring,
    #   using "nothing" as the separator. ('' and "" are interchangeable)
    #     ["4", "3", "2", "1"] -> "4321"
    #
    #   Things of the form ``output = [something for x in data]`` are
    #   "list comprehensions" and what you see is shorthand for:
    #     output2 = []
    #     for x in output:
    #         output2.append(rejoin_bytes(x))
    #     output = b''.join(output2)
    #     del output2
    #
    # TODO: Are these files ALWAYS supposed to be multiples of 4 bytes when
    #       dumped? If so, I should enforce that unconditionally to catch
    #       corruption as broadly as possible.
    file_len = len(data)
    if swap_bytes:
        assert_stride(data, 2)
        data = zip(data[1::2], data[0::2])  # type: ignore
        data = b''.join([rejoin_bytes(x) for x in data])

    if swap_words:
        assert_stride(data, 4)
        data = zip(data[2::4], data[3::4],  # type: ignore
                   data[0::4], data[1::4])
        data = b''.join([rejoin_bytes(x) for x in data])

    # Now, apply padding if requested
    #
    # In Python, multiplying a string by an int repeats the string.
    #   'Foo' * 3 -> 'FooFooFoo'
    if pad_to > file_len:
        data = data + (b'\x00' * (pad_to - file_len))

    # Now, overwrite the old data with the new data
    #
    # The file will automatically be wiped clean when calling open() with
    # 'w' in the mode and this, while not infallible, is hard to screw up
    # because we only open the file after all the tricky bits are done.
    #
    with open(path, 'wb') as fobj_out:
        fobj_out.write(data)

def process_path(path, swap_bytes=True, swap_words=True, pad_to=None,
                 make_backup=True):
    """Do all necessary swapping and padding for a single file.
    This is separated out from `main` because it's good convention to
    keep your "handle one file" code in a function of its own so
    main() is all about processing the command-line input.
    See `byteswap` for additional argument documentation and exceptions raised.
    :Parameters:
      make_backup : `bool`
        If `True`, generate a backup file by appending `.bak` to the path.
        This will happen after detecting oversize files but before performing
        any actual work.
    :raises TypeError: The value of ``path`` is not a string.
    :raises IOError: Failure when attempting to read/write a file.
    :raises OSError: ``path`` does not exist (with ``pad_to=None``)
    """
    if pad_to is None:  # "None" means "Nothing specified. Guess."
        pad_to = calculate_padding(path)
    elif not pad_to:    # Anything else False-y (eg. 0) means "No padding."
        pad_to = 0

    if make_backup:
        bak_path = path + '.bak'

        # Don't get fancy. Just let a well-tested routine make our backup
        # (copy2 also preserves metadata like modification date)
        shutil.copy2(path, bak_path)

    byteswap(path, swap_bytes, swap_words, pad_to)

def main():  # type: () -> None
    """The main entry point, compatible with setuptools entry points."""
    # If we're running on Python 2, take responsibility for preventing
    # output from causing UnicodeEncodeErrors. (Done here so it should only
    # happen when not being imported by some other program.)
    if sys.version_info.major < 3:  # pragma: nocover
        # pylint: disable=no-member
        reload(sys)                      # type: ignore
        sys.setdefaultencoding('utf-8')  # type: ignore

    # Define a command-line argument parser which handles things like --help
    # and enforcing requirements for what arguments must be provided
    from argparse import ArgumentParser, RawDescriptionHelpFormatter
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
        description=__doc__.replace('\r\n', '\n').split('\n--snip--\n')[0],
        epilog=textwrap.dedent("""
            The swap modes behave as follows:
                    both: 12 34 -> 43 21
              bytes-only: 12 34 -> 21 43
              words-only: 12 34 -> 34 12
            The valid padding sizes for N64 save dumps are as follows:
              ===== EEPROM =====
                  512 (  4kbit)
                 2048 ( 16kbit)
              ====== SRAM ======
                32768 (256kbit)
               131072 (  1Mbit)
              ===== Flash ======
               131072 (  1Mbit)
            For scripting purposes, the exit code will indicate the most
            serious error encountered, with the following meanings:
               0 = Success
              10 = Could not read file / Could not write backup
              20 = File is too large to be an N64 save dump
              30 = File size is not a multiple of the requested swap increment
            """))

    parser.add_argument('--version', action='version',
        version="%%(prog)s v%s" % __version__)
    parser.add_argument('-v', '--verbose', action="count",
        default=2, help="Increase the verbosity. Use twice for extra effect.")
    parser.add_argument('-q', '--quiet', action="count",
        default=0, help="Decrease the verbosity. Use twice for extra effect.")

    parser.add_argument('--swap-mode', action="store", default='both',
        choices=('both', 'bytes-only', 'words-only'),
        help="Set the type of byte-swapping to be performed.")
    parser.add_argument('--force-padding', action="store", dest="pad_to",
        metavar="NEW_SIZE", default=None, type=int,
        help="Override autodetected padding size. This also disables the "
             " associated safety checks, allowing this tool to be used on "
             " other types of files. Specify 0 to disable padding entirely.")
    parser.add_argument('--no-backup', action="store_false", dest="backup",
        default=True,
        help="Disable creation of an automatic backup. This is intended to "
            "be used by scripts which want more control over whether and "
            "where backups are created.")
    parser.add_argument('path', nargs='+',
        help="One or more Nintendo 64 save memory dumps to byte-swap")

    # Parse the command-line
    args = parser.parse_args()

    # Set up clean logging to stderr which listens to -v and -q
    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    args.verbose = min(args.verbose - args.quiet, len(log_levels) - 1)
    args.verbose = max(args.verbose, 0)
    logging.basicConfig(level=log_levels[args.verbose],       # type: ignore
                        format='%(levelname)s: %(message)s')

    # Adapt the external interface to the internal one and process each file
    retcode = 0
    for path in args.path:
        log.info("Processing %s...", path)
        try:
            process_path(path=path,
                swap_bytes=args.swap_mode in ('both', 'bytes-only'),
                swap_words=args.swap_mode in ('both', 'words-only'),
                pad_to=args.pad_to,
                make_backup=args.backup)

        # Return the most serious error code we encountered
        except (IOError, OSError) as err:
            retcode = max(retcode, 10)
            log.error("Error while trying to read file: %s\n\t%s", path, err)
        except FileTooBig as err:
            retcode = max(retcode, 20)
            log.error("File is too big to be an N64 save dump: %s", path)
        except FileIncomplete as err:
            retcode = max(retcode, 30)
            log.error("File is incompatible with requested swap: %s", path)

    if retcode != 0:
        sys.exit(retcode)

# If we're being run directly rather than `import`-ed, run the code in `main()`
if __name__ == '__main__':
    main()  # pragma: nocover

# vim: set sw=4 sts=4 expandtab :