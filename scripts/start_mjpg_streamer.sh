cd /home/pi/mjpg-streamer/mjpg-streamer-experimental
date >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
echo "Starting mjpg-streamer video services" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
sudo /home/pi/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so" >> /home/pi/Code/WA3/WA3_Raspberry/log/log_video.txt
