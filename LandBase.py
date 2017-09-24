from API_key import *
# API 호출을 위한 키값을 별도 파일에 두고 읽어오기 위해서 추가한 부분
# 실제 값은 프로젝트 디렉토리의 상위 디렉토리에 두며, 여기서 참조하기 위해서 심볼릭 링크로 만들었음
# data_go_kr_apikey
# kosis_kr_apikey

import re
import datetime
import time

import pandas as pd
import numpy as np
from pandas_datareader import data, wb

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothicCoding'
plt.rcParams['axes.grid'] = True 
plt.rcParams['axes.unicode_minus'] = False

# xml을 DataFrame으로 바꾸기
def xml2df(xml_data, p_element_name='items', p_level=2):
    root = ET.fromstring(xml_data) # = ET.XML(xml_data)
    all_records = []
    if (p_level==1) :
        record = {}
        for child in (root.find('body').find(p_element_name)): #for i, child in enumerate(root.find('body').find('items')):
            record[child.tag] = child.text
        all_records.append(record)
    elif (p_level==2) :
        for child in (root.find('body').find(p_element_name)): #for i, child in enumerate(root.find('body').find('items')):
            record = {}
            for subchild in child:
                record[subchild.tag] = subchild.text
            all_records.append(record)

    return pd.DataFrame(all_records)

# 시작일과 종료일 사이의 년도 리스트 반환
def get_yyyy_list(p_from_yyyy, p_to_yyyy) :
    fromdate = datetime.datetime.strptime(p_from_yyyy, '%Y') # 시작년도
    todate = datetime.datetime.strptime(p_to_yyyy, '%Y') # 종료년도
    yyyy_list = []
    while fromdate <= todate :
        yyyy_list.append(fromdate.strftime('%Y'))
        fromdate = fromdate.replace(year = fromdate.year+1)

    return yyyy_list

# 시작일과 종료일 사이의 년월 리스트 반환
def get_ym_list(p_from_ym, p_to_ym) :
    fromdate = datetime.datetime.strptime(p_from_ym, '%Y%m') # 시작기간
    todate = datetime.datetime.strptime(p_to_ym, '%Y%m') # 종료기간
    ym_list = []
    while fromdate <= todate :
        ym_list.append(fromdate.strftime('%Y%m'))
        if fromdate.month == 12 :
            fromdate = fromdate.replace(year = fromdate.year+1, month = 1)
        else :
            fromdate = fromdate.replace(month = fromdate.month+1)

    return ym_list

# DB Connection Open
def get_db_connection() :
    user_name = 'landapp'
    user_password = 'qwer1234'
    schema_name = 'land'
    engine = create_engine('mysql+mysqlconnector://'+user_name+':'+user_password+'@localhost/'+schema_name+'?charset=utf8', convert_unicode=False)
    con = engine.connect()
    return con

# DB Connection Close
def disconnect_db(con) :
    con.close()

# DB에서 sql을 실행했을 때 결과가 있는지 검사
def check_data_exists(con, p_sql) :
    try:
        data = con.execute(p_sql).fetchone()
        if data is None :
            return False
        else:
            return True
    except Exception as e:
        print(e)
        return False

