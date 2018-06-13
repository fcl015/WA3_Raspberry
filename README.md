# WA3_Raspberry

Directories:

bin 	- python executable programs
config 	- csv configuration files
data 	- not used
log 	- output log files
scripts - scripts for crontab and boot
services- configuration for apache and webiopi services
www	- web interface



Files

bin\control_loop_area1.py	- main file for irrigation area 1
bin\control_loop_area2.py	- main file for irrigation area 2
bin\control_loop_area3.py	- main file for irrigation area 3
bin\control_loop_area4.py	- main file for irrigation area 4
bin\wa_config_data.py		- functions to access configuration files
bin\wa_control.py		- functions for control and data fusion algorithms
bin\wa_xbee_comm.py		- function for Zigbee communication
bin\wa_iot_comm.py		- function for IoT interface (ThingSpeak)

config\config_area1.csv		- configuration file for irrigation area 1
config\config_area2.csv		- configuration file for irrigation area 2
config\config_area3.csv		- configuration file for irrigation area 3
config\config_area4.csv		- configuration file for irrigation area 4
config\manual_control_area1.csv	- configuration file for manual irrigation area 1
config\manual_control_area2.csv	- configuration file for manual irrigation area 2
config\manual_control_area3.csv	- configuration file for manual irrigation area 3
config\manual_control_area4.csv	- configuration file for manual irrigation area 4
config\sched_area1.csv		- configuration file for scheduling irrigation area 1
config\sched_area2.csv		- configuration file for scheduling irrigation area 2
config\sched_area3.csv		- configuration file for scheduling irrigation area 3
config\sched_area4.csv		- configuration file for scheduling irrigation area 4
config\operation_mode_area1.csv	- confirguration file for operation mode area 1
config\operation_mode_area2.csv	- confirguration file for operation mode area 2
config\operation_mode_area3.csv	- confirguration file for operation mode area 3
config\operation_mode_area4.csv	- confirguration file for operation mode area 4

log\log_area1.csv		- output data for irrigation area 1
log\log_area2.csv		- output data for irrigation area 2
log\log_area3.csv		- output data for irrigation area 3
log\log_area4.csv		- output data for irrigation area 4
log\crontab.txt			- log data for coontab services
log\video.txt			- log data for video server
log\webiopi.txt			- log data for webiopi server

