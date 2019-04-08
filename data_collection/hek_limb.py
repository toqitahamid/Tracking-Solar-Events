from sunpy.net import hek
import pandas as pd
import os
import csv
import pytz
import datetime as dt
from datetime import timedelta
import numpy as np
import math


def create_csv(name):
    
    file_name = str(name)+'.csv'
    save_dir = 'csv'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, file_name)
    
    with open(save_path, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['event_starttime', 'event_endtime', 'hpc_bbox', 'hpc_boundcc', 'hpc_coord', 'hpc_radius','boundbox_c1ll', 'boundbox_c2ll', 'boundbox_c1ur', 'boundbox_c2ur',  'frm_name', 'frm_specificid', 'event_type', 'obs_channelid'])
        
    
    csvFile.close()
    
    
def create_csv_noaa(name):
    
    file_name = str(name)+'.csv'
    save_dir = 'csv'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, file_name)
    
    with open(save_path, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['event_starttime', 'event_endtime', 'hpc_bbox', 'hpc_boundcc', 'hpc_coord', 'hpc_radius', 'boundbox_c1ll', 'boundbox_c2ll', 'boundbox_c1ur', 'boundbox_c2ur',  'frm_name', 'ar_noaanum', 'event_type' 'obs_channelid'])
        
    
    csvFile.close()    


def save_event_information_noaa(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, ar_noaanum, event_type, obs_channelid, name):
    data = [[event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, ar_noaanum, event_type, obs_channelid]]
    file_name = str(name)+'.csv'
    save_dir = 'csv'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, file_name)
    
    with open(save_path, 'a') as csvFile:
        writer = csv.writer(csvFile)
        #writer.writerow(['epoch_list', 'train_loss', 'train_loss_mse', 'validation_loss', 'validation_loss_mse','train_time', 'validation_time'])
        writer.writerows(data)
    
    csvFile.close()

def save_event_information(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, frm_specificid, event_type, obs_channelid, name):
    data = [[event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, frm_specificid, event_type, obs_channelid]]
    file_name = str(name)+'.csv'
    save_dir = 'csv'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, file_name)
    
    with open(save_path, 'a') as csvFile:
        writer = csv.writer(csvFile)
        #writer.writerow(['epoch_list', 'train_loss', 'train_loss_mse', 'validation_loss', 'validation_loss_mse','train_time', 'validation_time'])
        writer.writerows(data)
    
    csvFile.close()


def convert_est_to_utc(event_time):
    utc = pytz.utc
    fmt = '%Y-%m-%dT%H:%M:%S'
    eastern=pytz.timezone('US/Eastern')
    date=dt.datetime.strptime(event_time,"%Y-%m-%dT%H:%M:%S") 
    
    date_eastern = eastern.localize(date,is_dst=None)
    date_utc = date_eastern.astimezone(utc)
    
    converted_event_time = date_utc.strftime(fmt) 
    return converted_event_time

client = hek.HEKClient()
startTime = '2015-04-02 00:00:00'
endTime = '2015-04-02 04:00:00'
#endTime = '2014-12-18 18:26:48'


#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('AR'), hek.attrs.FRM.Name == 'SPoCA', hek.attrs.FRM.SpecificID == 'SPoCA_v1.0_AR_0000021612')
#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('AR'), hek.attrs.FRM.Name == 'SPoCA')
results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('AR'), hek.attrs.FRM.Name == 'HMI SHARP', hek.attrs.FRM.SpecificID == '5374')
#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('AR'), hek.attrs.FRM.Name == 'NOAA SWPC Observer', hek.attrs.AR.NOAANum ==  '12553')
#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('SG'), hek.attrs.FRM.Name == 'Sigmoid Sniffer', hek.attrs.AR.NOAANum ==  '1998', hek.attrs.OBS.ChannelID == '131_THIN')

# = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('CH'), hek.attrs.FRM.Name == 'SPoCA', hek.attrs.FRM.SpecificID == 'SPoCA_v1.0_CH_0000023848')
#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('FL'), hek.attrs.FRM.Name == 'SSW Latest Events', hek.attrs.AR.NOAANum ==  '2002')
#results = client.search(hek.attrs.Time(startTime, endTime), hek.attrs.EventType('FL'), hek.attrs.FRM.Name == 'SSW Latest Events')
#SSW_Latest_Events
#SWPC 12002
#[elem["frm_specificid"] for elem in results]
#name = 'FL' + '_' + 'SWPC'+ '_' + '2016-01-01' + '_' + '2016-12-31'

name = 'AR' + '_' + 'HMI'+ '_' + '5374'
create_csv(name)
#create_csv_noaa(name)

for res in results:
    
    
    event_starttime = res['event_starttime']
    #event_starttime = convert_est_to_utc(event_starttime)
    event_endtime = res['event_endtime']
    #event_endtime = convert_est_to_utc(event_endtime)
    hpc_bbox = res['hpc_bbox']
    hpc_boundcc = res['hpc_boundcc']
    hpc_coord = res['hpc_coord']
    hpc_radius = res['hpc_radius']
    boundbox_c1ll = res['boundbox_c1ll']
    boundbox_c2ll = res['boundbox_c2ll']
    boundbox_c1ur = res['boundbox_c1ur']
    boundbox_c2ur = res['boundbox_c2ur']
    frm_name = res['frm_name']
    frm_specificid = res['frm_specificid']
    #ar_noaanum = res['ar_noaanum']
    event_type = res['event_type']
    obs_channelid = res['obs_channelid']
    #name = 'SPoCA_22494'
    save_event_information(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, frm_specificid, event_type, obs_channelid, name)
    
    
    #for NOAA SWPC Observer
    #save_event_information_noaa(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, ar_noaanum, obs_channelid, name)
'''  

x = []
y = []

for angleInDegrees in range(360):
    
    radius = 965.01612
    origin_X = 0.0
    origin_Y = 0.0
    #angleInDegrees = 27
    x.append(float(radius * math.cos(angleInDegrees * math.pi / 180)) + origin_X)
    y.append(float(radius * math.sin(angleInDegrees * math.pi / 180)) + origin_Y)

#(x-center_x)^2 + (y - center_y)^2 < radius^2

center_x = 0.0
center_y = 0.0
radius = 965.01612


def in_circle(center_x, center_y, radius, x, y):
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2

#in_circle(center_x, center_y, radius, 784.233, -336.513)


excluded_name = 'exluded_AR' + '_' + 'SPoCA'+ '_' + '2016-01-01' + '_' + '2016-01-31'
create_csv(excluded_name)

for res in results:
    if (in_circle(center_x, center_y, radius, np.abs(res['hpc_x']), np.abs(res['hpc_y']))):       
#   if (-725.0 <= np.abs(res['hpc_x']) <= 725.0 and -500.0 <= np.abs(res['hpc_y']) <= 500.0 ):
        event_starttime = res['event_starttime']
        #event_starttime = convert_est_to_utc(event_starttime)
        event_endtime = res['event_endtime']
        #event_endtime = convert_est_to_utc(event_endtime)
        hpc_bbox = res['hpc_bbox']
        hpc_boundcc = res['hpc_boundcc']
        hpc_coord = res['hpc_coord']
        hpc_radius = res['hpc_radius']
        boundbox_c1ll = res['boundbox_c1ll']
        boundbox_c2ll = res['boundbox_c2ll']
        boundbox_c1ur = res['boundbox_c1ur']
        boundbox_c2ur = res['boundbox_c2ur']
        frm_name = res['frm_name']
        #frm_specificid = res['frm_specificid']
        ar_noaanum = res['ar_noaanum']
        event_type = res['event_type']
        obs_channelid = res['obs_channelid']
        #name = 'SPoCA_22494'
        #save_event_information(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, frm_specificid, event_type, obs_channelid, name)
        
        #for NOAA SWPC Observer
        save_event_information_noaa(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, hpc_radius, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, ar_noaanum, event_type, obs_channelid, name)
    
    
    elif (in_circle(center_x, center_y, radius, np.abs(res['hpc_x']), np.abs(res['hpc_y'])) == False):
        event_starttime = res['event_starttime']
        #event_starttime = convert_est_to_utc(event_starttime)
        event_endtime = res['event_endtime']
        #event_endtime = convert_est_to_utc(event_endtime)
        hpc_bbox = res['hpc_bbox']
        hpc_boundcc = res['hpc_boundcc']
        hpc_coord = res['hpc_coord']
        boundbox_c1ll = res['boundbox_c1ll']
        boundbox_c2ll = res['boundbox_c2ll']
        boundbox_c1ur = res['boundbox_c1ur']
        boundbox_c2ur = res['boundbox_c2ur']
        frm_name = res['frm_name']
        #frm_specificid = res['frm_specificid']
        ar_noaanum = res['ar_noaanum']
        event_type = res['event_type']
        obs_channelid = res['obs_channelid']
        #name = 'SPoCA_22494'
        #save_event_information(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, frm_specificid, event_type, obs_channelid, name)
        
        
        #for NOAA SWPC Observer
        save_event_information_noaa(event_starttime, event_endtime, hpc_bbox, hpc_boundcc, hpc_coord, boundbox_c1ll, boundbox_c2ll, boundbox_c1ur, boundbox_c2ur,  frm_name, ar_noaanum, event_type, obs_channelid, excluded_name)
        
       
df = pd.read_csv('csv/AR_SPoCA_2016-01-01_2016-01-31.csv', index_col=0)
''' 

'''
#grouped = df.groupby('frm_specificid').filter(lambda x: len(x) >= 3)
grouped = df.groupby('frm_specificid')
gf = grouped.filter(lambda x: len(x['frm_name']) > 5.)
gf_grouped = gf.groupby('frm_specificid')

#gf_grouped['frm_specificid'].agg([np.sum])

'''
'''
for i, g in gf_grouped:
    g.to_csv('grouped_data/FL/' + '{}.csv'.format(i), header=True)
     
'''

'''
for res in results:
    print(res['hpc_boundcc'])
'''

