#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 04:58:04 2018

@author: manish
"""

import numpy as np
import pandas as pd
import random
from bs4 import BeautifulSoup
import urllib
import json
import tqdm


lat = 28.7499867
lng = 77.1183137
key='AIzaSyAz3TCn2VgbDyPnvWgEfgBBpKjnqlBHYWk'


def get_nurse_info(lat, lng, key):
    info_dict = []
    rlat_min = lat - 0.05
    rlat_max = lat +0.05
    rlng_min = lng - 0.05
    rlng_max = lng + 0.05



    for i in range(0, 50):
        lat1 = random.uniform(rlat_min, rlat_max)
        lng1 = random.uniform(rlng_min, rlng_max)
        info_dict.append([lat1, lng1])


    time_info = []

    for i in tqdm.tqdm(range(len(info_dict))):

        lat2 = info_dict[i][0]
        lng2 = info_dict[i][1]
        url3 = 'https://maps.googleapis.com/maps/api/distancematrix/json?key='+key+'&origins='+str(lat)+','+str(lng)+'&destinations='+str(lat2)+','+str(lng2)


        r2 = urllib.request.urlopen(url3).read()


        soup2 = BeautifulSoup(r2)

        data2 = soup2.get_text()
        try:
            file = open('dist_mat.txt', 'w')
            file.write(data2)
            file.close()
        except:
            continue
        try:
            data2 = json.load(open('dist_mat.txt'))
            time_info.append([data2, lat2, lng2])
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')

    dummy = []
    for i in range(0, len(time_info)):
        dict1 = {}
        dict1['lat'] = time_info[i][1]
        dict1['lng'] = time_info[i][2]
        dict1['time_sec']= time_info[i][0]['rows'][0]['elements'][0]['duration']['value']
        dict1['time_dur'] = time_info[i][0]['rows'][0]['elements'][0]['duration']['text']
        dict1['available'] = 'Nurse'+str(i+1)
        dict1['phone_no'] = '9960'+str(random.randint(100000, 900000))
        if (i+1)/40 >= 1:
            dict1['available'] = 'Doctor'+str(i+1)
        dummy.append(dict1)

    dummy2 = sorted(dummy, key=lambda k: k['time_sec'])
    dummy2 = dummy2[:10]

    dummy_df =  pd.DataFrame(dummy2)
    dummy_df.to_csv('dummy_nurse_dataset.csv', sep=',')
    return dummy_df
