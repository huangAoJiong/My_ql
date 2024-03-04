import requests
from wx_notify import send

url = 'https://link-ai.tech/api/chat/web/app/user/sign/in'  # 请求的URL

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTA4MSIsImlhdCI6MTcwNDY5ODgxNywiZXhwIjoxNzA1MzkwMDE3fQ.R2u9_xRb43mCUprf8h2zLyS1e4aMqq6OFGb0mx-v_u2UjV512MrYqLk2xd5koNPVx6iL2qya_J_pmpKVtrwyxw',
    'Connection': 'keep-alive',
    'Cookie': '_gcl_au=1.1.1119734332.1703317262',
    'Host': 'link-ai.tech',
    'Referer': 'https://link-ai.tech/console/account',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

response = requests.get(url, headers=headers)

print(response.status_code)  # 打印状态码
datas=response.json()
if response.status_code == 200:
    if datas['success'] == 'True':
        send("LinkAI 签到",f"打卡成功：获得积分{datas['data']['score']}")
    else:
        send("LinkAI 签到",f"打卡成功：{datas['message']}")
else:
    send("LinkAI 签到",f"签到失败：{datas['message']}")
print(response.json())  # 打印响应的JSON内容
