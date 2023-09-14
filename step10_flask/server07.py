import random

from flask import Flask
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.parse import urlencode

app = Flask(__name__)

# 나중에 db 읽어오는 코드로 변경
menu = [
    {'id' : 1, 'title' : 'HTML', 'body' : 'html is'},
    {'id' : 2, 'title' : 'CSS', 'body' : 'css is'},
    {'id' : 3, 'title' : 'JS', 'body' : 'javascript is'}
]

# 태그 사용 가능
@app.route('/')
def index():
    liTags = ""
    for i in menu:
        # f-string 사용법
        # 1. 문자열 앞에 f를 붙임
        # 2. 문자열 중간에 변수나 계산식 넣을 수 있음({} 이용)
        liTags = liTags + f'<li><a href="/read/{i["id"]}" />{i["title"]}</a></li>'
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
    return '<h2>Create<h2>'

# 파라미터는 string인데 int로 변경(<int:id>
@app.route('/read/<int:id>')
def read(id):
    liTags = ""
    for i in menu:
        liTags = liTags + f'<li><a href="/read/{i["id"]}" />{i["title"]}</a></li>'

    title = ''
    body = ''
    for i in menu:
        if id == i['id']:
            title = i['title']
            body = i['body']
            break
    return f'''
        <!doctype html>
            <html>
                <body>
                    <h1><a href="/">WEB</a></h1>
                    <ol>
                        {liTags}
                    </ol>
                        <h2>{title}</h2>
                        {body}
                </body>
            </html> 
    '''

# 디버깅 실행 형식
app.run(debug=True)