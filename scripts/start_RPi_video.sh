#!/bin/sh
### BEGIN INIT INFO
# Provides:          RPi video server
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     true
# Short-Description: RPi video server
# Description:       Start the video server and associated helpers
#  This script will start RPi video, and possibly all associated instances.
### END INIT INFO
cd /home/pi/Code/WA3/WA3_Raspberry/log
date >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
echo "Starting RPi video services" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
sudo /home/pi/RPi_Cam_Web_Interface/start.sh >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
