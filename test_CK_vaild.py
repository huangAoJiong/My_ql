 #from 7天前京豆详情 import  getJDCookie()

'''
cron:  0 */2 * * * test_CK_vaild.py
new Env('测试CK有效性');
'''
import json
import threading
import requests


push_config_CK = {
    'PUSH_PLUS_TOKEN': '8f6bb548dc3349d3928effb23b501e2e',
}
notify_function = []


def pushplus_bot_CK(title: str, content: str) -> None:
    """
    通过 push+ 推送消息。
    """
    if not push_config_CK.get("PUSH_PLUS_TOKEN"):
        print("PUSHPLUS 服务的 PUSH_PLUS_TOKEN 未设置!!\n取消推送")
        return
    print("PUSHPLUS 服务启动")

    url = "http://www.pushplus.plus/send"
    data = {
        "token": push_config_CK.get("PUSH_PLUS_TOKEN"),
        "title": title,
        "content": content,
        "topic": push_config_CK.get("PUSH_PLUS_USER"),
    }
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=body, headers=headers).json()

    if response["code"] == 200:
        print("PUSHPLUS 推送成功！")

    else:

        url_old = "http://pushplus.hxtrip.com/send"
        headers["Accept"] = "application/json"
        response = requests.post(url=url_old, data=body, headers=headers).json()

        if response["code"] == 200:
            print("PUSHPLUS(hxtrip) 推送成功！")

        else:
            print("PUSHPLUS 推送失败！")



def send_CK_vaild(title: str, content: str) -> None:
    if not content:
        print(f"{title} 推送内容为空！")
        return
    content += "\n\n(By HBUT server \t——Mr.huang)"

    ts = [
        threading.Thread(target=mode, args=(title, content), name=mode.__name__)
        for mode in notify_function
    ]
    [t.start() for t in ts]
    [t.join() for t in ts]




if push_config_CK.get("PUSH_PLUS_TOKEN"):
    notify_function.append(pushplus_bot_CK)



## 上面是服务器想微信推送消息，下面就是检查cookie是否正确\可用
from  jd_douzi_detail import getJDCookie

ret = getJDCookie()
ret.getCookie()
# global cookiesList, userNameList, pinNameList
status = ret.iscookie()

def main():
    if status == "err":
        print("不正常，不正常了")
        send_CK_vaild("JD_CK", "失效了，赶紧补吧")
    else:
        print("一切正常，就不打扰了")


if __name__ == "__main__":
    main()