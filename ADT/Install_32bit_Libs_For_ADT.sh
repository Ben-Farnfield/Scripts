#! /bin/bash

#--------------------------------------------------------------#
#         Installs 32bit libs required by adb and aapt         #
#--------------------------------------------------------------#

pantheon-terminal --execute="sudo apt-get install libc6:i386 \
libstdc++6:i386 zlib1g:i386"

