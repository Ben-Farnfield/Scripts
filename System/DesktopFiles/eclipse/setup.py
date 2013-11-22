#! /usr/bin/python

import argparse
import shutil
import os

# CONFIG -----------------------------------------------------------------------

USER = "mooli"   # enter your user name
PROG = "eclipse" # enter program name
HOME = ("/home/"+USER+"/Scripts/System/DesktopFiles/"+PROG)

# Icon
ICON_SIZES = ["48x48", "64x64"]
ICON_TYPES = ["png", "svg"]
ICON_INST_HOME = "/usr/share/icons/hicolor"

# .desktop
EXEC = "/opt/eclipse/eclipse" # enter execution instructions
MENU = "Development"          # enter menu entry type


# .desktop ---------------------------------------------------------------------

def get_desktop_contents(args):
    return ('''[Desktop Entry]
Type=Application
Encoding=UTF-8
Name={}
Comment={}
Exec={}
Icon={}/64x64/apps/{}.{}
Terminal=false
Categories={};'''
.format(PROG, PROG, EXEC, ICON_INST_HOME, PROG, args.install, MENU))


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
        print ("Installing "+ICON_SIZES[i]+" "+icon_name+" icon...")
        shutil.copyfile((HOME+"/icons/"+ICON_SIZES[i]+"/"+icon_name), 
                        (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"+icon_name))


def remove_icons():
    for i in range(len(ICON_SIZES)):
        print "Removing "+ICON_SIZES[i]+" icons"
        for j in range(len(ICON_TYPES)):
            icon_path = (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"
                         +PROG+"."+ICON_TYPES[j])
            if os.path.isfile(icon_path):
                os.remove(icon_path)


def install_desktop():
    print "Installing .desktop file"


def remove_desktop():
    print "Removing .desktop file"

# ------------------------------------------------------------------------------

args = get_args()

if args.install:
    install_icons(args)
    install_desktop()
elif args.remove:
    remove_icons()
    remove_desktop()
else:
    print "Try 'setup.py --help'"
