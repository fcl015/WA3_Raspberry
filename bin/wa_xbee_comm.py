#!/usr/bin/env python

import serial
import array
import datetime


#---------------------------------------------------------------
# Configure serial port
#---------------------------------------------------------------
def config_xbee_comm(device,baud_rate):

        ser=serial.Serial(
                port=device,
                baudrate=baud_rate,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=10
        )
        ser.flushInput()
        ser.flushOutput()
        return ser


#---------------------------------------------------------------
# Transmit message to sensor node
#---------------------------------------------------------------
def transmit_sensor_message(ser,data,message):

        output_message_size=24
        buffer_out=bytearray(output_message_size)
        buffer_out[0]=0x7e  	                # Start character
        buffer_out[1]=0x00	                # MSB data size 
        buffer_out[2]=output_message_size-4	# LSB data size
        buffer_out[3]=0x10	                # TX DigiMesh  64 bits
        buffer_out[4]=0x00	                # Frame ID
        buffer_out[5]=data.sensor_mac_address[0]# 64 bits destination address
        buffer_out[6]=data.sensor_mac_address[1]
        buffer_out[7]=data.sensor_mac_address[2]
        buffer_out[8]=data.sensor_mac_address[3]
        buffer_out[9]=data.sensor_mac_address[4]
        buffer_out[10]=data.sensor_mac_address[5]
        buffer_out[11]=data.sensor_mac_address[6]	
        buffer_out[12]=data.sensor_mac_address[7]
        buffer_out[13]=0xFF	                # 16 bits destination address
        buffer_out[14]=0xFE	
        buffer_out[15]=0x00	                # Broadcast radius
        buffer_out[16]=0x00	                # Options
        buffer_out[17]=ord(message[0])	        # Data
        buffer_out[18]=ord(message[1])
        buffer_out[19]=ord(message[2])
        buffer_out[20]=ord(message[3])          # Sm equation number
        buffer_out[21]=0x00	                # Not used
        buffer_out[22]=0x0A	                # End of packet
        buffer_out[23]=0x00	                # Checksum
        checksum=0;
        for i in range(3,output_message_size-1):
                checksum=checksum+buffer_out[i]
                if checksum > 0xFF:
                        checksum=checksum-0x100
        checksum=0xFF-checksum
        buffer_out[output_message_size-1]=checksum
        # Send message 
        ser.write(buffer_out)
        return

#---------------------------------------------------------------
# Receive message from sensor node
#---------------------------------------------------------------
def receive_sensor_message(ser,data,message):
        
        input_message_size=30
        data_in=bytearray(0);
        data_in=ser.read(input_message_size)
        try:
                extra_data=ser.inWaiting()
                if (data_in[15]!=ord(message[0]) or data_in[10]!=data.sensor_mac_address[6] or data_in[11]!=data.sensor_mac_address[7]):
                        print("    ERROR: Invalid Node Identifier or Invalid MAC address");
                        ser.flushInput()
                        data.comm_status=0;
                        return
                if len(data_in)==input_message_size and extra_data==0:
                        # Extract data from received message
                        data.sm1=data_in[16]+data_in[17]/100
                        data.sm2=data_in[18]+data_in[19]/100
                        data.sm3=data_in[20]+data_in[21]/100
                        # Display data
                        print("    SM1={0:5.2f}, SM2={1:5.2f}, SM3={2:5.2f}".format(data.sm1,data.sm2,data.sm3));
                        data.comm_status=1;
                elif extra_data>0:
                        print("    ERROR Incorrect Message: {} extra-bytes received".format(extra_data))
                        ser.flushInput()
                        data.comm_status=0;
                elif len(data_in)>0: 
                        print("    ERROR Incomplete Message: {} bytes received".format(len(data_in)))
                        ser.flushInput()
                        data.comm_status=0;
                else:        
                        print("    ERROR Timeout: No Message received");
                        data.comm_status=0;
                return
        except:
                print("    ERROR Timeout: No Message received");
                data.comm_status=0;
                return
                

#---------------------------------------------------------------
# Transmit message to actuator node
#---------------------------------------------------------------
def transmit_actuator_message(ser,data,message):

        v1=str('{0:03b}'.format(data.sm_actuators))[2]
        v2=str('{0:03b}'.format(data.sm_actuators))[1]
        v3=str('{0:03b}'.format(data.sm_actuators))[0]

        output_message_size=24
        buffer_out=bytearray(output_message_size)
        buffer_out[0]=0x7e  	                # Start character
        buffer_out[1]=0x00	                # MSB data size 
        buffer_out[2]=output_message_size-4	# LSB data size
        buffer_out[3]=0x10	                # TX DigiMesh  64 bits
        buffer_out[4]=0x00	                # Frame ID
        buffer_out[5]=data.actuator_mac_address[0] # 64 bits destination address
        buffer_out[6]=data.actuator_mac_address[1]
        buffer_out[7]=data.actuator_mac_address[2]
        buffer_out[8]=data.actuator_mac_address[3]
        buffer_out[9]=data.actuator_mac_address[4]
        buffer_out[10]=data.actuator_mac_address[5]
        buffer_out[11]=data.actuator_mac_address[6]	
        buffer_out[12]=data.actuator_mac_address[7]
        buffer_out[13]=0xFF	                # 16 bits destination address
        buffer_out[14]=0xFE	
        buffer_out[15]=0x00	                # Broadcast radius
        buffer_out[16]=0x00	                # Options
        buffer_out[17]=ord(message[0])	        # Data
        if v1=='1':
                buffer_out[18]=data.valve_status+48
        else:
                buffer_out[18]=ord('X')
        if v2=='1':
                buffer_out[19]=data.valve_status+48
        else:
                buffer_out[19]=ord('X')
        if v3=='1':
                buffer_out[20]=data.valve_status+48
        else:
                buffer_out[20]=ord('X')
        buffer_out[21]=0x00                     # Not used
        buffer_out[22]=0x0A                     # End of transmission
        buffer_out[23]=0x00	                # Checksum
        checksum=0;
        for i in range(3,output_message_size-1):
                checksum=checksum+buffer_out[i]
                if checksum > 0xFF:
                        checksum=checksum-0x100
        checksum=0xFF-checksum
        buffer_out[output_message_size-1]=checksum
        # Send message 
        ser.write(buffer_out)
        return


#---------------------------------------------------------------
# Receive message from actuator node
#---------------------------------------------------------------
def receive_actuator_message(ser,data,message):
        
        v1=str('{0:03b}'.format(data.sm_actuators))[2]
        v2=str('{0:03b}'.format(data.sm_actuators))[1]
        v3=str('{0:03b}'.format(data.sm_actuators))[0]                       

        input_message_size=30
        data_in=bytearray(0);
        data_in=ser.read(input_message_size)
        try:
                extra_data=ser.inWaiting()
                if (data_in[15]!=ord(message[0]) or data_in[10]!=data.actuator_mac_address[6] or data_in[11]!=data.actuator_mac_address[7]):
                        print("    ERROR: Invalid Node Identifier or Invalid MAC address");
                        ser.flushInput()
                        data.comm_status=0;
                        return
                if len(data_in)==input_message_size and extra_data==0:
                        # Extract data from received message
                        if v1=='1':
                                print("    VALVE1_STATUS_SENT={0:d}, VALVE1_STATUS_RECEIVED={1:d}".format(data.valve_status,data_in[16]))
                        if v2=='1':
                                print("    VALVE2_STATUS_SENT={0:d}, VALVE2_STATUS_RECEIVED={1:d}".format(data.valve_status,data_in[17]))
                        if v3=='1':        
                                print("    VALVE3_STATUS_SENT={0:d}, VALVE3_STATUS_RECEIVED={1:d}".format(data.valve_status,data_in[18]))
                        data.valve_flow=data_in[19]+data_in[20]/100
                        print("    FLOW={0:5.2f}".format(data.valve_flow))
                        data.comm_status=1;
                elif extra_data>0:
                        print("    ERROR Incorrect Message: {} extra-bytes received".format(extra_data))
                        ser.flushInput()
                        data.comm_status=0;
                elif len(data_in)>0: 
                        print("    ERROR Incomplete Message: {} bytes received".format(len(data_in)))
                        ser.flushInput()
                        data.comm_status=0;
                else:        
                        print("    ERROR Timeout: No Message received");
                        data.comm_status=0;
                return        
        except:
                print("    ERROR Timeout: No Message received");
                data.comm_status=0;
                return

#---------------------------------------------------------------
# Transmit message to weather node
#---------------------------------------------------------------
def transmit_weather_message(ser,data,message):

        output_message_size=24
        buffer_out=bytearray(output_message_size)
        buffer_out[0]=0x7e  	                # Start character
        buffer_out[1]=0x00	                # MSB data size 
        buffer_out[2]=output_message_size-4	# LSB data size
        buffer_out[3]=0x10	                # TX DigiMesh  64 bits
        buffer_out[4]=0x00	                # Frame ID
        buffer_out[5]=data.weather_mac_address[0]# 64 bits destination address
        buffer_out[6]=data.weather_mac_address[1]
        buffer_out[7]=data.weather_mac_address[2]
        buffer_out[8]=data.weather_mac_address[3]
        buffer_out[9]=data.weather_mac_address[4]
        buffer_out[10]=data.weather_mac_address[5]
        buffer_out[11]=data.weather_mac_address[6]	
        buffer_out[12]=data.weather_mac_address[7]
        buffer_out[13]=0xFF	                # 16 bits destination address
        buffer_out[14]=0xFE	
        buffer_out[15]=0x00	                # Broadcast radius
        buffer_out[16]=0x00	                # Options
        buffer_out[17]=ord(message[0])	        # Data
                                                # Month 0-Jan, 1-Feb, ... , 11-Dec
        buffer_out[18]=datetime.datetime.today().month-1                      
                                                # Chihuahua's Altitude=1440 => 0x05A0 
        buffer_out[19]=int(data.altitude)//256       # 05 (high byte) 
        buffer_out[20]=int(data.altitude)%256        # A0 (low byte)
        buffer_out[21]=ord('-')                 # Not used
        buffer_out[22]=0x0A                     # End of transmission
        buffer_out[23]=0x00	                # Checksum
        checksum=0;
        for i in range(3,output_message_size-1):
                checksum=checksum+buffer_out[i]
                if checksum > 0xFF:
                        checksum=checksum-0x100
        checksum=0xFF-checksum
        buffer_out[output_message_size-1]=checksum
        # Send message
        ser.write(buffer_out)
        return

#---------------------------------------------------------------
# Receive message from weather node
#---------------------------------------------------------------
def receive_weather_message(ser,data,message):
        
        input_message_size=30
        data_in=bytearray(0);
        data_in=ser.read(input_message_size)
        try:
                extra_data=ser.inWaiting()
                if (data_in[15]!=ord(message[0]) or data_in[10]!=data.weather_mac_address[6] or data_in[11]!=data.weather_mac_address[7]):
                        print("    ERROR: Invalid Node Identifier or Invalid MAC address");
                        ser.flushInput()
                        data.comm_status=0;
                        return
                if len(data_in)==input_message_size and extra_data==0:
                        # Extract data from received message
                        data.w_radiation=data_in[16]*256+data_in[17]
                        data.w_humidity=data_in[18]+data_in[19]/100
                        data.w_temperature=data_in[20]+data_in[21]/100
                        data.w_wind=data_in[22]+data_in[23]/100
                        data.w_eto=data_in[24]+data_in[25]/100
                        # Display data
                        print("    RAD={0:5.0f}, HUM={1:5.2f}, TEMP={2:5.2f}, WIND={3:5.2f}, ETO={4:5.2f}".format(data.w_radiation,data.w_humidity,data.w_temperature,data.w_wind,data.w_eto));
                        data.comm_status=1;
                elif extra_data>0:
                        print("    ERROR Incorrect Message: {} extra-bytes received".format(extra_data))
                        ser.flushInput()
                        data.comm_status=0;
                elif len(data_in)>0: 
                        print("    ERROR Incomplete Message: {} bytes received".format(len(data_in)))
                        ser.flushInput()
                        data.comm_status=0;
                else:        
                        print("    ERROR Timeout: No Message received");
                        data.comm_status=0;
                return
        except:
                print("    ERROR Timeout: No Message received");
                data.comm_status=0;
                return
                

