#!/usr/bin/env python

import csv
import array
import datetime

#---------------------------------------------------------------
# Read configuration file
#---------------------------------------------------------------
def read_config_file(file_name,data):
        
        try:
                data.valve_flow=0.0;
                data.smC=0.0;
                data.sm1=0.0;
                data.sm2=0.0;
                data.sm3=0.0;
                data.w_radiation=0.0;
                data.w_temperature=0.0;
                data.w_humidity=0.0;
                data.w_wind=0.0;
                data.w_eto=0.0;
                data.ndvi_alpha=0.0;
                data.ndvi_value=0.0;
         
                with open(file_name) as csvfile:
                        readCSV=csv.reader(csvfile, delimiter='=')
                        for row in readCSV:
                                if row[0]== 'Q':
                                        data.Q=round(float(row[1]),5)
                                if row[0]== 'R':
                                        data.R=round(float(row[1]),5)
                                if row[0]== 'p1_ant':
                                        data.p1_ant=round(float(row[1]),2)
                                if row[0]== 'smKalman_ant':
                                        data.smKalman_ant=round(float(row[1]),2)
                                if row[0]== 'sensor_mac_address':
                                        data.sensor_mac_address=bytearray.fromhex(row[1])
                                if row[0]== 'actuator_mac_address':
                                        data.actuator_mac_address=bytearray.fromhex(row[1])
                                if row[0]== 'weather_mac_address':
                                        data.weather_mac_address=bytearray.fromhex(row[1])
                                if row[0]== 'ndvi_mac_address':
                                        data.ndvi_mac_address=bytearray.fromhex(row[1])
                                if row[0]== 'valve_status':
                                        data.valve_status=int(row[1])
                                if row[0]== 'sm_sensors':
                                        data.sm_sensors=int(row[1],2)
                                if row[0]== 'sm_actuators':
                                        data.sm_actuators=int(row[1],2)
                                if row[0]== 'irrigation_high_limit':
                                        data.irrigation_high_limit=round(float(row[1]),2)
                                if row[0]== 'irrigation_low_limit':
                                        data.irrigation_low_limit=round(float(row[1]),2)
                                if row[0]== 'altitude':
                                        data.altitude=round(float(row[1]),2)
                                if row[0]== 'operation_mode':
                                        data.operation_mode=row[1]
                        csvfile.close()
                return data
        except:
                print("    ERROR Configuration File: Cannot access configuration file");
                return data

#---------------------------------------------------------------
# Read operation mode file
#---------------------------------------------------------------
def read_operation_mode_file(file_name,data):
        
        try:
                data.operation_mode='none'
                with open(file_name) as csvfile:
                        readCSV=csv.reader(csvfile, delimiter=',')
                        for row in readCSV:
                                if row[0]=='operation_mode' and row[1]=='0':
                                        data.operation_mode='manual'
                                elif row[0]=='operation_mode' and row[1]=='1': 
                                        data.operation_mode='sched'
                                elif row[0]=='operation_mode' and row[1]=='2': 
                                        data.operation_mode='auto'
                                else:
                                        data.operation_mode='none'
                        csvfile.close()
                return data
        except:
                print("    ERROR Operation Mode File: Cannot access configuration file");
                return data

#---------------------------------------------------------------
# Update configuration file
#---------------------------------------------------------------
def update_config_file(file_name,data):
        try:
                with open(file_name,"w") as csvfile:
                        writeCSV=csv.writer(csvfile, delimiter='=')
                        writeCSV.writerow(['actuator_mac_address',''.join(['{:02x}'.format(i) for i in data.actuator_mac_address])])
                        writeCSV.writerow(['sensor_mac_address',''.join(['{:02x}'.format(i) for i in data.sensor_mac_address])])
                        writeCSV.writerow(['weather_mac_address',''.join(['{:02x}'.format(i) for i in data.weather_mac_address])])
                        writeCSV.writerow(['ndvi_mac_address',''.join(['{:02x}'.format(i) for i in data.ndvi_mac_address])])
                        writeCSV.writerow(['Q',str('{:7.5f}'.format(data.Q))])
                        writeCSV.writerow(['R',str('{:7.5f}'.format(data.R))])
                        writeCSV.writerow(['p1_ant',str('{:7.5f}'.format(data.p1_ant))])
                        writeCSV.writerow(['smKalman_ant',str('{:5.2f}'.format(data.smKalman_ant))])
                        writeCSV.writerow(['valve_status',str('{:d}'.format(data.valve_status))])
                        writeCSV.writerow(['sm_sensors',str('{0:03b}'.format(data.sm_sensors))])
                        writeCSV.writerow(['sm_actuators',str('{0:03b}'.format(data.sm_actuators))])
                        writeCSV.writerow(['irrigation_high_limit',str('{:5.2f}'.format(data.irrigation_high_limit))])
                        writeCSV.writerow(['irrigation_low_limit',str('{:5.2f}'.format(data.irrigation_low_limit))])
                        writeCSV.writerow(['altitude',str('{:4.0f}'.format(data.altitude))])
                        writeCSV.writerow(['operation_mode',data.operation_mode])
                        csvfile.close()
                return
        except:
                print("    ERROR Conguration File: File was not updated");
                return
                


#---------------------------------------------------------------
# Update log file
#---------------------------------------------------------------
def update_log_file(file_name,data):
        try:
                f1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f2=str('{:5.2f}'.format(data.smC))
                f3=str('{:5.2f}'.format(data.sm1))
                f4=str('{:5.2f}'.format(data.sm2))
                f5=str('{:5.2f}'.format(data.sm3))
                f6=str('{:d}'.format(data.valve_status))
                f7=str('{:5.2f}'.format(data.valve_flow))
                f8=str('{:5.0f}'.format(data.w_radiation))
                f9=str('{:5.2f}'.format(data.w_temperature))
                f10=str('{:5.2f}'.format(data.w_humidity))
                f11=str('{:5.2f}'.format(data.w_wind))
                f12=str('{:5.2f}'.format(data.w_eto))
                f13=str('{:5.3f}'.format(data.ndvi_alpha))
                f14=str('{:5.3f}'.format(data.ndvi_value))
                if data.verbose:
                        print('    ','DATE               ',' ',sep='|')
                        print('    ',f1,' ',sep='|')
                        print('    ','SMC  ','SM1  ','SM2  ','SM3  ','V','FLOW ','RAD  ','TEMP ','HUM  ','WIND ','ETO  ','ALPHA','NDVI ',' ',sep='|')
                        print('    ',f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,' ',sep='|')
                
                with open(file_name,"a") as csvfile:
                        writeCSV=csv.writer(csvfile, delimiter=',')
                        writeCSV.writerow([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14])
                        csvfile.close()
                return
        except:
                print("    ERROR Log File: File was not updated");
                return


#---------------------------------------------------------------
# Update data file
#---------------------------------------------------------------
def update_data_file(file_name,data):
        try:
                f1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f2=str('{:5.2f}'.format(data.smC))
                f3=str('{:5.2f}'.format(data.sm1))
                f4=str('{:5.2f}'.format(data.sm2))
                f5=str('{:5.2f}'.format(data.sm3))
                f6=str('{:d}'.format(data.valve_status))
                f7=str('{:5.2f}'.format(data.valve_flow))
                f8=str('{:5.0f}'.format(data.w_radiation))
                f9=str('{:5.2f}'.format(data.w_temperature))
                f10=str('{:5.2f}'.format(data.w_humidity))
                f11=str('{:5.2f}'.format(data.w_wind))
                f12=str('{:5.2f}'.format(data.w_eto))
                f13=str('{:5.3f}'.format(data.ndvi_alpha))
                f14=str('{:5.3f}'.format(data.ndvi_value))
                
                with open(file_name,"w+") as csvfile:
                        writeCSV=csv.writer(csvfile, delimiter=',')
                        writeCSV.writerow([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14])
                        csvfile.close()
                return
        except:
                print("    ERROR Data File: File was not updated");
                return


#---------------------------------------------------------------
# Read schedule file
#---------------------------------------------------------------
def read_schedule_file(file_name,c_weekday,c_hour,c_min):
        try:
                init_time=0.0
                end_time=0.0
                current_time=0.0
                return_value=False
                with open(file_name) as csvfile:
                        readCSV=csv.reader(csvfile, delimiter=',')
                        for row in readCSV:
                                if int(row[0])==c_weekday:
                                        init_time=float(row[1])+float(row[2])/60.0;
                                        end_time=float(row[3])+float(row[4])/60.0;
                                        current_time=float(c_hour)+float(c_min)/60.0;
                                        if current_time >= init_time and current_time < end_time:
                                              return_value=True  
                        csvfile.close()
                return return_value
        except:
                print("    ERROR Schedule File: Cannot access schedule file");
                return False


#---------------------------------------------------------------
# Read manual control file
#---------------------------------------------------------------
def read_manual_control_file(file_name):
        try:
                return_value=False
                with open(file_name) as csvfile:
                        readCSV=csv.reader(csvfile, delimiter=',')
                        for row in readCSV:
                                if row[0]=='manual_control':
                                        valve_value=int(row[1]);
                                        if valve_value==1:
                                              return_value=True  
                        csvfile.close()
                return return_value
        except:
                print("    ERROR Manual Control File: Cannot access manual control file");
                return False
