# flask 설치 해야됨

# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서
from urllib.parse import urlencode

import requests
from urllib.request import urlopen, Request
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

from flask import Flask
# server01. 의 내용을 접목 시키자
url1 = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
response1 = requests.get(url1)

url2 = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params ={'serviceKey' : '사용자 인증키', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
response2 = requests.get(url2, params=params)

app = Flask(__name__)

# 태그 사용 가능
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/makeup')
def makeup():
    return response1.content

@app.route('/data')
def data():
    return response2.content

# 원래 실행 형식
# if __name__ == '__main__':
#     app.run()

# 디버깅 실행 형식
app.run(debug=True)