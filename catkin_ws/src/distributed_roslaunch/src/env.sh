#!/usr/bin/env sh

roscd 
source setup.bash

export ROS_MASTER_URI=http://archbone1:11311

exec "$@"
