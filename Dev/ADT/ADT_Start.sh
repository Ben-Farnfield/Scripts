#! /bin/bash

#--------------------------------------------------------------#
#      Start adb server with root privileges on ADT start      #
#--------------------------------------------------------------#

ADT_HOME=/opt/ADT
ADB_HOME=$ADT_HOME/sdk/platform-tools

# Restart adb server with root privileges.
$ADB_HOME/adb kill-server
gksudo $ADB_HOME/adb start-server

# Display devices now attached.
DEVICES=$($ADB_HOME/adb devices)
zenity --info --title="Device List" --text "$DEVICES"

# Start ADT.
$ADT_HOME/eclipse/eclipse
