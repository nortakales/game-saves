# game-saves

Repository of my retro game saves. Readme includes various tools for interacting with game saves and games. Also included is firmware for devices and programs used with saves.

# Git Repos

* [drehren/ra_mp64_srm_convert](https://github.com/drehren/ra_mp64_srm_convert) - RetroArch N64 Save Converter
* [heuripedes/pj64tosrm](https://github.com/heuripedes/pj64tosrm) - Another SRM converter. See `/executables/`. Just drag + drop files to convert onto the exe.
* [bryc/mempak](https://github.com/bryc/mempak) - Online controller memory pak editor

# JELOS

[JustEnoughLinuxOS/distribution](https://github.com/JustEnoughLinuxOS/distribution) - The GitHub repo

# Hardware

* [JoeyN64](https://bennvenn.myshopify.com/products/joeyn64-cart-flasher) - N64 game pak and controller pak reader/writer
* [JoeyJR](https://bennvenn.myshopify.com/products/usb-gb-c-cart-dumper-the-joey-jr) - GB/GBC/GBA cart reader/writer

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