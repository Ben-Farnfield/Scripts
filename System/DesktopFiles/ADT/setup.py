#! /usr/bin/python

import argparse
import shutil
import os

# CONFIG -----------------------------------------------------------------------

PROG = "ADT"                        # enter program name
COMMENT = "Android Development Kit" # enter comment

# Icon
ICON_SIZES = ["48x48", "64x64"]
ICON_TYPES = ["png", "svg"]
ICON_INST_HOME = "/usr/share/icons/hicolor"


# .desktop

EXEC = "/home/mooli/Scripts/Dev/ADT/ADT_Start.sh" # enter execution instructions
CAT = "Development"           # enter menu entry type

def get_desktop_contents(args):
    return ("[Desktop Entry]\n"+
            "Type=Application\n"+
            "Encoding=UTF-8\n"+
            "Name="+PROG+"\n"+
            "Comment="+COMMENT+"\n"+
            "Exec="+EXEC+"\n"+
            "Icon="+ICON_INST_HOME+"/64x64/apps/"+PROG+"."+args.install+"\n"+
            "Terminal=false\n"
            "Categories="+CAT+";")


# ------------------------------------------------------------------------------


# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--install", 
                        help=("install .desktop and icons. MUST pass the "
                              "icon type as: 'svg' or 'png'"))
    parser.add_argument("-r", "--remove", action="store_true",
                        help="remove .desktop file and icons")
    return parser.parse_args()
 

def install_icons(args):
    icon_name = (PROG+"."+args.install)
    for i in range(len(ICON_SIZES)):
        print ("Installing "+ICON_SIZES[i]+" "+icon_name)
        shutil.copyfile((WRK_DIR+"/icons/"+ICON_SIZES[i]+"/"+icon_name), 
                        (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"+icon_name))


def remove_icons():
    for i in range(len(ICON_SIZES)):
        for j in range(len(ICON_TYPES)):
            icon_path = (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"
                         +PROG+"."+ICON_TYPES[j])
            if os.path.isfile(icon_path):
                print ("Removing "+ICON_SIZES[i]+" "+PROG+"."+ICON_TYPES[j])
                os.remove(icon_path)


def install_desktop(args):
    print "Installing .desktop file"
    desktop = open("/usr/share/applications/"+PROG+".desktop", "w")
    desktop.write(get_desktop_contents(args))
    desktop.close()


def remove_desktop():
    print "Removing .desktop file"
    os.remove("/usr/share/applications/"+PROG+".desktop")


# ------------------------------------------------------------------------------


WRK_DIR = os.getcwd()

args = get_args()

if args.install:
    install_icons(args)
    install_desktop(args)
elif args.remove:
    remove_icons()
    remove_desktop()
else:
    print "Try 'setup.py --help'"
