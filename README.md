# game-saves

Repository of my retro game saves. Readme includes various tools for interacting with game saves and games. Also included is firmware for devices and programs used with saves.

# Save/File Converters/Managers

* [drehren/ra_mp64_srm_convert](https://github.com/drehren/ra_mp64_srm_convert) - RetroArch N64 Save Converter. Worked for Snowboard Kids 2 (so far) but created SRA and EEP files when only EEP was needed.
* [heuripedes/pj64tosrm](https://github.com/heuripedes/pj64tosrm) - Another SRM converter. See `/executables/`. Just drag + drop files to convert onto the exe. Tested minimally.
* [feyris-tan/gdidrop](https://github.com/feyris-tan/gdidrop) - Convert Dreamcast BIN/CUE to GDI. WORKS.
* [bryc/mempak](https://github.com/bryc/mempak) - Online N64 memory pak manager
* [savefileconverter.com](https://savefileconverter.com/)
* [save-editor.com](https://www.save-editor.com/)
* [hjojojo8359/DeSmuMESaveConverter](https://github.com/jojojo8359/DeSmuMESaveConverter)
* [j-tai/dsv2sav](https://github.com/j-tai/dsv2sav)

# JELOS

[JustEnoughLinuxOS/distribution](https://github.com/JustEnoughLinuxOS/distribution) - The GitHub repo

# Hardware

* [JoeyN64](https://bennvenn.myshopify.com/products/joeyn64-cart-flasher) - N64 game pak and controller pak reader/writer
* [JoeyJR](https://bennvenn.myshopify.com/products/usb-gb-c-cart-dumper-the-joey-jr) - GB/GBC/GBA cart reader/writer
* Retrotink 4k
  * Firmware: https://retrotink-llc.github.io/firmware/
  * Docs: https://consolemods.org/wiki/AV:RetroTINK-4K
* Orange FM: https://orangegb.com/orangefm/manual_v13

## GBC Screen

Model: [Q5 IPS LCD Retro Pixel 2.0 laminated with OSD - Funny Playing](https://handheldlegend.com/products/game-boy-color-q5-retro-pixel-ips-lcd-kit-with-laminated-lens-funnyplaying)

Operating OSD:
* Tap and hold the touch sensor for 3 seconds to open OSD menu.
* Quick tap to make adjustments in the current menu option.
* To move to the next menu option, tap and hold the touch sensor for 2 seconds. 
* To exit the OSD menu, hold the touch sensor for 3 seconds or the menu will time out on its own.

Functions:
* BRT = Brightness options
* DSP = Pixel Modes
* FRM = Frame Blending Mode - flicker reduction
* LGC = GBC logo color options
* R/G/B = Customize GBC logo color options
* N = Move the display image left and right respectively

Pixel Modes:
* Built-in 5 display effects.
* 2? Full pixel copy display (display the highest brightness, gorgeous and concise)
* 3? Classic GBC display (perfectly restore the original display effect)
* 4? Classic RGB display (perfectly restore the original display effect, and the pixel gap looks smaller, the brightness will be slightly darker)
* 5? RGB display (closest to the original display, but the brightness is very low)
* 1? Grid line display (close to the display effect of DMG)

# Programs

* chdman - Converts between GDI/CUE and CHD
* NKit - downsize Gamecube isos

# Scripts

* saveswap - worked for N64 SRAM (.sra .srm) saves from Joey to work on the Everdrive (and vice versa), does a word AND byte swap by default which is what works for the Everdrive
  * Note: save files in this repo may be in either format depending on where they were played or taken from and have not been consolidated to a single format

# Pokemon

* [projectpokemon/Gen3-WCTool](https://github.com/projectpokemon/Gen3-WCTool) - Gen 3 Wondercard Editor

# Command Line

* Diff binary files like this: `hexdiff.sh <file1> <file2>`
* `checksums.sh` will compare checksums of ALL save files, and tell you if a file is empty

# N64

* [Save Methods](http://micro-64.com/database/gamesave.shtml)
* [CIC List](http://micro-64.com/database/gamecic.shtml)
* Gamebox 64 HD
  * [GameboxSystems/64HD-Installation-Guide](https://github.com/GameboxSystems/64HD-Installation-Guide)
    * L + R + C-down + Dpad-down = enter OSD mode
  * [GameboxSystems/Firmware-Update-Install-Scripts](https://github.com/GameboxSystems/Firmware-Update-Install-Scripts)
  * [GameboxSystems/Gamebox-Product-Firmware-Updates](https://github.com/GameboxSystems/Gamebox-Product-Firmware-Updates)

# 3DS

## Homebrew

* [Checkpoint](https://github.com/BernardoGiordano/Checkpoint)
* [Twilight Menu](https://github.com/DS-Homebrew/TWiLightMenu)
  * [Guide](https://www.cfwaifu.com/twilight-menu-3ds/)
* [Universal Updater](https://github.com/Universal-Team/Universal-Updater)
* [Homebrew Launcher](https://github.com/PabloMK7/homebrew_launcher_dummy)
* [FBI](https://github.com/Steveice10/FBI)
* [Godemode9](https://github.com/d0k3/GodMode9)
* [3DS Hacking Guide](https://3ds.hacks.guide/)
* [CFW Guide](https://3ds.eiphax.tech/tips.html)

## Hotkeys

* Holding (Select) on boot will launch the Luma3DS configuration menu.
* Holding (Start) on boot will launch GodMode9, or if you have multiple payloads in /luma/payloads/, the Luma3DS chainloader.
* By default, pressing (Left Shoulder) + (Down D-Pad) + (Select) while in 3DS mode will open the Rosalina menu, where you can check system information, take screenshots, enable cheats, and more. This can be changed from the Rosalina menu.
* Holding (Start) + (Select) + (X) on boot will make the notification LED show a color for debug purposes. See the changelog for a list.

TODO DSi hotkeys

# SNES

* [Correct aspect ratios](https://forums.nesdev.org/viewtopic.php?t=23885)

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

* [Online Patcher](https://www.marcrobledo.com/RomPatcher.js/)
* [Checksums](https://www.marcrobledo.com/sfv-checker/)
* Other online patches and utilities: https://www.marcrobledo.com/
* List of popular color hacks and translations: https://www.romhacking.net/forum/index.php?topic=33121.0
Programs here for patching:
* `/programs/patchers/Lunar IPS.exe` to apply `.ips`
* `/programs/patchers/beat.exe` to apple `.bps`
* `/programs/patchers/tsukuyomi ups.exe` to apple `.ups`

## NES

| Hack                                                            | File          | ROM SHA1                                 |
| --------------------------------------------------------------- | ------------- | ---------------------------------------- |
| [Tecmo Super Bowl 2014](https://www.romhacking.net/hacks/1585/) | `TSB2014.ips` | 0A491B125CA1D8BCEBFD19174527D9EEC13820D0 |

## SNES

| Hack                                                                                                                              | File                                               | ROM SHA1                                 |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------- |
| [Dragon Quest III](https://www.romhacking.net/translations/6398/)                                                                 | `Dragon_Quest_III-SNES.zip`                        | B711341E4B1022D7645C5313840874AEBC01B7B7 |
| [F-Zero BS Deluxe](https://www.romhacking.net/hacks/8437/)                                                                        | `bs-deluxe-usa.ips`                                | D3EFD32B68F1FE37A82DB9D9929B7CA7CC1A3AF4 |
| [F-Zero BS Deluxe 1.1](https://archive.org/details/bs_f-zero_deluxe_v1.1)                                                         | `bs_f-zero_deluxe_v1.1.zip`                        | D3EFD32B68F1FE37A82DB9D9929B7CA7CC1A3AF4 |
| [Jurasic Park II - The Chaos Continues Redux](https://romhackplaza.org/romhacks/jurassic-park-ii-the-chaos-continues-redux-snes/) | `Jurassic Park II - The Chaos Continues Redux.zip` | 23967B9DD586C01A8B6E89BB3774C3B3F7BDF3BA |
| [Kirby's Super Star Stacker](https://www.romhacking.net/translations/4917/)                                                       | `Super Star Stacker 1.1.ips`                       | DC252753D4964516419CA981D59A8E704BA41842 |
| [Mario's Super Picross](https://www.romhacking.net/translations/6306/)                                                            | `Marios Super Picross - English Translation.bps`   | C4200B9886B16C148B32D2C75D02F2A875D997CC |
| [Super Mario World - A Plumber For All Seasons](https://www.smwcentral.net/?p=section&a=details&id=28856)                         | `a-plumber-for-all-seasons_2021-11-22.bps`         | 6B47BB75D16514B6A476AA0C73A683A2A4C18765 |
| [Super Bomberman 4 Translation](https://www.romhacking.net/translations/1450)                                                     | `Super Bomberman 4 (jap2eng) v1.0.zip`             | FF580E5A990B1EB4026FDC3669EC6F4A750B6309 |
| [Super Bomberman 5 Translation](https://www.romhacking.net/translations/5333/)                                                    | `sbomb5-beta.7z`                                   | E2DD2F062D3B41F7550FDBC5F7E2B7D0C8AC684C |

[F-Zero BS Deluxe 1.1 release](https://superfamicom.org/blog/2025/03/we-found-bs-f-zero-grand-prix-2-week-1/)

## N64

| Hack                                                                                       | File             | ROM SHA1                               |
| ------------------------------------------------------------------------------------------ | ---------------- | -------------------------------------- |
| [Bomberman 64 - Arcade Edition Translation](https://www.romhacking.net/translations/2755/) | `Bomberman64.7z` | 08E491F87445C6E5C168D982FC665D5F (MD5) |

## GB

| Hack                                                                         | File            | ROM SHA1                                 |
| ---------------------------------------------------------------------------- | --------------- | ---------------------------------------- |
| [For the Frog the Bell Tolls](https://www.romhacking.net/translations/1623/) | `Frog_v1.0.ips` | CE1E4A788327F3099877C88CC848E48C1FD055AB |

## GBC

| Hack                                                                                                                                                           | File                                             | ROM SHA1                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| [Bugs Bunny Crazy Castle 2 DX](https://github.com/supergamerguy777/Bugs-Bunny-Crazy-Castle-2-DX-backup-)                                                       | `Bugs Bunny Crazy Castle 2 DX (v1.0).ips`        | 1E4C8C8FE8B6C34F76CD0DA876442F14299DA725                                                        |
| [Donkey Kong Land DX](https://www.romhacking.net/hacks/6076/)                                                                                                  | `DKL_v1.01.ips`                                  | 4E6D8F085CA197479D59912C1D58E4F3B40C28AC                                                        |
| [Donkey Kong Land 2 DX](https://www.romhacking.net/hacks/6866/)                                                                                                | `DKL2 V1.2.ips`                                  | 89CC4F01653A6105EE5C00E10FC65AA1437FD320                                                        |
| [Donkey Kong Land 3 DX](https://www.romhacking.net/translations/1757/)                                                                                         | `DKL3 - English v1.3.zip`                        | 55B133B739A5472D477336647CB9EC97B7FA85A2                                                        |
| [Dr Mario DX](https://www.romhacking.net/hacks/5281/)                                                                                                          | `dr_mario_dx.ips`, `dr_mario_dx_v21.zip`         | D31D67D0682515C7C85DEAA1752B02231150E5BF                                                        |
| [Final Fantasy Adventure DX](https://www.romhacking.net/hacks/8673/)                                                                                           | `Final Fantasy Adventure DX (USA).ips.zip`       | 8B93C55EE2660C60CF86DD70058F96ACE98782C8                                                        |
| [Kirby's Dream Land 2 DX](https://www.romhacking.net/hacks/7724/)                                                                                              | `Kirby's Dream Land 2 DX v1.0b.bps`              | 8A2898FFA17E25F43793F40C88421D840D372D3C                                                        |
| [Kirby's Dream Land DX](https://www.romhacking.net/hacks/5635/)                                                                                                | `dreamLandDX.ips`                                | 90979BAA1D0E24B41B5C304C5DDAF77450692D5A                                                        |
| [Kirby's Pinball Land DX](https://www.romhacking.net/hacks/6079/)                                                                                              | `Kirby's Pinball Land DX v1.1.ips`               | 06EFDB138FF56CD9522DECE44ADADD3FAE169C76                                                        |
| [Mario Picross 2 (translation)](https://www.romhacking.net/translations/2303/)                                                                                 | `Picross2.ips`                                   | 57788519111CBE9E20B43D1935E9F52AE165E858                                                        |
| [Mega Man - Dr Wily's Revenge DX](https://www.romhacking.net/hacks/7492/)                                                                                      | `MMW1 GBC_v1.02.zip`                             | 277EDB3C844E812BA4B3EB9A96C9C30414541858                                                        |
| [Mega Man II DX](https://www.romhacking.net/hacks/8688/)                                                                                                       | `MMW2 Color v1.01.zip`                           | 334F1A93346D55E1BE2967F0AF952E37AA52FCA7                                                        |
| [Mega Man III DX](https://www.marcrobledo.com/game-boy/mega-man-world-3-dx/)                                                                                   | `mmw3dx_v1_2b.zip`                               | 57347305AB297DAA4332564623C4A098E6DBB1A3                                                        |
| [Mega Man IV DX](https://www.marcrobledo.com/game-boy/mega-man-world-4-dx/)                                                                                    | `mmw4dx_v1_0b.zip`                               | 6F0901DB2B5DCAACE0215C0ABDC21A914FA21B65                                                        |
| [Mega Man V DX](https://www.marcrobledo.com/game-boy/mega-man-world-5-dx/)                                                                                     | `mmw5dx_v1_5_2.zip`                              | 9A7DA0E4D3F49E4A0B94E85CD64E28A687D81260                                                        |
| [Metroid II EJRTQ Colorization](https://www.romhacking.net/hacks/4388/)                                                                                        | `Metroid_II_EJRTQ_Colorization_v1.3.zip`         | 74A2FAD86B9A4C013149B1E214BC4600EFB1066D                                                        |
| [Mobile Golf (translation)](https://www.romhacking.net/translations/6236) ([alternate](https://www.marcrobledo.com/game-boy/mobile-golf-english-translation/)) | `mobile_golf_en_v1_2b.zip`                       | FDE414FC9EFEF2C30D1A9E0A2ED35AD2EFC0EDEE                                                        |
| [Pinball - Revenge of the Gator Gold](https://www.romhacking.net/hacks/7480/)                                                                                  | `GatorGold_v1.zip`                               | 493834DB1C3C7859086A1C570A4BF5E5F6DD332B                                                        |
| [Pokemon Crystal 251](https://www.romhacking.net/hacks/6088/)                                                                                                  | `251 Crystal (2.3).ips`                          | F2F52230B536214EF7C9924F483392993E226CFB                                                        |
| [Pokemon Red/Blue DX](https://www.romhacking.net/hacks/1385/)                                                                                                  | `pokered_color.zip`                              | EA9BCAE617FDF159B045185467AE58B2E4A48B9A (Red), D7037C83E1AE5B39BDE3C30787637BA1D4C48CE2 (Blue) |
| [Pokemon Picross (translation)](https://www.romhacking.net/translations/5702/)                                                                                 | `POKEPICROSS_ENG.ups`                            | 8204064B7149357939B57342820E7955749183B6                                                        |
| [Pokemon TCG 2 (translation)](https://www.romhacking.net/translations/1736/)                                                                                   | `PokemonTCG2-FullTrans.ips`                      | A7E12BCC5F514E3AAD8DE570FD511AAB0A308822                                                        |
| [Super Mario Land 2 DX](https://www.romhacking.net/hacks/3784/)                                                                                                | `SML2DXv181.ips`                                 | BBA408539ECBF8D322324956D859BC86E2A9977B                                                        |
| [Super Mario Land DX](https://www.romhacking.net/hacks/4477/)                                                                                                  | `smldx.ips`                                      | 3A4DDB39B234A67FFB361EE7ABC3D23E0A8B1C89                                                        |
| [Super Robot Pinball](https://www.marcrobledo.com/game-boy/super-robot-pinball-english-translation/)                                                           | `super_robot_pinball_en_v1.zip`                  | 2DBE45E3D5912B270B8BFACC5D9FFC836FE74284                                                        |
| [Wario Land Super Mario Land 3 DX](https://www.romhacking.net/hacks/6683/)                                                                                     | `Wario Land - Super Mario Land 3 DX (World).ips` | AE65800302438E37A99E623A71D1C954D73C843E                                                        |


## GBA

| Hack                                                                       | File                                   | ROM SHA1                                 |
| -------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------- |
| [F-Zero Climax Translation](https://www.romhacking.net/translations/6339/) | `F-Zero Climax English Patch 1.1.ips`  | 6EB9208C493E8BAA43ECC0DACF71A8CB631BE7CA |
| [F-Zero GP Legend eReader Levels](https://www.romhacking.net/hacks/5366/)  | `f-zero_gpl_e+_complete.zip`           | 977588D9D27B7115E0BB309FB019AE81B9F413FF |
| [Mother 3 Fan Translation](https://www.romhacking.net/translations/1333/)  | `MOTHER3_EarthBound2_English_v1.3.zip` | 4F0F493E12C2A8C61B2D809AF03F7ABF87A85776 |
| [Pokemon Liquid Crystal](https://www.romhacking.net/hacks/1901/)           | `PKMNLC-3.3.00512.ips`                 | 41CB23D8DCCC8EBD7C649CD8FBB58EEACE6E2FDC |

## Turbografx-16

| Hack                                                                                    | File           | ROM SHA1                                 |
| --------------------------------------------------------------------------------------- | -------------- | ---------------------------------------- |
| [Lode Runner: Lost Labyrinth Translation](https://www.romhacking.net/translations/673/) | `ldrun_ll.ips` | D3C9813D6133EF0CA468870E9E1C8A8FE8E46C09 |

# Dreamcast

* Manage physical VMUs using SD card adapter + Dreamshell
  * SD card needs `DreamShell_4.0.0_RC4_and_Boot_Loader.7z` expanded in root
  * IMPORTANT: Get the full VMU dumps, not individual saves, otherwise information is lost
* Use `vmuexplorer.exe` to manage the files
  * `*.vmd` files can be renamed `*.bin`
* Delete `dc_nvmem.bin` from Anbernic to clear out the Dreamcast emulator's internal memory (which will clear PSO SN/AK)
  * This only worked deleting over SSH, and did NOT work when deleting from the SD card on PC

# Gamecube

Important Git repos

* [PicoBoot](https://github.com/webhdx/PicoBoot) - PicoBoot firmware for Raspberry Pi Pico
* [iplboot](https://github.com/redolution/iplboot) - I believe PicoBoot uses this to boot
* [Swiss](https://github.com/emukidid/swiss-gc) - main homebrew/ROM launcher
* [CleanRip](https://github.com/emukidid/cleanrip) - homebrew for ripping ROMs
* [GCMM](https://github.com/suloku/gcmm) - homebrew for managing memory cards
* TODO: gameboy player interface
* [GBI-Speedrunning-Fullscreen](https://github.com/ABOhiccups/GBI-Speedrunning-Fullscreen) - presets for GBI

# BlueRetro

* [Web Config](https://blueretro.io/index.html)
* [Documentation](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-BLE-Web-Config-User-Manual)

* HW1 is typically external (N64 adapter)
* HW2 is typically internal (Gamecube port adapter)

# Gameboy Printer/Camera

* [Compilation of printable content](https://www.reddit.com/r/gamecollecting/comments/jx96pc/all_the_images_you_can_print_from_game_boy/)
* [DisplayBoy - GB screen filters on photos](https://coding-fish-1989.github.io/displayboy/)

# Other Assorted Links

* [Genki ShadowCast: How to Fix 1080p Streaming](https://medium.com/@karlphillip/genki-shadowcast-how-to-fix-it-for-free-27d40870eaa0)
* [Some Tips For Optimizing Mupen64 FZ For Nintendo 64 Games](https://www.reddit.com/r/EmulationOnAndroid/comments/pp3uxi/some_tips_for_optimizing_mupen64_fz_for_nintendo/)
* [Miyoo Mini Logos](https://github.com/schmurtzm/Miyoo-Mini-easy-logotweak)

