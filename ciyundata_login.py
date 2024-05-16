# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time : 2023/05/03 10:23
# -------------------------------
# cron "1,30 9 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('慈云签到');
'''
new Env('慈云签到1');
8 8 30 9 * jciyundata_login.py
'''
import json
import re

import requests
from wx_notify import WxPusher_send_message
# 签到
def login():
    url = "https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "PHPSESSID=775nvn4reldussad2a38o90qbg; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjIyMy43Ni4yMjEuMTQ4IiwiaWF0IjoxNzE1ODI3ODY0LCJuYmYiOjE3MTU4Mjc4NjQsImV4cCI6MTcxNTgzNTA2NH0.S_Hb0T-WVtvvDwcrKbXU9LStIxDEnjxbpLTWPbu60N8; YOFDCRU=66ef817cf8a8c4bed99140ec87ae99c7ea94fa4b49e895e9d01fc13ae3e0d6db",
        "Origin": "https://www.zovps.com",
        "Pragma": "no-cache",
        "Referer": "https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = {
        "_plugin": "70",
        "_controller": "index",
        "_action": "index",
        "uid": "3906"
    }
    response = requests.post(url, headers=headers, data=data)
    json_data = json.loads(bytes(response.text, "utf-8").decode("unicode_escape"))
    print(json_data['msg'])
    return json_data['msg']

## 积分查询
def score_search():


    url = 'https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '__51vcke__K1TtM22rHYgNQAb5=2a2e0e18-be69-5adf-ab7d-2607514dbe1a; __51vuft__K1TtM22rHYgNQAb5=1683249938313; AGL_USER_ID=73a85530-a5f0-4691-b967-ce19ce42f8ec; __51uvsct__K1TtM22rHYgNQAb5=6; AffiliateID=HZCZCNTP; PHPSESSID=0du35vsessj9c70m4k52ae4p55; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjIyMy43Ni4yMjEuNTUiLCJpYXQiOjE3MDkyODk1MTUsIm5iZiI6MTcwOTI4OTUxNSwiZXhwIjoxNzA5Mjk2NzE1fQ.nep0Sbu2LGEcV6rUWJZTOnc-aJpxzm7S1kHypv0a6xU',
        'Origin': 'https://www.zovps.com',
        'Referer': 'https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index',
        'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {'uid': '3906',
            'type': 'point'}

    response = requests.post(url, headers=headers, data=data)

    print( bytes(response.text, "utf-8").decode("unicode_escape"))
    json_data = json.loads(bytes(response.text, "utf-8").decode("unicode_escape"))
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', json_data['msg'])
    # return int(numbers[0])
    return json_data['msg']
if __name__ == "__main__":
    WxPusher_send_message("慈云签到得积分", f"{login()}\n{score_search()}")
    # login()
    # print(score_search())

