#!/bin/bash

# bash from autostart.sh to fix volume key bug

terminator --command="xset -r"

exit 0

# you also need to change the volume-step-size property within:
# ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-mixer.xml
# to 0.
