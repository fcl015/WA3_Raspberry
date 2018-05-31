# Import grove pi library
import webiopi
import csv
import array
import datetime

# Define variables
sensors = [0 for a in range(14)]

def setup():
    # Configure variables
    webiopi.sleep(5)

def loop():
    # Read measurements
    file_name="/home/pi/Code/WA3/WA3_Raspberry/data/data_area1.csv"
    with open(file_name) as csvfile:
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
def getPWMValue():
    return "%d" % pwmValue

@webiopi.macro
def setPWMValue(value):
    global pwmValue
    pwmValue=int(value)
    if (pwmValue > 255 ):
        pwmValue=255
    if (pwmValue < 0 ):
        pwmValue=0
    return getPWMValue();
