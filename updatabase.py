import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
def update():
    conn = psycopg2.connect(database=os.getenv('DB_SCHEMA'), user=os.getenv('DB_USER'), password=os.getenv('DB_CODE'), host=os.getenv('DB_HOST'))
    cur = conn.cursor()
    df = pd.read_csv('rain2.csv')
    for i in range(0,len(df),1):
        save = [None] *20
        row = df.iloc[i]
        save[0] = row[0]
        save[1]= row[1]
        save[2] = row[2]
        save[3]= row[3]
        save[4] = row[4]
        save[5] = row[5]
        save[6] = row[6]
        save[7]= row[7]
        save[8] = row[8]
        save[9] = row[9]
        save[10] = row[10]
        save[11] = row[11]
        save[12]= row[12] 
        save[13]= row[13]
        save[14]=row[14]
        save[15]= row[15]
        save[16] = row[16]
        save[17]= int(row[17])
        save[18] = row[18]
        save[19] = int(row[19])
        sql ="UPDATE rain_hour SET lat=%s,lon=%s,stationid=%s,time=%s,elev=%s,hour_12=%s,hour_24=%s,hour_3=%s,hour_6=%s,min_10=%s,now=%s,rain=%s,latest_2days=%s,latest_3days=%s,attribute=%s,city=%s,city_sn=%s,town=%s,town_sn=%s WHERE index =%s"
        cur.execute(sql,(save[1],save[2],save[3],save[4],save[5],save[6],save[7],save[8],save[9],save[10],save[11],save[12],save[13],save[14],save[15],save[16],save[17],save[18],save[19],i))
    conn.commit()
    cur.close()
    conn.close()