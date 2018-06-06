#!/usr/bin/env python

import time
import requests


#---------------------------------------------------------------
# Configure serial port
#---------------------------------------------------------------
def update_thingspeak(data,api_key):

        r=requests.post("http://api.thingspeak.com/update",data={'key':api_key,
                'field1':str(data.smC),'field2':str(data.valve_status),'field3':str(data.w_radiation),'field4':str(data.w_temperature),
                'field5':str(data.w_humidity),'field6':str(data.w_wind),'field7':str(data.w_eto),'field8':str(data.ndvi_value)})
        if data.verbose:
                print(r)

        return r
