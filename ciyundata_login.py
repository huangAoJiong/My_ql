# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3
import requests
from bs4 import BeautifulSoup
import time

import sendNotify

send_output=''

send_output+="***********慈云数据签到详情***********"
# 构造请求头
cookies = "__51vcke__K1TtM22rHYgNQAb5=2a2e0e18-be69-5adf-ab7d-2607514dbe1a; __51vuft__K1TtM22rHYgNQAb5=1683249938313; __51uvsct__K1TtM22rHYgNQAb5=3; PHPSESSID=vrfguddsndj78uh88kmhmhr02d; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjU0LjI1NS4xNjIuMTEyIiwiaWF0IjoxNjkxMjE5ODM4LCJuYmYiOjE2OTEyMTk4MzgsImV4cCI6MTY5MTIyNzAzOH0.a4kpP-KJdPx12ofOJzoZjKGm29Q9uIiAQfkHaNA3SsI; AGL_USER_ID=73a85530-a5f0-4691-b967-ce19ce42f8ec"
cookies_end = "PHPSESSID=o5ndq7q4ghqto42kc8najac11o; Hm_lvt_024e02d3bbfa180f1e704c0872386d2e=1680590993; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjIyMy43Ni4yMjEuMyIsImlhdCI6MTY4MDc0ODUwMiwibmJmIjoxNjgwNzQ4NTAyLCJleHAiOjE2ODA3NTU3MDJ9.S_BiorBjkBrGEHwIVNgLkTub0If647TxQmeIDlv8ULw"
refers =['https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index','https://ww.zovps.com/clientarec']
headers1 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookies,
    'Origin': 'https://www.zovps.com',
    'Referer': refers[0],
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.188',
    'X-Requested-With': 'XMLHttpRequest'
}
headers2 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookies,
    'Host': 'www.zovps.com',
    'Origin': 'https://www.zovps.com',
    'Referer': refers[1],
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'X-Requested-With': 'XMLHttpRequest'
}

# 构造POST请求数据
params = {
    '_plugin': '70',
    '_controller': 'index',
    '_action': 'index'
}
data = {'uid': '3906'}

# 创建urllib3的PoolManager对象
bodys = urllib3.request.urlencode(data)
# 发起POST请求
http = urllib3.PoolManager()
http2 = urllib3.PoolManager()
response = http.request(
    'POST',
    'https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index',
    headers=headers1,
    # fields=params
    body=bodys

)
response2 = http2.request(
    'post',
    'https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index',
    headers=headers2,
    fields=params
)
print(response2.status)

date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# 打印响应结果
# print(response.status)
response_text = response.data.decode('utf-8')
decoded_text = bytes(response_text, "utf-8").decode("unicode_escape")
send_output+=decoded_text
# print(decoded_text)
# print(decoded_text.split(':').index('-1'))



## 请求显示余额
# 构造请求头
headers_bonus = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': '__51vcke__K1TtM22rHYgNQAb5=2a2e0e18-be69-5adf-ab7d-2607514dbe1a; __51vuft__K1TtM22rHYgNQAb5=1683249938313; __51uvsct__K1TtM22rHYgNQAb5=3; PHPSESSID=vrfguddsndj78uh88kmhmhr02d; AGL_USER_ID=73a85530-a5f0-4691-b967-ce19ce42f8ec; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjIyMy43Ni4yMjEuNTUiLCJpYXQiOjE2OTEzMDc5NjgsIm5iZiI6MTY5MTMwNzk2OCwiZXhwIjoxNjkxMzE1MTY4fQ.nUNJJC9OHGMHeqS9ZvswaY-0s0tpRUdZVomOZ7AtCNo',
    'referer': 'https://www.zovps.com/addons?_plugin=70&_controller=index&_action=index',
    'cookie':'__51vcke__K1TtM22rHYgNQAb5=2a2e0e18-be69-5adf-ab7d-2607514dbe1a; __51vuft__K1TtM22rHYgNQAb5=1683249938313; __51uvsct__K1TtM22rHYgNQAb5=3; AGL_USER_ID=73a85530-a5f0-4691-b967-ce19ce42f8ec; PHPSESSID=4mck51po8it4d36r59otdn69a0; ZJMF_226527B9B10DA797=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaW5mbyI6eyJpZCI6MzkwNiwidXNlcm5hbWUiOiJcdTllYzRcdTZmYjNcdTcwYWYifSwiaXNzIjoid3d3LmlkY1NtYXJ0LmNvbSIsImF1ZCI6Ind3dy5pZGNTbWFydC5jb20iLCJpcCI6IjUyLjc5LjIzNC4xMSIsImlhdCI6MTY5NDUxMTIyOSwibmJmIjoxNjk0NTExMjI5LCJleHAiOjE2OTQ1MTg0Mjl9.nfIHD-X9n09W4DEpMFJiuehCFW6F03hglvqWYCTorFE',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}

try:
# 发送GET请求
    response_bonus = requests.get('https://www.zovps.com/clientarea', headers=headers_bonus)

# 输出响应内容
# print(response_bonus.text)

    html = response_bonus.text

    soup = BeautifulSoup(html, 'html.parser')
    # sendNotify.send("***********慈云数据签到详情***********",send_output)
    # print(soup)
    current_balance = soup.find('div', {'class': 'zdye'}).find('span', {'class': 'd-inline-flex fz-14 text-black-80'}).text.strip()

    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

    send_output+=f"{date}=>{decoded_text}\n 当前余额：{current_balance}\n\n"

    '''
    with open('login.log','a') as f:
        f.write(date+'=>'+decoded_text+'\t\t'+'当前余额：'+current_balance+'\n')
        f.close()
    '''
    
except Exception as e:
    print(e)

send_output+="***********慈云数据签到结束***********"
sendNotify.send("***********慈云数据签到详情***********",send_output)