# game-saves

Repository of my retro game saves. Readme includes various tools for interacting with game saves and games. Also included is firmware for devices and programs used with saves.

# Git Repos

* [drehren/ra_mp64_srm_convert](https://github.com/drehren/ra_mp64_srm_convert) - RetroArch N64 Save Converter
* [heuripedes/pj64tosrm](https://github.com/heuripedes/pj64tosrm) - Another SRM converter. See `/executables/`. Just drag + drop files to convert onto the exe.
* [feyris-tan/gdidrop](https://github.com/feyris-tan/gdidrop) - Convert dreamcast BIN/CUE to GDI

# JELOS

[JustEnoughLinuxOS/distribution](https://github.com/JustEnoughLinuxOS/distribution) - The GitHub repo

# Hardware

* [JoeyN64](https://bennvenn.myshopify.com/products/joeyn64-cart-flasher) - N64 game pak and controller pak reader/writer
* [JoeyJR](https://bennvenn.myshopify.com/products/usb-gb-c-cart-dumper-the-joey-jr) - GB/GBC/GBA cart reader/writer

# Programs

* chdman - Converts between GDI/CUE and CHD

# Pokemon

* [projectpokemon/Gen3-WCTool](https://github.com/projectpokemon/Gen3-WCTool) - Gen 3 Wondercard Editor

# Command Line

Diff binary files like this:
```
xxd <file1> > 1.hex
xxd <file2> > 2.hex
git diff --no-index 1.hex 2.hex
```

# N64 Information

* [Save Methods](http://micro-64.com/database/gamesave.shtml)
* [CIC List](http://micro-64.com/database/gamecic.shtml)

# R4i Save Dongle

Drivers seem to be not needed on Windows 11.
Used the firmware upload tool to upload v1.3 firmware.
Writing a save failed twice, succeeded on 3rd try.

Files
* `drivers/r4i/drivers.rar` - Drivers, not needed?
* `firmware/r4i/SaveDongle_v13.bin` - The actual firmware
* `programs/r4i/SaveDongle_Firmware_Uploader.rar` - Contains the program to upload the firmware
* `programs/r4i/R4i SaveDongle V1.5.rar` - Contains the program to read/write save files
* `programs/r4i/3DSaveToolv0.2b-cred.rar` - Tool to encrypt/decrypt 3DS saves

Links
* [Main Page](http://www.r4i-sdhc.com/SaveDongle.asp)
* [Firmware Downloads](http://www.r4i-sdhc.com/Upgrade.asp)