#!/bin/bash

# Add Java to PATH
export JAVA_HOME=/usr/local/java/jdk1.7.0_40/bin
export PATH=$JAVA_HOME:$PATH

# Add ADT tools to PATH
export ADT_SDK=/usr/local/ADT/sdk
export P_TOOLS=$ADT_SDK/platform-tools
export TOOLS=$ADT_SDK/tools
export PATH=$PATH:$P_TOOLS:$TOOLS

exit 0
