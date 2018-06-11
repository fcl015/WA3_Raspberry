cd /home/pi/Code/WA3/WA3_Raspberry/bin
date >> /home/pi/Code/WA3/WA3_Raspberry/log/log_crontab.txt
echo "Starting WA3 Area 2 control loop process" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_crontab.txt
sudo /usr/bin/python3 /home/pi/Code/WA3/WA3_Raspberry/bin/control_loop_area2.py >> /home/pi/Code/WA3/WA3_Raspberry/log/log_crontab.txt
echo "Ending WA3 Area 2 control loop process" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_crontab.txt

