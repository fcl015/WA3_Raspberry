cd /home/pi/Code/WA3/WA3_Raspberry/log
date >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
echo "Stopping RPi video services" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
sudo /home/pi/RPi_Cam_Web_Interface/stop.sh >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt

