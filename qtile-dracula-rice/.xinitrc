#!/bin/sh
xrandr --newmode "3440x1440_30.00" 196.90 3440 3600 3960 4480 1440 1441 1444 1465 -HSync +Vsync
xrandr --addmode HDMI-2 3440x1440_30.00
xrandr --output HDMI-2 --mode 3440x1440_30.00

lxsession &
udiskie &

nm-applet &
pnmixer &

dunst &
picom &
nitrogen --restore &

exec qtile start
