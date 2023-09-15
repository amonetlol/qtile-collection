#!/bin/sh

function run {
 if ! pgrep $1 ;
  then
    $@&
  fi
}

#run "nitrogen --restore"
xrandr -s 1920x1080
vmware-user-suid-wrapper &
