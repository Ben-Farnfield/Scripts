#! /usr/bin/python

import argparse
import subprocess
import getpass
import shutil
import os
import sys

# CONFIG -----------------------------------------------------------------------

USER = "mooli" # enter your user name
PROG = "eclipse" # enter program name
HOME = "/home/{}/Scripts/System/DesktopFiles/{}".format(USER, PROG)

# Icon
ICON_SIZES = ["48x48", "64x64"]
ICON_TYPES = ["png", "svg"]
ICON_INST_HOME = "/usr/share/icons/hicolor"

# .desktop
EXEC = "/opt/eclipse/eclipse" # enter execution instructions
MENU = "Development" # enter menu entry type

# .desktop ---------------------------------------------------------------------

def get_desktop_contents(args):
    return '''[Desktop Entry]
Type=Application
Encoding=UTF-8
Name={}
Comment={}
Exec={}
Icon={}/64x64/apps/{}.{}
Terminal=false
Categories={};'''.format(PROG, PROG, EXEC, ICON_INST_HOME, PROG, 
                         args.install, MENU)

# ------------------------------------------------------------------------------

# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--install", 
                        help=("install .desktop and icons. Must pass the "
                              "icon type as: 'svg' or 'png'"))
    parser.add_argument("-r", "--remove", action="store_true",
                        help="remove .desktop file and icons")
    return parser.parse_args()


def install_icons(args):
    for i in range(len(ICON_SIZES)):
        print "Installing {} {} icons...".format(ICON_SIZES[i], args.install)
        shutil.copyfile("{}/icons/{}/{}.{}"
                        .format(HOME, ICON_SIZES[i], PROG, args.install), 
                        "{}/{}/apps/{}.{}"
                        .format(ICON_INST_HOME, ICON_SIZES[i], PROG, 
                        args.install))


def remove_icons():
    for i in range(len(ICON_SIZES)):
        print "Removing {} icons".format(ICON_SIZES[i])
        for j in range(len(ICON_TYPES)):
            tmp_path = ("{}/{}/apps/{}.{}"
                        .format(ICON_INST_HOME, ICON_SIZES[i], PROG, 
                        ICON_TYPES[j]))
            if os.path.isfile(tmp_path):
                os.remove(tmp_path)


def install_desktop():
    print "Installing .desktop file"


def remove_desktop():
    print "Removing .desktop file"


def check_user():
    if getpass.getuser() != "root":
        print "You need to run as root!"
        sys.exit()

# ------------------------------------------------------------------------------

check_user()

args = get_args()

if args.install:
    install_icons(args)
    install_desktop()
elif args.remove:
    remove_icons()
    remove_desktop()
else:
    print "Try 'setup.py --help'"
