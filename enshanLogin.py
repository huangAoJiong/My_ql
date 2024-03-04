# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import wx_notify

headers_bonus = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': '_dx_captcha_cid=73780178; _dx_uzZo5y=8785e2f554dd0eaa9e66771d902e03d186fc7edf14be956dbfab242ce50edf4bc9cec9b7; _dx_FMrPY6=6555a311vWYnFqBkc5oR9mZzo6zddVzEAipzfXd1; _dx_app_captchadiscuzpluginbydingxiang2017=6555a311vWYnFqBkc5oR9mZzo6zddVzEAipzfXd1; TWcq_2132_saltkey=iUe4kE4l; TWcq_2132_lastvisit=1700135364; TWcq_2132_connect_is_bind=0; TWcq_2132_nofavfid=1; TWcq_2132_nofocus_forum=1; TWcq_2132_smile=1D1; _dx_captcha_vid=728255F9FEAD123B3E02FB3C3749DD9037CCE87FB4FC4631EE246E403F6F681646135184B794DC9F60E0350378F286D86A1ED3914AB31E4C336C462A9DA33F2796A9E003C800E84A95399E3BD096070B; TWcq_2132_auth=56ef79YaQt1khcdooM1ReFhgxTsoXrTrgmWO7ruLuXatqeEaBJ7REHNEKoc5%2BYv1vmqvdBtvRxutjF1ODyj3FWxYsDw; TWcq_2132_lastcheckfeed=895869%7C1700638262; TWcq_2132_atarget=1; TWcq_2132_sid=Gvs0Za; TWcq_2132_lip=223.76.221.55%2C1700656593; TWcq_2132_pc_size_c=0; TWcq_2132_viewid=tid_4042849; TWcq_2132_ulastactivity=13c1Qji7V9%2FrScjrfuWQxcbqAcdrnf98k7vAPaB1IivcOWpmRVbB; TWcq_2132_sendmail=1; Hm_lvt_4fd617216d6743edf4851b17882cdd82=1700127968,1700644461,1701250022; TWcq_2132_nofocus_home=1; TWcq_2132_home_diymode=1; TWcq_2132_st_p=895869%7C1701250155%7C1c6bffc7e4633ae4bb37d30455d6ac5a; Hm_lpvt_4fd617216d6743edf4851b17882cdd82=1701250157; TWcq_2132_lastact=1701250156%09misc.php%09patch',
    'sec-ch-ua': 'Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}


# 发送GET请求
requests.get('https://www.right.com.cn/forum/thread-4042849-1-1.html', headers=headers_bonus)
response_bonus = requests.get('https://www.right.com.cn/forum/thread-4042849-1-1.html', headers=headers_bonus)
# 输出响应内容
print(response_bonus.status_code)
html = response_bonus
# print(html.text)
html_doc = html.text
# 创建BeautifulSoup对象并指定解析器
soup = BeautifulSoup(html_doc, 'html.parser')

# 获取特定元素，例如，获取id为content的div元素下的所有p标签
content_div = soup.find('div', {'id': 'um'})
paragraphs = content_div.find_all('p')

username = "null"
money = content_div.find('a',  {'id': 'extcreditmenu'})

for p in paragraphs:
    # 找到<p>标签内的<a>标签
    a_tags = p.find_all('a')

    for a in a_tags:
        # 获取<a>标签内的文本内容
        if a.get('title') == '访问我的空间':
            username = a.get_text()
            # print(username)
money = money.get_text().split(':')
wx_notify.send(username, money[1])

# for p in paragraphs:
#     print(p.get_text())
#     sendMsg += f"{p.get_text()}\n"

