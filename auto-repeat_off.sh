#!/bin/bash

# bash from autostart.sh to fix volume key issue

terminator --command="xset -r"

# you also need to change the volume-step-size property within:
# ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-mixer.xml
# to 0.
