#!/usr/bin/env sh

roscd 
source setup.bash

export ROS_MASTER_URI=http://head.local:11311

exec "$@"
