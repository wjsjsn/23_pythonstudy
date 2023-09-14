# flask 설치 해야됨
import random
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서
from urllib.parse import urlencode

import requests
from urllib.request import urlopen, Request
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

from flask import Flask
# server01. 의 내용을 접목 시키자

app = Flask(__name__)

# 나중에 DB 읽어 오는 코드로 변경된다.
menu = [
    {'id':1, 'title':'HTML', 'body':'html is ...'},
    {'id':2, 'title':'CSS', 'body':'html is ...'},
    {'id':3, 'title':'JS', 'body':'html is ...'}
]

@app.route('/')
def index():
    liTags = ""
    for i in  menu:
        # f-string 사용법
        # 1. 문자열 앞에 f를 붙인다.
        # 2. 문자열 중간에 변수나 계산식으로 넣을수 있다(중괄호{}를 이용하면)
        liTags = liTags + f'<li><a href="/read/{i["id"]}">{i["title"]}</a></li>'
    return f'''
    <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                    <h2>Welcome</h2>
                    Hello, Web
            </body>
        </html>
'''


@app.route('/create')
def create():
    return '<h2> create </h2>'

@app.route('/read/<id>')
def read(id):
    return '<h2> Read %s </h2>' %id

# 디버깅 실행 형식
app.run(debug=True)