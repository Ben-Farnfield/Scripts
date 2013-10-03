#! /bin/bash

export ADT_HOME=/usr/local/ADT
export ADB_HOME=$ADT_HOME/sdk/platform-tools

# Restart adb server with root privileges.
$ADB_HOME/adb kill-server
gksudo $ADB_HOME/adb start-server
$ADB_HOME/adb devices

# Start ADT.
$ADT_HOME/eclipse/eclipse

exit 0
