#!/bin/bash

#------------------------------------------------#
#                 Update script                  #
#------------------------------------------------#

pantheon-terminal --execute="sudo apt-get update; \
sudo apt-get upgrade; \
sudo apt-get autoremove; \
sudo apt-get autoclean"
