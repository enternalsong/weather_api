import requests
import json
import pandas as pd
import schedule
import time
from update import update

def get_data():
    #get data and make pivot table
    response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0002-001?Authorization=rdec-key-123-45678-011121314&format=JSON')
    json_data = response.text
    data = json.loads(json_data)

    weather_data = pd.json_normalize(data["cwbopendata"]["location"], record_path=["weatherElement"],meta=["locationName","lat","lon","stationId",["time","obsTime"]])
    weather_data_wide = pd.pivot_table(
        weather_data, index=["locationName","lat","lon","stationId","time.obsTime"], columns="elementName", values=["elementValue.value"], aggfunc="first"
    )
    parameter_data = pd.json_normalize(data["cwbopendata"]["location"], record_path=["parameter"],meta=["locationName","lat","lon","stationId",["time","obsTime"]])
    parameter_data_wide = pd.pivot_table(
        parameter_data, index=["locationName","lat","lon","stationId","time.obsTime"], columns="parameterName", values="parameterValue", aggfunc="first"
    )
    concat_data=pd.concat([weather_data_wide, parameter_data_wide], axis=1)
    path = 'rain2.csv'
    concat_data.to_csv(path,sep=',',index=True,header = True)
    #update csv columns
    df = pd.read_csv('rain2.csv', header=None)
    df.iloc[0] = ['locationame','lat','lon','stationid','time','elev','hour_12','hour_24','hour_3','hour_6','min_10','now','rain','latest_2days','latest_3days','attribute','city','city_sn','town','town_sn']
    df.to_csv('rain2.csv', index=False, header=False)
    #updated database
    
    print("success")

schedule.every(10).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(10)