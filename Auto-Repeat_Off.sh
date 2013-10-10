#!/bin/bash

#--------------------------------------------------------------#
#     Script to fix volume key issue when using Crunchbang     #
#--------------------------------------------------------------#

terminator --command="xset -r"

#--------------------------------------------------------------# 
# Also need to change volume-step-size property to 0 within:   #
# ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-mixer.xml   #
#--------------------------------------------------------------#
