#!/bin/bash

#-----------------------------------------------------------#
#     This script sets or removes custom PATH variables.    #
#-----------------------------------------------------------#

#-----------------------------------------------------------#
# WARNING! if you've prev set your path using this script   #
#          you MUST run this script to remove your old PATH # 
#          BEFORE making any changes to the PATH variables. #
#-----------------------------------------------------------#

# Set Your PATH Variables -----------------------------------

# Java
JAVA_VER=jdk1.7.0_40
JAVA_HOME=/usr/local/java/$JAVA_VER/bin
PATH=$JAVA_HOME:$PATH

# ADT tools
ADT_SDK=/usr/local/ADT/sdk
P_TOOLS=$ADT_SDK/platform-tools
TOOLS=$ADT_SDK/tools
PATH=$PATH:$P_TOOLS:$TOOLS


# Add / Remove PATH Variables from ~/.profile ---------------

COMMENT="# set $USER's PATH"
MSG="You must now log out for your PATH to be set"

# check if PATH prev set by this script
PATH_SET=$(egrep "^$COMMENT" ~/.profile)

if [ "X$PATH_SET" = "X" ]; then
	# add PATH to ~/.profile
	printf "$COMMENT\n" >> ~/.profile
	printf "PATH=$PATH" >> ~/.profile
	zenity --info --title="Set PATH" --text "$MSG"
else
	# remove PATH from ~/.profile
	egrep -v "^$COMMENT" ~/.profile > ~/.profile.tmp
	egrep -v "PATH=$PATH" ~/.profile.tmp > ~/.profile
	rm ~/.profile.tmp
	zenity --info --title="Set PATH" --text "$MSG"
fi

exit 0
