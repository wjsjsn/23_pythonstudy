import random

from flask import Flask
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.parse import urlencode

# server01의 내용 접목
url1 = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
response1 = requests.get(url1)
print(response1.content)

url2 = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params2 ={'serviceKey' : '사용자 인증키', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
response2 = requests.get(url2, params=params2)
print(response2.content)

app = Flask(__name__)

# 태그 사용 가능
@app.route('/')
def hello_world():
    return '<h2>random : ' + str(random.random()) + '<h2>'


@app.route('/makeup')
def makeup():
    return response1.content

@app.route('/data')
def data():
    return response2.content

@app.route('/create')
def create():
    return '<h2>Create<h2>'

@app.route('/read/<id>')
def read(id):
    return '<h2>Read %s <h2>' %id

# 디버깅 실행 형식
app.run(debug=True)