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

# Patches

Use `/programs/Lunar IPS.exe` to apply `.ips` patches to ROMs

| Hack                                                                       | File                                             | ROM SHA1                                 |
| -------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| [Super Mario Land DX](https://www.romhacking.net/hacks/4477/)              | `smldx.ips`                                      | 3A4DDB39B234A67FFB361EE7ABC3D23E0A8B1C89 |
| [Super Mario Land 2 DX](https://www.romhacking.net/hacks/3784/)            | `SML2DXv181.ips`                                 | BBA408539ECBF8D322324956D859BC86E2A9977B |
| [Dr Mario DX](https://www.romhacking.net/hacks/5281/)                      | `dr_mario_dx.ips`                                | D31D67D0682515C7C85DEAA1752B02231150E5BF |
| [Kirby's Dream Land DX](https://www.romhacking.net/hacks/5635/)            | `dreamLandDX.ips`                                | 90979BAA1D0E24B41B5C304C5DDAF77450692D5A |
| [Kirby's Pinball Land DX](https://www.romhacking.net/hacks/6079/)          | `Kirby's Pinball Land DX v1.1.ips`               | 06EFDB138FF56CD9522DECE44ADADD3FAE169C76 |
| [Metroid II EJRTQ Colorization](https://www.romhacking.net/hacks/4388/)    | `Metroid_II_EJRTQ_Colorization_v1.3.zip`         | worked on my ROM                         |
| [Wario Land Super Mario Land 3 DX](https://www.romhacking.net/hacks/6683/) | `Wario Land - Super Mario Land 3 DX (World).ips` | AE65800302438E37A99E623A71D1C954D73C843E |
| [Mother 3 Fan Translation](https://www.romhacking.net/translations/1333/)  | `MOTHER3_EarthBound2_English_v1.3.zip`           | 4F0F493E12C2A8C61B2D809AF03F7ABF87A85776 |
| [Donkey Kong Land DX](https://www.romhacking.net/hacks/6076/)              | `DKL_v1.01.ips`                                  | 4E6D8F085CA197479D59912C1D58E4F3B40C28AC |
| [Donkey Kong Land 2 DX](https://www.romhacking.net/hacks/6866/)            | `DKL2 V1.2.ips`                                  | 89CC4F01653A6105EE5C00E10FC65AA1437FD320 |

