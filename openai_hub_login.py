"""
任务名称
name: OpenAI-Hub签到领余额
定时规则
cron: 6 9 * * *
"""
import json

import requests
from wx_send import WxPusher_send_message

MSG = ''


def gpt_hub_login():
    # 请求的 URL
    url = 'https://api.openai-hub.com/api/user/checkin?turnstile=&captchaId=&captcha='

    # 请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Length': '0',
        'Cookie': 'session=MTcxNzA3MzgxOXxEWDhFQVFMX2dBQUJFQUVRQUFEX2xQLUFBQVVHYzNSeWFXNW5EQlFBRW1Ga2JXbHVYMkZqWTJWemMxOW1iR0ZuY3dWcGJuUTJOQVFDQUFBR2MzUnlhVzVuREFRQUFtbGtBMmx1ZEFRRUFQNFBXZ1p6ZEhKcGJtY01DZ0FJZFhObGNtNWhiV1VHYzNSeWFXNW5EQVlBQkVoaGIyb0djM1J5YVc1bkRBWUFCSEp2YkdVRGFXNTBCQUlBQWdaemRISnBibWNNQ0FBR2MzUmhkSFZ6QTJsdWRBUUNBQUk9fPxCjCoKScPJK70r427P28xeSjySkVkd1NeotMtRivvq',
        'Origin': 'https://api.openai-hub.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://api.openai-hub.com/token',
        'Sec-Ch-Ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers)

    # 打印响应内容
    print(response.status_code)
    print(response.text)
    json_data = json.loads(response.text)
    print(f"提示：{json_data['message']}")
    return f"{json_data['message']}"


if __name__ == "__main__":
    MSG = gpt_hub_login()
    WxPusher_send_message('openai-hub签到', f"{MSG}")
