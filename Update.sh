#!/bin/bash

terminator --command="sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get autoremove && \
sudo apt-get autoclean"

exit 0
