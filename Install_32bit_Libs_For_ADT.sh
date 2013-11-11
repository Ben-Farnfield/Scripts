#! /bin/bash

#--------------------------------------------------------------#
#         Installs 32bit libs required by adb and aapt         #
#--------------------------------------------------------------#

gksudo apt-get -y install libc6:i386 libstdc++6:i386 zlib1g:i386

