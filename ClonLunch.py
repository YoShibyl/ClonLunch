import os
import sys
import time
import string
import configparser

clonlunch_version = [1,0,0]

print("ClonLunch.py version 1.0.0 by YoshiOG :: https://github.com/YoshiOG1/ClonLunch")

config = configparser.ConfigParser()

config.read("ClonLunch.ini")

if config['Other']['path_to_clone_hero_exe'] == None:
    print("ERROR: You must set path_to_clone_hero_exe in ClonLunch.ini")
    print("If you don't know where your CH is installed, check the Settings tab of \n the Clone Hero Launcher and look for the Install Directory.")
    input("Press Enter to exit...")
    exit()
else:
    ch_exe_path = config['Other']['path_to_clone_hero_exe']

launch_args = " -nolog --launcher-build"

if config.has_option("Graphics", "change_resolution"):
    if config["Graphics"]["change_resolution"].lower() == "true":
        launch_args += " -screen-width %s" % config["Graphics"]["game_width"]
        launch_args += " -screen-height %s" % config["Graphics"]["game_height"]
if config.has_option("Graphics","force_renderer"):
    if config["Graphics"]["force_renderer"].lower() == "d3d11":
        launch_args += " -force-d3d11"
    elif config["Graphics"]["force_renderer"].lower() == "d3d12":
        launch_args += " -force-d3d12"
    elif config["Graphics"]["force_renderer"].lower() == "opengl":
        launch_args += " -force-d3d11"
    elif config["Graphics"]["force_renderer"].lower() == "vulkan":
        launch_args += " -force-vulkan"

if config.has_option("Other", "extra_params") and len(sys.argv) < 2:
    launch_args += " " + config["Other"]["extra_params"]
elif len(sys.argv) >= 2:
    launch_args += " -s \"%s\"" % sys.argv[1]
    for i in range(1,5):
        if config.has_option("Chart Preview", "player%d" % i):
            launch_args += " -p " + config["Chart Preview"]["player%d"%i]
    if config.has_option("Chart Preview", "chart_profile"):
        profile = config["Chart Preview"]["chart_profile"]
        if profile.lower() != "default":
            launch_args += " --profile " + profile
    if config.has_option("Chart Preview", "show_instrument_names"):
        if config["Chart Preview"]["show_instrument_names"].lower() == "true":
            launch_args += " --instrumentNames"

os.popen("\"" + ch_exe_path + "\"" + launch_args)
time.sleep(0.5)
exit()