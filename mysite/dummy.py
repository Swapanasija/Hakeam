#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:09:15 2018

@author: manish
"""

import pandas as pd
import numpy as np
import random
from bs4 import BeautifulSoup
import urllib
import json
import tqdm
from sklearn import preprocessing

def get_dataset_hosp(lat, lng, key='AIzaSyCxDFHxQmsAQP7jXw_tftJDoCFTAOtLkv4'):

    table  = pd.read_csv('specialities.csv')
    sector = ['Govt', 'Private']
    table = table.as_matrix()

    specs = []
    sec = []
    for i in range(0, len(table)):
        specs.append(table[i][0])


    specs_dum = []

    for i in range(0, 1000):
        n= random.sample(range(0, len(specs)-1), random.randint(8,13))
        s = []
        for j in range(0, len(n)):
            s.append(specs[n[j]])
        sec.append(sector[random.randint(0,1)])
        specs_dum.append(s)



    type1='hospital'
    #lat=28.6027739
    #lng =76.9829565
    radius=2000

    url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?key='+key+'&radius='+str(radius)+'&location='+str(lat)+','+str(lng)+'&type='+type1
    #url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?key=AIzaSyBBtnTL-OyYqkpxZm9i8VtPiBv9W0vmCl4&type=hospital&location=28.6027739,76.9829565&radius=3000'
    r = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(r)

    data = soup.get_text()

    file = open('nearby_data.txt', 'w')
    file.write(data)
    file.close()


    data = json.load(open('nearby_data.txt'))

    place_Ids = []

    n = len(data['results'])

    for i in range(0, n):
        place_Ids.append(data['results'][i]['place_id'])

    place_info = []
    time_info = []
    for i in tqdm.tqdm(range(len(place_Ids))):
        url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='+place_Ids[i]+'&key='+key
        url3 = 'https://maps.googleapis.com/maps/api/distancematrix/json?key='+key+'&origins='+str(lat)+','+str(lng)+'&destinations=place_id:'+place_Ids[i]

        r = urllib.request.urlopen(url).read()
        r2 = urllib.request.urlopen(url3).read()

        soup = BeautifulSoup(r)
        soup2 = BeautifulSoup(r2)
        data = soup.get_text()
        data2 = soup2.get_text()
        try:
            file = open('place_data.txt', 'w')
            file.write(data)
            file.close()

            file = open('time_data.txt', 'w')
            file.write(data2)
            file.close()
        except:
            continue

        try:

            data = json.load(open('place_data.txt'))
            data2 = json.load(open('time_data.txt'))
            place_info.append(data)
            time_info.append(data2)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')

    place_dict = []
    for i in tqdm.tqdm(range(len(place_info))):
        dict1 ={}
        d = place_info[i]['result']['name'].split()
        if 'clinic' in d or 'Clinic' in d:
            continue
        dict1['name'] = place_info[i]['result']['name']
        try:
            if place_info[i]['result']['opening_hours']['open_now'] is True:
                dict1['open_now'] = True
            else:
                continue
        except:
            continue
        try:
            dict1['phone'] = place_info[i]['result']['international_phone_number']
        except:
            continue
        try:
            dict1['rating'] = place_info[i]['result']['rating']
        except:
            continue
        dict1['lat'] = float(place_info[i]['result']['geometry']['location']['lat'])
        dict1['lng'] = float(place_info[i]['result']['geometry']['location']['lng'])
        dict1['address'] = place_info[i]['result']['formatted_address']
        dict1['place_id'] = place_info[i]['result']['place_id']
        dict1['rating'] = place_info[i]['result']['rating']
        dict1['specialities'] = specs_dum[i]
        dict1['open_now'] = place_info[i]['result']['opening_hours']['open_now']
        dict1['sec'] = sec[i]

        dict1['time_dur'] =time_info[i]['rows'][0]['elements'][0]['duration']['text']
        dict1['time_sec'] = time_info[i]['rows'][0]['elements'][0]['duration']['value']
        dict1['distance'] = time_info[i]['rows'][0]['elements'][0]['distance']['text']

        place_dict.append(dict1)
    print(place_dict)

    table2 = pd.DataFrame(place_dict)
    table2.to_csv('dummy_dataset.csv', sep=',')
    return table2


def get_best_hosp():
    table = pd.read_csv('dummy_dataset.csv')
    table_x = table.as_matrix()
    headers = np.array(table.columns.values)

    table_f = table_x[:, [ 9, -1]]

    X_scaled = preprocessing.scale(table_f)

    sum1 = []
    for i in range(0 , len(X_scaled)):
        sum1.append(X_scaled[i][1] - X_scaled[i][0])

    sum2 = sorted(sum1)
    index = []
    for i in range(0, len(sum2)):
        ind = sum1.index(sum2[i])
        index.append(ind)

    table_sort = []
    table_sort.append(headers)

    if len(table_x) < 10:
        n = len(table_x)
    else:
        n = 10
    for i in range(0, n):
        table_sort.append(table_x[index[i]])

    table_sort = pd.DataFrame(table_sort)

    table_sort.to_csv('best_hosp.csv', sep=',', header = False)
    return table_sort
