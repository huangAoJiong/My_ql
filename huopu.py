
'''
cron:  39 15 * * * huopu.py
new Env('火瀑签到签到');
'''
import requests
from wx_notify import send,  WxPusher_send_message
url = 'https://pos.meituan.com/api/v1/crm/frontend/campaign/sign-in/participate'  # 替换为你要请求的URL
url_status = 'https://pos.meituan.com/api/v1/crm/frontend/campaign/sign-in/records-and-incentives'#2938
cookiess=[
    "_lxsdk_cuid=189c44b4f8fc8-04b3aaba534ff1-26031c51-1fa400-189c44b4f8fc8; IJSESSIONID=node0ag23kui3wi0z19rgljohcpbsf61916025; iuuid=4F7773150B8EDE038A93961F778C170DEB3D5AFBE01746DAC41C41933BD82A62; ci=57; cityname=%E6%AD%A6%E6%B1%89; webp=1; i_extend=H__a100002__b1; __utma=74597006.953042105.1691246773.1691246773.1691246773.1; __utmc=74597006; __utmz=74597006.1691246773.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; pinyin=wuhan; WEBDFPID=u9zxw231u06w52z30008y01u30032065810x370w5x897958z2z64x1v-2006606777716-1691246777463EOOIUOSfd79fef3d01d5e9aadc18ccd4d0c95076546; latlng=30.482875%2C114.303105; ci3=57; _lxsdk=4F7773150B8EDE038A93961F778C170DEB3D5AFBE01746DAC41C41933BD82A62; uuid=8a40d84009f4484f8029.1691246784.1.0.0; token=AgGfJWJ3-TR0ZMlaJq4ezOuH2l1RXaRVWcNC_xGSFLR6VoGryghZy89f34PwRjG2VXd8I2GjWO8TdQAAAAD1GQAA9U9thPhekcCLILDudF4CgPfn507DNlLbJ9e0SKNWcUnekKHv3n77zEK9C4cuoIQe; mt_c_token=AgGfJWJ3-TR0ZMlaJq4ezOuH2l1RXaRVWcNC_xGSFLR6VoGryghZy89f34PwRjG2VXd8I2GjWO8TdQAAAAD1GQAA9U9thPhekcCLILDudF4CgPfn507DNlLbJ9e0SKNWcUnekKHv3n77zEK9C4cuoIQe; oops=AgGfJWJ3-TR0ZMlaJq4ezOuH2l1RXaRVWcNC_xGSFLR6VoGryghZy89f34PwRjG2VXd8I2GjWO8TdQAAAAD1GQAA9U9thPhekcCLILDudF4CgPfn507DNlLbJ9e0SKNWcUnekKHv3n77zEK9C4cuoIQe; userId=281416322; u=281416322; lt=AgGWIgASdCq7Gf0DJGDL3HCS6cr_JtSjYTGHcEw3EZuELpRgTRjAFj7WC2AZjrXm7gYipIG_IInOtwAAAAC6HAAAXl6-o-5yyEspTlk-Urdk-Y59an19mZYm6970JLkywVamRtXit9P_Wl4QfA9fCBpV; n=TKA461631688; token2=AgGWIgASdCq7Gf0DJGDL3HCS6cr_JtSjYTGHcEw3EZuELpRgTRjAFj7WC2AZjrXm7gYipIG_IInOtwAAAAC6HAAAXl6-o-5yyEspTlk-Urdk-Y59an19mZYm6970JLkywVamRtXit9P_Wl4QfA9fCBpV; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; logan_session_token=tzaex4vyqgznth6j7rhr; _lxsdk_s=18cc94f17a0-c34-ec-4d8%7C%7C15; UNI-TOKEN-10029157=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQxOTI1ODEsImp0aSI6ImI2ZTNiNDdkOTRhNDQ3NTlhMTA3ZjEyY2U5N2M4ZDA1IiwibWVtYmVySWQiOjIwNTMxOTU5MTR9.NoUwQ_HxzictljELR3bSMgJV_H50HAhfrWh9jVjfkqU",
    "_lxsdk_cuid=189c44be827c8-082dd8b2c5897a-26031c51-1fa400-189c44be827c8; WEBDFPID=59208u710w5y52yy0xz3wxyz7436z39z810v104vu0097958vy819261-2007184288258-1691824287727MAUCYOIfd79fef3d01d5e9aadc18ccd4d0c95072442; iuuid=5F7FA8EA7ECBAFF10DF6C28077E26FB30953BF8DB83315D93112C2142AD72022; uuid=a40d020cddba4fd38f31.1691824290.1.0.0; token=AgHQHnhlnpnRmi2d2ZkO1pl82ho-ZS8DULpmm_V2Sm28uXyUzCCxFWkKFX2YBT5c8JhL95YxWRLuYwAAAABBGgAAY8VDyxfCGA6KL8Er5FHnCDjfaKPnlbitTpjjA-6CLHMZUq6mT2NYkljMuyJiXxcV; mt_c_token=AgHQHnhlnpnRmi2d2ZkO1pl82ho-ZS8DULpmm_V2Sm28uXyUzCCxFWkKFX2YBT5c8JhL95YxWRLuYwAAAABBGgAAY8VDyxfCGA6KL8Er5FHnCDjfaKPnlbitTpjjA-6CLHMZUq6mT2NYkljMuyJiXxcV; oops=AgHQHnhlnpnRmi2d2ZkO1pl82ho-ZS8DULpmm_V2Sm28uXyUzCCxFWkKFX2YBT5c8JhL95YxWRLuYwAAAABBGgAAY8VDyxfCGA6KL8Er5FHnCDjfaKPnlbitTpjjA-6CLHMZUq6mT2NYkljMuyJiXxcV; userId=281416322; u=281416322; _lxsdk=5F7FA8EA7ECBAFF10DF6C28077E26FB30953BF8DB83315D93112C2142AD72022; logan_session_token=1k24cdvtaa2qgxti1cd3; _lxsdk_s=18cc94ed030-7ac-05c-05d%7C%7C15; UNI-TOKEN-10029157=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQxOTE3MjgsImp0aSI6IjY5YmZmZjkxMWFhNjQ4ZTZhMmQ2NTFkYzAyZDlkODAyIiwibWVtYmVySWQiOjE5ODE4Nzc5MjJ9.BrNVbwZDPCNY_E1IS2Z3UecSHe6FjZfVQXn0eGV3EZU"
]
headers0 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'App-Container': '3',
    'App-Id': '',
    'App-Platform': '99',
    'App-Template': '',
    'App-Version': '',
    'Appcode': '50',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/json',
    'Cookie': cookiess[0],
    'Host': 'pos.meituan.com',
    'M-Appkey': 'fe_com.sankuai.sjstcrm.usercampaign.h5',
    'M-Traceid': '-5880759855751547638',
    'Orgid': '95587',
    'Origin': 'https://pos.meituan.com',
    'Poiid': '0',
    'Poitype': '1',
    'Referer': 'https://pos.meituan.com/web/user/campaign/sign-in-page/10029157/1004623731?poiId=0&tenantId=10029157&poiType=1&orgId=95587&campaignType=87&campaignId=1004623731&from=qrcode&objectCode=signinLimo',
    'Sandbox_strategy': '',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Tenantid': '10029157',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Versioncode': '5361000',
    'X-Platform': '81',
    'X-Wxappversion': '5.43.02'
}
headers2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'App-Container': '3',
    'App-Id': '',
    'App-Platform': '99',
    'App-Template': '',
    'App-Version': '',
    'Appcode': '50',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/json',
    'Cookie': cookiess[1],
    'Host': 'pos.meituan.com',
    'M-Appkey': 'fe_com.sankuai.sjstcrm.usercampaign.h5',
    'M-Traceid': '-5880759855751547638',
    'Orgid': '95587',
    'Origin': 'https://pos.meituan.com',
    'Poiid': '0',
    'Poitype': '1',
    'Referer': 'https://pos.meituan.com/web/user/campaign/sign-in-page/10029157/1004623731?poiId=0&tenantId=10029157&poiType=1&orgId=95587&campaignType=87&campaignId=1004623731&from=qrcode&objectCode=signinLimo',
    'Sandbox_strategy': '',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Tenantid': '10029157',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Versioncode': '5361000',
    'X-Platform': '81',
    'X-Wxappversion': '5.43.02'
}
datas = ['{"campaignId": "1004623731","cardId":"2136555094"}',
         '{"campaignId": "1004623731","cardId":"2063335295","couponDisplayScene":"44", "styleVersion":"2"}',
         '{"campaignId": "1004623731","endTime":"1706716799000","startTime":"1704038400000",'
         '"queryOnlySignInRecordInRange":"false","cardId":"2063335295"}',
         '{"campaignId": "1004623731","endTime":"1706716799000","startTime":"1704038400000",'
         '"queryOnlySignInRecordInRange":"false","cardId":"2136555094"}']  #
# 替换为你要发送的JSON数据

response = requests.post(url, headers=headers0, data=datas[0])
response_status = requests.post(url_status, headers=headers0, data=datas[3])
print(response.status_code)
print(response.json())  # 如果返回的是JSON数据，可以通过response.json()来获取
json1=response.json()
print(response_status.json()['nextStepIncentives']['nextStepIncentivesContent'])
WxPusher_message = ''
if json1['success'] == "True" or json1['success'] == "true":
    WxPusher_message+=json1['nextStepIncentives']['nextStepIncentivesContentPrefix']

else:
    WxPusher_message+=f"7862:{response_status.json()['msg']}, {response_status.json()['nextStepIncentives']['nextStepIncentivesContent']}\n\n"

response2 = requests.post(url, headers=headers2, data=datas[1])

print(response2.status_code)
print(response2.json())  # 如果返回的是JSON数据，可以通过response.json()来获取
jsons2=response2.json()
response2_status = requests.post(url_status, headers=headers2, data=datas[2])
print(response2_status.json()['nextStepIncentives']['nextStepIncentivesContent'])
if jsons2['success'] == "True" or jsons2['success'] == "true":
    WxPusher_message+=f"{jsons2['nextStepIncentives']['nextStepIncentivesContentPrefix']}"
    #send("火瀑31天签到:2938",f"{jsons2['nextStepIncentives']['nextStepIncentivesContentPrefix']}")
else:
    WxPusher_message+=f"2938:{response2_status.json()['msg']}，{response2_status.json()['nextStepIncentives']['nextStepIncentivesContent']}"
    #send("火瀑31天签到:2938",f"{response2_status.json()['nextStepIncentives']['nextStepIncentivesContent']}，2938账号可能没成功，去查看一下：{jsons2['nextStepIncentives']}")
print("***********************")
print(WxPusher_message)
WxPushe