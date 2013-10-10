#!/bin/bash

#---------------------------------------------------------------------#
#                      Script to set custom PATH                      #
#---------------------------------------------------------------------#

CURRENT_PATH=$PATH
DEFAULT_PATH=/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
PATH=$DEFAULT_PATH


# Set Your PATH Variables Here ----------------------------------------

# Java
JAVA_VER=jdk1.7.0_40
JAVA_HOME=/usr/local/java/$JAVA_VER/bin
PATH=$JAVA_HOME:$PATH

# ADT tools
ADT_SDK=/usr/local/ADT/sdk
P_TOOLS=$ADT_SDK/platform-tools
TOOLS=$ADT_SDK/tools
PATH=$PATH:$P_TOOLS:$TOOLS

#----------------------------------------------------------------------



# Add / Remove PATH Variables from ~/.profile -------------------------

COMMENT="# set $USER's PATH"
MSG="You MUST now log out to set your PATH."

# check if PATH prev set by this script
PATH_SET=$(egrep "^$COMMENT" ~/.profile)

if [ "X$PATH_SET" = "X" ]; then
	# backup profile
	cp ~/.profile ~/.profile.OLD
	# add PATH to ~/.profile
	printf "$COMMENT\n" >> ~/.profile
	printf "PATH=$PATH" >> ~/.profile
	# info pop-up
	zenity --info --title="info" --text "$MSG"
else
	# backup profile
	cp ~/.profile ~/.profile.OLD
	# remove old PATH from ~/.profile
	egrep -v "PATH=$CURRENT_PATH" ~/.profile > ~/.profile.tmp
	mv ~/.profile.tmp ~/.profile
	# add new PATH to ~/.profile
	printf "PATH=$PATH" >> ~/.profile
	# info pop-up
	zenity --info --title="info" --text "$MSG"
fi

#----------------------------------------------------------------------
