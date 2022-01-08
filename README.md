# ClonLunch
A Clone Hero v1.0.0+ alternative launcher written in Python 3 for Windows *(not tested on other platforms)*

## Usage
This script can be used either for setting the game to a custom resolution, or for loading directly into a song to preview it.

First, download the latest version from [Releases](https://github.com/YoshiOG1/ClonLunch/releases/latest).  Then, make sure to edit the `ClonLunch.ini` file according to the settings below.

## Config (`ClonLunch.ini`)

### Graphics
- `change_resolution` : Set to `True` or `False` to enable or disable changing the game window's resolution.
- `game_width`, `game_height` : Window size in pixels (self-explanatory)
- `force_renderer` : Force the game renderer to one of the following: `d3d11` (Direct3D 11), `d3d12`, `opengl` (OpenGL), `vulkan`, `auto`

### Chart Preview
Drag and drop the folder of a song onto `ClonLunch.py` to launch directly into that song with the bot enabled. Very useful for charters looking to make chart previews without needing multiple gamepads.

It is not currently possible to set modifiers, such as 2x Kick on Drums.

- `chart_profile` : (optional) Set to the name of your in-game profile to use it for all players in the chart preview. If set to a non-existent profile, then the default (Guest) will be used.
- `show_instrument_names` : Whether to show the instrument name on each highway (True/False)
- `player1`-`player4` : Set the instrument and difficulty of each bot player. Players 2, 3, and 4 are optional and can be commented out with a `#` symbol.
  - Syntax: `instrument,difficulty`
  - Known Instruments: `guitar`, `guitarcoop`, `guitar6fret`, `bass`, `bass6fret`, `drums`, `prodrums`, `keys`
  - Difficulties: `expert`, `hard`, `medium`, `easy`

### Other
- `path_to_clone_hero_exe` : **IMPORTANT!** This must be set to the filepath of your `Clone Hero.exe` installation, including the file name.  Otherwise, the script will fail!

## Credits
- YoshiOG : Author of this Python script
- mdsitton : One of the developers of Clone Hero, who informed me of the command-line arguments that can be used with Clone Hero
  - Twitch channel: https://twitch.tv/mdsitton
- srylain : Creator of Clone Hero
  - https://clonehero.net/

Download the latest build of Clone Hero using the Clone Hero Launcher, which can be acquired on the official Clone Hero Discord server: https://discord.gg/Hsn4Cgu
- You'll need to opt-in to the public test builds (PTB) in `#ptb-opt-in`
