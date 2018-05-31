# Import grove pi library
import webiopi
import csv
import array
import datetime

# Define variables
sensors = [0 for a in range(14)]
modeValue = 0
manualValue = 0

def setup():
    # Configure variables
    webiopi.sleep(1)

def loop():
    # Read measurements
    data_file_name="/home/pi/Code/WA3/WA3_Raspberry/data/data_area1.csv"
    with open(data_file_name) as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            sensors[0]=row[0];
            sensors[1]=row[1];
            sensors[2]=row[2];
            sensors[3]=row[3];
            sensors[4]=row[4];
            sensors[5]=row[5];
            sensors[6]=row[6];
            sensors[7]=row[7];
            sensors[8]=row[8];
            sensors[9]=row[9];
            sensors[10]=row[10];
            sensors[11]=row[11];
            sensors[12]=row[12];
            sensors[13]=row[13];
        csvfile.close()


# Macro executed from index.html
@webiopi.macro
def getSensor(channel):
    if( int(channel)<14 ):
        return (sensors[int(channel)])
    else:
        return 'XXXX'

@webiopi.macro
def getModeValue():
    mode_file_name="/home/pi/Code/WA3/WA3_Raspberry/config/operation_mode_area1.csv"
    with open(mode_file_name) as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0]=='operation_mode':
                modeValue=int(row[1])
        csvfile.close()   
    return "%d" % modeValue

@webiopi.macro
def setModeValue(value):
    global modeValue
    mode_file_name="/home/pi/Code/WA3/WA3_Raspberry/config/operation_mode_area1.csv"
    if (int(value) <= 2 and int(value) >= 0 ):
        modeValue=int(value)
        with open(mode_file_name,"w+") as csvfile:
            writeCSV=csv.writer(csvfile, delimiter=',')
            writeCSV.writerow(["operation_mode",value])
            csvfile.close()
    return getModeValue();


@webiopi.macro
def getManualValue():
    manual_file_name="/home/pi/Code/WA3/WA3_Raspberry/config/manual_control_area1.csv"
    with open(manual_file_name) as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0]=='manual_control':
                manualValue=int(row[1])
        csvfile.close()   
    return "%d" % manualValue

@webiopi.macro
def setManualValue(value):
    global manualValue
    manual_file_name="/home/pi/Code/WA3/WA3_Raspberry/config/manual_control_area1.csv"
    if (int(value) <= 1 and int(value) >= 0 ):
        manualValue=int(value)
        with open(manual_file_name,"w+") as csvfile:
            writeCSV=csv.writer(csvfile, delimiter=',')
            writeCSV.writerow(["manual_control",value])
            csvfile.close()
    return getManualValue();
