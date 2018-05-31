#!/usr/bin/env python

import wa_xbee_comm
import wa_config_data
import wa_control


#---------------------------------------------------------------
# Define data strcutures
#---------------------------------------------------------------
class irrigation_area:
        def __init__(self, id=0):
                self.area_id=id
                self.operation_mode='none'   #Options: none,manual,sched,auto
                self.config_file='../config/config_area'+str(id)+'.csv'
                self.sched_file='../config/sched_area'+str(id)+'.csv'
                self.manual_control_file='../config/manual_control_area'+str(id)+'.csv'
                self.operation_mode_file='../config/operation_mode_area'+str(id)+'.csv'
                self.log_file='../log/log_area'+str(id)+'.csv'
                self.data_file='../data/data_area'+str(id)+'.csv'

                Q=0.0
                R=0.0
                p1_ant=1.0
                smKalman_ant=0.0
                smC=0.0
                sm1=0.0
                sm2=0.0
                sm3=0.0
                sm_sensors=0
                sm_actuators=0
                sensor_mac_address=bytearray()
                actuator_mac_address=bytearray()
                weather_mac_adress=bytearray()
                ndvi_mac_adress=bytearray()
                valve_status=0
                valve_flow=0.0
                irrigation_low_limit=0.0
                irrigation_high_limit=0.0
                altitude=1440
                w_radiation=0.0
                w_temperature=0.0
                w_humidity=0.0
                w_wind=0.0
                w_eto=0.0
                ndvi_alpha=0.0
                ndvi_value=0.0
                comm_status=0
                
                

#---------------------------------------------------------------
# Main program
#---------------------------------------------------------------
area1=irrigation_area(1)

print("(1) Read configuration files")
wa_config_data.read_config_file(area1.config_file,area1)
wa_config_data.read_operation_mode_file(area1.operation_mode_file,area1)
print("    OPERATION MODE: "+area1.operation_mode)

print("(2) Configure serial port")
ser = wa_xbee_comm.config_xbee_comm('/dev/ttyS0',9600)

print("(3) Transmit message to sensor node")
wa_xbee_comm.transmit_sensor_message(ser,area1,'SEN1')

print("(4) Extract data from sensor node")
wa_xbee_comm.receive_sensor_message(ser,area1,'SEN1')

if area1.comm_status:

        print("(5) Calculate control action")
        wa_control.data_fusion(area1)
        wa_control.control_algorithm(area1)

        print("(6) Transmit control action to actuator")
        wa_xbee_comm.transmit_actuator_message(ser,area1,'ACTUATOR')

        print("(7) Receive confirmation from actuator")
        wa_xbee_comm.receive_actuator_message(ser,area1,'ACTUATOR')

else:
        print("(5) No control action due SM data not available")
        print("(6) No action transmit to actuator due SM data not available")
        print("(7) No data receive from actuator due SM data not available")
        
        
print("(8) Transmit message to weather node")
wa_xbee_comm.transmit_weather_message(ser,area1,'WEATHER')

print("(9) Extract data from weather sensor")
wa_xbee_comm.receive_weather_message(ser,area1,'WEATHER')        

print("(10)Update configuration file")
wa_config_data.update_config_file(area1.config_file,area1)

print("(11)Update data file")
wa_config_data.update_data_file(area1.data_file,area1)

print("(12)Update log file")
wa_config_data.update_log_file(area1.log_file,area1)
	


