# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/14
# @Author  : Haoj
# @File    : Microsoft_Rewards.py
# @Software: PyCharm

'''
cron:  33 13 * * * Microsoft_Rewards.py
new Env('微软Rewards积分');
'''
import random
import time
import requests
import json


# 查询总积分
def get_total_scores():
    # 目标URL
    url = 'https://rewards.bing.com/api/reportactivity?X-Requested-With=XMLHttpRequest'

    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_C_Auth=; MUID=1403F992615664E622EBEDD6602E6575; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=2DBCD5071A6649D1B23911A9AA0D9F5D&dmnchg=1; ANON=A=86C2E4898087F7B1A49F4FAAFFFFFFFF; SRCHUSR=DOB=20240316&T=1710618863000; BFBUSR=BAWAS=1&BAWFS=1; BFB=AxDuEe_l2G8QBQqwuyxKGntWqPRyAFGZbV84A2w5EnWct83gbDrNRHq-Nwb0VCEz1F0M4dBqSejdYM_DhVRrsMFoa2waHQvY0I-j6GVU8GVCsxd170T1Zn9OIKXXJw9-U6FyZPfFSGIh8NQmF8fPa8hIrm0o-zeOvmG-JvSCoGZYxsHTswn5d1l5hk1SdeJUPJk; OIDI=AxCPo05uYN8mh9-Pl4HhWkT57grxqP_vEcmCIZGBLZ0jZw; MMCASM=ID=D35B11A548F04E1BA86B6289BEF6823B; ANIMIA=FRE=1; MUIDB=1403F992615664E622EBEDD6602E6575; vdp=%7B%22ex%22%3Atrue%2C%22red%22%3Afalse%7D; MicrosoftApplicationsTelemetryDeviceId=075ef574-2d8e-4344-bd20-2d63acc9d385; MicrosoftApplicationsTelemetryFirstLaunchTime=2024-03-23T15:52:58.259Z; MSCCSC=1; MSPTC=QRDvrE7HLtIaxiNi4Xgj9r1ncOMjvfOzEBJFoe7-PpQ; MUIDB=1403F992615664E622EBEDD6602E6575; mapc=rm=0; WLS=C=d4f13ef6c1b0be3a&N=%e6%be%b3%e7%82%af; SRCHS=PC=U531; _Rwho=u=d&ts=2024-05-06; EDGSRCHHPGUSR=CIBV=1.1719.0; _C_Auth=; .AspNetCore.Antiforgery.icPscOZlg04=CfDJ8F79XorNUSlPuQIOpL4R67qcpRw3-qyipDjTheugpKV3flxzz3X-ILYDhQKn_d3RrHeKWmJIZZU6_SG0L_KJmqnuUXhlVih1UdM4acLyI2h1M0L5h-dO-7kd4jlsQavOAK850HIJNOgaQZguoJBsOac; GRNID=269f056e-760d-49d4-b55e-e3fc749158dc; tifacfaatcs=CfDJ8F79XorNUSlPuQIOpL4R67oKceWFn4omtGn31OBgTtYt3eiujlvJjrPWEqDbBR-ixLXBr62NzxekOLkvg952j3tN0FQ7suSEcaKcI5ZMXol4DGhpWMA23UTAYYJ6fCQjRHck1inRH4W_nigRSLXHqF7f5QmBch9AjTUyaCQ7LScXvMgiCATsyusNT55s0emrOZfMxJSvI94GygOQWKbJym1PH9obxTuXU7TYe3grV3Lh62N_fGhtoHzfOlmHCVpBea3OEXCQ8TIeT4Vw--6XoYiuJhVk0IYMvqJYFhfjNHPRwl862FQ67bvXoWvsU4CZ03SPFZ40IXneRtF804d8jW396m0A38HJ8g7lmZg_zd8zoTbQr2wTqKKVrC5r8NLqwDTbnGVsy_3MFLM9cOzUwbRebjn_G9bo-v8yFK0Glg7E6mvGkWab0fsWxFpanhMh5YnvKj6udsHi9HMtu1d9UYiAnDLtkzylZDDdgiz_POgTGHh-v6bmEs3x-ygUIvaE0ey2us87gow8UNK0v3SKS8aYm6vBwjUmMH_dZvchSqUQhfpbvsTCMR7whyK2ZApCT7zwnLZrFp51fccKeazb5lb-VlihZ5WcQKt1n1UWWBcHEaEiiQh-1VqrOhxAuIwUUZmNeUqJMvbPDW6FIyCTS9mouo0A4QSHm5A77rWp3O6nwXCytcBOEHfYOvKxKKXcGCpPMhTHTYUwezfADuUXaCnTX8_eB1lzsMAK_M1IX3tI12phNC1J9p_IqZ07Y1Tq-ZR_Jyj02gZ0ZP6vrK0pWmxiO_lgT-gX4IPkiZkMfGcYevfsrfGH6fVkIoaMI4hz55y4VfyxpEcHvUyczkhws528MkeMJyq7b-5BRWBK7fdy_IEqpc-fTUpG523LLGPFAzaobpGfP4PuIHn3eVVVSk4M6JKyKY9iZoerNeSfQjvrsZoq0aOHEsOTuRn8ZOnqcIGGJxnFV93D8CiQ_vIE5D5wq-8DRBmiknrnZj30fXlC4-gyQem6CtuESWl_xMvaWsKZxDkXLWJs3xZf0jfD8YTTZB6ntNpnlLXMCyCRwXs1qI83GGQ253qWJQrDCohkgGSHtH3sNurO_jfsJfTz1rdknkyi5CDdWbs18Gok7GGBaHaExn-Z84j5dsYnfOjIaKqGP_nbrpsvZaRlWIMmoT718UR0mwRsRgPdTV8PMJVydb1ccLNYYos-KVRpYDM_1akWAdkQ0TQsSQkRgsxn0_KwtcME-ezpF5GgouKEgtNzhQzoAz3o2hmhOftnnw7NF1dkiM2lvC7xXcSPMF_JVFacjlq8dOcxkg_HloagHYODpE_Fq19SLxPc4vD-koaZPnJLdr1xIqB-K2Fcj6ztQryP9GTGgpK_fSE2N3GOvNXxLVt1haAiC7IuQJHkHTx8FtNSW2-LJPs3Y-DavA78gaEdO1BWkur8IM6vwwun5bqmAdyCABEFQXKMjVr1XC-92NDtdGsgzKws0mzQ1fglQ8v-oW1SSUN04z3TQLk98P-ziEQXwG4kuTH0tzMuSA9f16tvG7IlJk2T5CT10jXJ7rEBcSgjGWpivzpFg1sYjW8Dl9VGZy3ANf_PTPSJI2ervAOhuaXAJURNt84mz1NhFa_v3S8eSdhxFVbPSUgrq8xik28C6o7pyK13s8pDcrGsvGZa-5PUmzaLXp-m8JXiadF4crgDgjHewkqnpcpSWwSr8SzHEb4YsKLQZovxfZP_bLjF8n4I4ZwW6ssSEFR1QB6ZP1Mn52eYoQxjfRurusfQ09S-N1PwicwsiJm7aMu5Y0LDXzz7KZ19L0cHi54gVXjPumEncnxHiJOwNt__X4_u49MfDGiySEkQ1lU102FzRlKB0TshlRiJL2CF8LlCuyMy4heQpYh9ZAP6H1DTmvHRRtknidAcbCM6eCyIQzInB6lXwteYs3UOkXYqc0Wi5r7lF5t8ErFfG68BTJ-qzwC8c6yrD3ntHpqz7sNiVW1OmZJUQH_zHUC4MTUXQWYSP5lDyuBi51TX3DnGi8RzhFL1kA8a_5ZKIpYutClJOz-sSE2IrzMoOlMVPThc4ZGqNduxaKYkBeekGdNeNCLYNxlDzqCj3WBneT5RhWGHs7oMuMuE4G5RDZfmmRQ0YYfnyt2v97KcmD1iyC2dFwZZMwraCKrkHpAmv6wZQ6tiVd_kw9jnacZqpXpOZOmDtBUB3pE_J08cZfz_ZOMqyFffzMxLV9Uo6_ZMwq-8aBmMJS-jJoBDEqPtEnqZYTGAf7SR53W8dB2RnRutgB_2GQLl6uux5B_PQhAhbDkjI6l29NOjxcFYQ7QQBuAsNZjK8S2groT_p7Fj2hBSsPHF9xTTSCfFm2vvWoZFYVh52wFrc0oL34gnhJjzDjwHTjrIPpWFdJi6xutQUfqa8mKm-7caiFDCJroWJSR_ffN5h7rcjmZCHAjuxaLtoeki_mMnIGBZ0hpI--rt5c-OhRZAqo0bZsHq6rA7ExrKP3N_pAWSh8hgnyLMInvdGLT5DhdGpnzbVgbckVBlIKrL6dy0gNYTlAH1BeYMtWCqijHL4vlbS9Cby3I21K4teCe_OSrxyj_9Hgu3_FV4Pb7nW-iREwvy3wHkUy7_PR_9ie-P2muYHsBbvJMrHtCLv3g-h_cxg-8QQAOM-Ij-mOt1ND-OnwvCnixB5-ZNDsXsUw3HCKkYDa2HlMpU4PsWohFkJjuMMCJz7jiXg4rm6o_ORQ5FY4klCsK4wgEetJ56o75zmasKKQSTaH0t3n3WZFYqyQATnavTEdR-soykOl0ZktdFuyEUYy9W--mUSsmr4FDjvtb4WoAo-bImTh1lhLaf5HE8_VC5FXTERf5W9uNcpIb7OTEr40dHTn9PhnV7_VYcHK5YnCBJEfVRRIBGRQygwIYOpY6y9H4HND-xdsDvMI4YCwxoGzNsExHKxzg8dfPHKx-ue4H8vynewh4FKiUQQBaCscFb43pb-U3lcqBtmyM_6Wot9uyP90zv0KW2rr_ACK_ZmeXZFWaQ8SkrbZxfDQNeZyK4oKf7Uwkjd7eI4U8l5hTNIqfsO11wv2Hnecznyz8eVbdz9P-mPyvD3wH7fikq2pJokOiwDS4IsA3cv_gyy-Lvn0tFfoRRlfM6M8UG5p9O3MALQJEDc2VLblFH5DDtAQJ5svTjIt9-FNhhWxKLWCVd6bX0w1aZwF0u7iHDuS3pkYMTHUWOBWXtcHTTfJSYVRuj7b7fINA0LpB4pSY6Qh6FUqvEFx9TntRTVf7SGl4wrkus4pkO8NiPEeXGX5z7HaFogs_9jU60FpidlNGuOqXvwTom4443XFDM_GTZLez4g-K87TDRf2QK0TK7ni4a7V8QLAShOzF6L76wuCh1vgGfm9U2AGfcansHqNI17fhIsbZvGiiVOUJJ5n9I5AjW9iDihkpj85ap-MQVyv1r-duM5mlV1T2gHYXQ3iltt1VLlrTAx6p6QmBFQi6QRoaOA4h6dS5ISn0yai-7lDm0lTmGx3NUTmm7xXaMP_B3PwR43quTtbSy6s6SrJ48HTSP9R0G4TyN5k3BC7PRc_nO_B4UGu569pEHz1L437OqPZ2WU0IEDt__aemiljBXYH59dSIT6zdJbVcFXwn3n5HB35zA9eWmV87afQ4Gi4Zv3i9MxfAm94LXjO35KiJXGK47bJr2H8WedlF0MheeMLoSfgiZstvEF7rjW2_Si4B269CbehD7pUMtXIRqBzdglNuxvTNBpxMzS4PBNXgqKruVeCz28oKQ; SnrOvr=X=rebateson; _EDGE_S=SID=2917DAE1B6B9686C3F84CE96B79769CE&mkt=EN-US&ui=zh-cn; MSCC=cid=saj132lqys7meaj2ho8bsro8-c1=2-c2=2-c3=2; BFPRResults=FirstPageUrls=A362573359DDE14CAD37767E64103398%2C3B85F5930A4AFC329DE7C4EB4956D9FB%2CAAE5EEABB86B766B9B7AA0FE7B60DA75%2CAB20F4FDB1BAFF3EF816812D824EC0A3%2CF2D53E5113CBD54C9EB7B45F0B662153%2C53F71A4F75C9037424108C3FE42C1F1D%2C4583F56BA0F296043C3B47A3C5726BE8%2CEAB388DEB6612D60549C8FABB07AD465%2C45A9665DC32D2068BCB953A8D6285595%2C58F8B78CA6E2C4BBE4A0ACAAAF13ADC5&FPIG=9C58268C710D4F4CB626ECE316D06108; OID=gxDc5N5DQPKsHWzWu1OLpyldGuVBNh53s5byMbjb9U9HZA; _SS=SID=2917DAE1B6B9686C3F84CE96B79769CE&PC=U531&R=4687&RB=4687&GB=0&RG=89570&RP=4684&RA=-&BTOID=-&BTQID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-&BTSTKey=-&OCID=ML2BFU; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&HV=1715320307&BRW=HTP&BRH=M&CW=869&CH=966&SCW=1164&SCH=2255&DPR=1.0&UTC=480&DM=0&EXLTT=31&CIBV=1.1719.0&PRVCW=869&PRVCH=966&BZA=0&IG=F50DEA4D65484AC79E2CBDE3027D4D06; USRLOC=HS=1&ELOC=LAT=30.4775333404541|LON=114.29781341552734|N=%E6%B4%AA%E5%B1%B1%E5%8C%BA%EF%BC%8C%E6%B9%96%E5%8C%97%E7%9C%81|ELT=4|&DLOC=LAT=30.4805|LON=114.3049|A=10458|N=%e6%ad%a6%e6%b1%89%e5%b8%82%e6%b4%aa%e5%b1%b1%e5%8c%ba|C=|S=|TS=240510055146|ETS=240510060146|&BID=MjQwNTA5MjMxMDE3Xzc5MWIxNGE1MGQ0NTE2ZWEzODY1OGI2MTFlZjQ2Y2E0NmVjMjZlNThkYWY0NGM2MTI5NTMwYjYwNjljZDllNTc=; ipv6=hit=1715323909122; _clck=15qwo4i%7C2%7Cfln%7C1%7C1544; _uetsid=9943bfe00e9111efa13881733cb131b4; _uetvid=0d273760e9bc11ee81e12d9fa88bc004; SNRHOP=I=&TS=; _RwBf=r=1&mta=0&rc=4687&rb=4687&gb=0&rg=89570&pc=4684&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=38&l=2024-05-09T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-05-07T18:36:07.4079092-07:00&rwflt=2024-05-06T21:38:49.2395147-07:00&o=16&p=WINDOWSBARACQ201902&c=M5001O&t=4878&s=2022-08-16T01:47:02.9424911+00:00&ts=2024-05-10T05:51:43.3489322+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&e=tK3Ul9rmy4R0_mIa8RCAMeP1F8nRy7fV3aUMdPo2-wwFnYMrLnAl2zhVSYvPpN7S5_LQgYZLX2tHwXeepqoyrg&A=86C2E4898087F7B1A49F4FAAFFFFFFFF&cpt=0; _U=1W49JEX3A60og_CMp_Prb1xXJkBqOJW7OyQezwiRVMgpSIYuABgFyiQ5UVQQaAAXozQ_j6eH7nKLtZlNdju83z05Bauhs16qnPnF6zlG-1_2rOD564dUbz0GnMojMPsDhYHnESScUPaqFX_1LOzAJjh5CVeBS0kP8h8By3kVmquhRRqgOZnQg4K8wkpKbu498uLV9TA20MrqL9MkMm2ReVokOGX2sWERZJ9E5yGN-dcY; GC=WuG-OTnKv1wzRv-rsSaWPbO6issFavXdEthRs_ZDEyCK46cy_2XJJnAmTvAW7uUa0lmZ3xN1nelQwxlQy2oIAw; webisession=%7B%22impressionId%22%3A%22c6414237-9541-4fa5-93e7-8f501ccf973b%22%2C%22sessionid%22%3A%22fae7a71a-276e-4ea0-bbcd-fe99ddbfb4df%22%2C%22sessionNumber%22%3A16%7D',
        'Origin': 'https://rewards.bing.com',
        'Referer': 'https://rewards.bing.com/',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 负载数据
    data = {
        'id': 'Gamification_Impression_AMC_Dashboard',
        'hash': '3dd336a029463a1e2d30ea02a5d71d5900d5dd66cc9feacbe4f6a54ca227f0c0',
        'timeZone': '480',
        'activityAmount': '1',
        'dbs': '0',
        'form': '',
        '__RequestVerificationToken': 'CfDJ8JYJKBW24hpHiazIjul8o0kqCw6wMSRTyOfF0Y6yHqs4wbuNaaaMeY7V1YwZBWilRvQTHRflb5J0Zi39_G-0PvsHmRRLRoEO4NZQvwMY6uSAfqFk6rMKnyPjp-pSvHCs3efwKsLsdcvTvLzYm3lWkqQb44n7VhzLIgXF69z8TtKh3yRQ8O9EliBAkFdDRPIUFw'
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data)

    # 输出响应内容
    # print(response)
    response_json = json.loads(response.text)
    # print(f"{response_json['balance']}")
    return response_json['balance']


# 查询今日各个项目得分
def get_today_score():
    # 目标URL
    url = 'https://rewards.bing.com/'

    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Cookie': 'MUID=1403F992615664E622EBEDD6602E6575; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=2DBCD5071A6649D1B23911A9AA0D9F5D&dmnchg=1; ANON=A=86C2E4898087F7B1A49F4FAAFFFFFFFF; SRCHUSR=DOB=20240316&T=1710618863000; BFBUSR=BAWAS=1&BAWFS=1; BFB=AxDuEe_l2G8QBQqwuyxKGntWqPRyAFGZbV84A2w5EnWct83gbDrNRHq-Nwb0VCEz1F0M4dBqSejdYM_DhVRrsMFoa2waHQvY0I-j6GVU8GVCsxd170T1Zn9OIKXXJw9-U6FyZPfFSGIh8NQmF8fPa8hIrm0o-zeOvmG-JvSCoGZYxsHTswn5d1l5hk1SdeJUPJk; OIDI=AxCPo05uYN8mh9-Pl4HhWkT57grxqP_vEcmCIZGBLZ0jZw; MMCASM=ID=D35B11A548F04E1BA86B6289BEF6823B; ANIMIA=FRE=1; MUIDB=1403F992615664E622EBEDD6602E6575; vdp=%7B%22ex%22%3Atrue%2C%22red%22%3Afalse%7D; MicrosoftApplicationsTelemetryDeviceId=075ef574-2d8e-4344-bd20-2d63acc9d385; MicrosoftApplicationsTelemetryFirstLaunchTime=2024-03-23T15:52:58.259Z; MSCCSC=1; MSPTC=QRDvrE7HLtIaxiNi4Xgj9r1ncOMjvfOzEBJFoe7-PpQ; MUIDB=1403F992615664E622EBEDD6602E6575; mapc=rm=0; WLS=C=d4f13ef6c1b0be3a&N=%e6%be%b3%e7%82%af; SRCHS=PC=U531; _Rwho=u=d&ts=2024-05-06; EDGSRCHHPGUSR=CIBV=1.1719.0; _C_Auth=; .AspNetCore.Antiforgery.icPscOZlg04=CfDJ8F79XorNUSlPuQIOpL4R67qcpRw3-qyipDjTheugpKV3flxzz3X-ILYDhQKn_d3RrHeKWmJIZZU6_SG0L_KJmqnuUXhlVih1UdM4acLyI2h1M0L5h-dO-7kd4jlsQavOAK850HIJNOgaQZguoJBsOac; GRNID=269f056e-760d-49d4-b55e-e3fc749158dc; tifacfaatcs=CfDJ8F79XorNUSlPuQIOpL4R67oKceWFn4omtGn31OBgTtYt3eiujlvJjrPWEqDbBR-ixLXBr62NzxekOLkvg952j3tN0FQ7suSEcaKcI5ZMXol4DGhpWMA23UTAYYJ6fCQjRHck1inRH4W_nigRSLXHqF7f5QmBch9AjTUyaCQ7LScXvMgiCATsyusNT55s0emrOZfMxJSvI94GygOQWKbJym1PH9obxTuXU7TYe3grV3Lh62N_fGhtoHzfOlmHCVpBea3OEXCQ8TIeT4Vw--6XoYiuJhVk0IYMvqJYFhfjNHPRwl862FQ67bvXoWvsU4CZ03SPFZ40IXneRtF804d8jW396m0A38HJ8g7lmZg_zd8zoTbQr2wTqKKVrC5r8NLqwDTbnGVsy_3MFLM9cOzUwbRebjn_G9bo-v8yFK0Glg7E6mvGkWab0fsWxFpanhMh5YnvKj6udsHi9HMtu1d9UYiAnDLtkzylZDDdgiz_POgTGHh-v6bmEs3x-ygUIvaE0ey2us87gow8UNK0v3SKS8aYm6vBwjUmMH_dZvchSqUQhfpbvsTCMR7whyK2ZApCT7zwnLZrFp51fccKeazb5lb-VlihZ5WcQKt1n1UWWBcHEaEiiQh-1VqrOhxAuIwUUZmNeUqJMvbPDW6FIyCTS9mouo0A4QSHm5A77rWp3O6nwXCytcBOEHfYOvKxKKXcGCpPMhTHTYUwezfADuUXaCnTX8_eB1lzsMAK_M1IX3tI12phNC1J9p_IqZ07Y1Tq-ZR_Jyj02gZ0ZP6vrK0pWmxiO_lgT-gX4IPkiZkMfGcYevfsrfGH6fVkIoaMI4hz55y4VfyxpEcHvUyczkhws528MkeMJyq7b-5BRWBK7fdy_IEqpc-fTUpG523LLGPFAzaobpGfP4PuIHn3eVVVSk4M6JKyKY9iZoerNeSfQjvrsZoq0aOHEsOTuRn8ZOnqcIGGJxnFV93D8CiQ_vIE5D5wq-8DRBmiknrnZj30fXlC4-gyQem6CtuESWl_xMvaWsKZxDkXLWJs3xZf0jfD8YTTZB6ntNpnlLXMCyCRwXs1qI83GGQ253qWJQrDCohkgGSHtH3sNurO_jfsJfTz1rdknkyi5CDdWbs18Gok7GGBaHaExn-Z84j5dsYnfOjIaKqGP_nbrpsvZaRlWIMmoT718UR0mwRsRgPdTV8PMJVydb1ccLNYYos-KVRpYDM_1akWAdkQ0TQsSQkRgsxn0_KwtcME-ezpF5GgouKEgtNzhQzoAz3o2hmhOftnnw7NF1dkiM2lvC7xXcSPMF_JVFacjlq8dOcxkg_HloagHYODpE_Fq19SLxPc4vD-koaZPnJLdr1xIqB-K2Fcj6ztQryP9GTGgpK_fSE2N3GOvNXxLVt1haAiC7IuQJHkHTx8FtNSW2-LJPs3Y-DavA78gaEdO1BWkur8IM6vwwun5bqmAdyCABEFQXKMjVr1XC-92NDtdGsgzKws0mzQ1fglQ8v-oW1SSUN04z3TQLk98P-ziEQXwG4kuTH0tzMuSA9f16tvG7IlJk2T5CT10jXJ7rEBcSgjGWpivzpFg1sYjW8Dl9VGZy3ANf_PTPSJI2ervAOhuaXAJURNt84mz1NhFa_v3S8eSdhxFVbPSUgrq8xik28C6o7pyK13s8pDcrGsvGZa-5PUmzaLXp-m8JXiadF4crgDgjHewkqnpcpSWwSr8SzHEb4YsKLQZovxfZP_bLjF8n4I4ZwW6ssSEFR1QB6ZP1Mn52eYoQxjfRurusfQ09S-N1PwicwsiJm7aMu5Y0LDXzz7KZ19L0cHi54gVXjPumEncnxHiJOwNt__X4_u49MfDGiySEkQ1lU102FzRlKB0TshlRiJL2CF8LlCuyMy4heQpYh9ZAP6H1DTmvHRRtknidAcbCM6eCyIQzInB6lXwteYs3UOkXYqc0Wi5r7lF5t8ErFfG68BTJ-qzwC8c6yrD3ntHpqz7sNiVW1OmZJUQH_zHUC4MTUXQWYSP5lDyuBi51TX3DnGi8RzhFL1kA8a_5ZKIpYutClJOz-sSE2IrzMoOlMVPThc4ZGqNduxaKYkBeekGdNeNCLYNxlDzqCj3WBneT5RhWGHs7oMuMuE4G5RDZfmmRQ0YYfnyt2v97KcmD1iyC2dFwZZMwraCKrkHpAmv6wZQ6tiVd_kw9jnacZqpXpOZOmDtBUB3pE_J08cZfz_ZOMqyFffzMxLV9Uo6_ZMwq-8aBmMJS-jJoBDEqPtEnqZYTGAf7SR53W8dB2RnRutgB_2GQLl6uux5B_PQhAhbDkjI6l29NOjxcFYQ7QQBuAsNZjK8S2groT_p7Fj2hBSsPHF9xTTSCfFm2vvWoZFYVh52wFrc0oL34gnhJjzDjwHTjrIPpWFdJi6xutQUfqa8mKm-7caiFDCJroWJSR_ffN5h7rcjmZCHAjuxaLtoeki_mMnIGBZ0hpI--rt5c-OhRZAqo0bZsHq6rA7ExrKP3N_pAWSh8hgnyLMInvdGLT5DhdGpnzbVgbckVBlIKrL6dy0gNYTlAH1BeYMtWCqijHL4vlbS9Cby3I21K4teCe_OSrxyj_9Hgu3_FV4Pb7nW-iREwvy3wHkUy7_PR_9ie-P2muYHsBbvJMrHtCLv3g-h_cxg-8QQAOM-Ij-mOt1ND-OnwvCnixB5-ZNDsXsUw3HCKkYDa2HlMpU4PsWohFkJjuMMCJz7jiXg4rm6o_ORQ5FY4klCsK4wgEetJ56o75zmasKKQSTaH0t3n3WZFYqyQATnavTEdR-soykOl0ZktdFuyEUYy9W--mUSsmr4FDjvtb4WoAo-bImTh1lhLaf5HE8_VC5FXTERf5W9uNcpIb7OTEr40dHTn9PhnV7_VYcHK5YnCBJEfVRRIBGRQygwIYOpY6y9H4HND-xdsDvMI4YCwxoGzNsExHKxzg8dfPHKx-ue4H8vynewh4FKiUQQBaCscFb43pb-U3lcqBtmyM_6Wot9uyP90zv0KW2rr_ACK_ZmeXZFWaQ8SkrbZxfDQNeZyK4oKf7Uwkjd7eI4U8l5hTNIqfsO11wv2Hnecznyz8eVbdz9P-mPyvD3wH7fikq2pJokOiwDS4IsA3cv_gyy-Lvn0tFfoRRlfM6M8UG5p9O3MALQJEDc2VLblFH5DDtAQJ5svTjIt9-FNhhWxKLWCVd6bX0w1aZwF0u7iHDuS3pkYMTHUWOBWXtcHTTfJSYVRuj7b7fINA0LpB4pSY6Qh6FUqvEFx9TntRTVf7SGl4wrkus4pkO8NiPEeXGX5z7HaFogs_9jU60FpidlNGuOqXvwTom4443XFDM_GTZLez4g-K87TDRf2QK0TK7ni4a7V8QLAShOzF6L76wuCh1vgGfm9U2AGfcansHqNI17fhIsbZvGiiVOUJJ5n9I5AjW9iDihkpj85ap-MQVyv1r-duM5mlV1T2gHYXQ3iltt1VLlrTAx6p6QmBFQi6QRoaOA4h6dS5ISn0yai-7lDm0lTmGx3NUTmm7xXaMP_B3PwR43quTtbSy6s6SrJ48HTSP9R0G4TyN5k3BC7PRc_nO_B4UGu569pEHz1L437OqPZ2WU0IEDt__aemiljBXYH59dSIT6zdJbVcFXwn3n5HB35zA9eWmV87afQ4Gi4Zv3i9MxfAm94LXjO35KiJXGK47bJr2H8WedlF0MheeMLoSfgiZstvEF7rjW2_Si4B269CbehD7pUMtXIRqBzdglNuxvTNBpxMzS4PBNXgqKruVeCz28oKQ; SnrOvr=X=rebateson; _EDGE_S=SID=2917DAE1B6B9686C3F84CE96B79769CE&mkt=EN-US&ui=zh-cn; MSCC=cid=saj132lqys7meaj2ho8bsro8-c1=2-c2=2-c3=2; BFPRResults=FirstPageUrls=A362573359DDE14CAD37767E64103398%2C3B85F5930A4AFC329DE7C4EB4956D9FB%2CAAE5EEABB86B766B9B7AA0FE7B60DA75%2CAB20F4FDB1BAFF3EF816812D824EC0A3%2CF2D53E5113CBD54C9EB7B45F0B662153%2C53F71A4F75C9037424108C3FE42C1F1D%2C4583F56BA0F296043C3B47A3C5726BE8%2CEAB388DEB6612D60549C8FABB07AD465%2C45A9665DC32D2068BCB953A8D6285595%2C58F8B78CA6E2C4BBE4A0ACAAAF13ADC5&FPIG=9C58268C710D4F4CB626ECE316D06108; OID=gxDc5N5DQPKsHWzWu1OLpyldGuVBNh53s5byMbjb9U9HZA; _SS=SID=2917DAE1B6B9686C3F84CE96B79769CE&PC=U531&R=4687&RB=4687&GB=0&RG=89570&RP=4684&RA=-&BTOID=-&BTQID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-&BTSTKey=-&OCID=ML2BFU; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&HV=1715320307&BRW=HTP&BRH=M&CW=869&CH=966&SCW=1164&SCH=2255&DPR=1.0&UTC=480&DM=0&EXLTT=31&CIBV=1.1719.0&PRVCW=869&PRVCH=966&BZA=0&IG=F50DEA4D65484AC79E2CBDE3027D4D06; USRLOC=HS=1&ELOC=LAT=30.4775333404541|LON=114.29781341552734|N=%E6%B4%AA%E5%B1%B1%E5%8C%BA%EF%BC%8C%E6%B9%96%E5%8C%97%E7%9C%81|ELT=4|&DLOC=LAT=30.4805|LON=114.3049|A=10458|N=%e6%ad%a6%e6%b1%89%e5%b8%82%e6%b4%aa%e5%b1%b1%e5%8c%ba|C=|S=|TS=240510055146|ETS=240510060146|&BID=MjQwNTA5MjMxMDE3Xzc5MWIxNGE1MGQ0NTE2ZWEzODY1OGI2MTFlZjQ2Y2E0NmVjMjZlNThkYWY0NGM2MTI5NTMwYjYwNjljZDllNTc=; ipv6=hit=1715323909122; _clck=15qwo4i%7C2%7Cfln%7C1%7C1544; SNRHOP=I=&TS=; _RwBf=r=1&mta=0&rc=4687&rb=4687&gb=0&rg=89570&pc=4684&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=38&l=2024-05-09T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-05-07T18:36:07.4079092-07:00&rwflt=2024-05-06T21:38:49.2395147-07:00&o=16&p=WINDOWSBARACQ201902&c=M5001O&t=4878&s=2022-08-16T01:47:02.9424911+00:00&ts=2024-05-10T05:51:43.3489322+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&e=tK3Ul9rmy4R0_mIa8RCAMeP1F8nRy7fV3aUMdPo2-wwFnYMrLnAl2zhVSYvPpN7S5_LQgYZLX2tHwXeepqoyrg&A=86C2E4898087F7B1A49F4FAAFFFFFFFF&cpt=0; _U=1W49JEX3A60og_CMp_Prb1xXJkBqOJW7OyQezwiRVMgpSIYuABgFyiQ5UVQQaAAXozQ_j6eH7nKLtZlNdju83z05Bauhs16qnPnF6zlG-1_2rOD564dUbz0GnMojMPsDhYHnESScUPaqFX_1LOzAJjh5CVeBS0kP8h8By3kVmquhRRqgOZnQg4K8wkpKbu498uLV9TA20MrqL9MkMm2ReVokOGX2sWERZJ9E5yGN-dcY; _uetsid=9943bfe00e9111efa13881733cb131b4; _uetvid=0d273760e9bc11ee81e12d9fa88bc004; _C_ETH=1; GC=WuG-OTnKv1wzRv-rsSaWPbO6issFavXdEthRs_ZDEyD-0nWWwNsYggzPPyqqXXQROKUM-LEDn8yhHV2TArV2HA; webisession=%7B%22impressionId%22%3A%22e0afc7e6-dc9f-4ed9-a3da-db0156293971%22%2C%22sessionid%22%3A%22fae7a71a-276e-4ea0-bbcd-fe99ddbfb4df%22%2C%22sessionNumber%22%3A37%7D',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }

    # 发送GET请求
    response = requests.get(url, headers=headers)
    # response_json = json.loads(requests.get(url, headers=headers).text)

    # 输出响应内容
    # print(response.text)

    import re

    '''
        返回值：字典（键值对）
        90：x
        60：y
        181:z
    '''

    def extract_progress_values(text):
        # 正则表达式匹配 "pointProgressMax" 和 "pointProgress"
        pattern = r'"pointProgressMax":(\d+),"pointProgress":(\d+)'
        matches = [match for match in re.finditer(pattern, text)]
        # 使用 finditer 遍历所有匹配项,
        ## 第二项是PC端搜索分数:90
        ## 第三项是Mobil端搜索分数:60
        ## 第四项是卡片点击搜索分数:31
        ## 第五项是今日可得/已得分数:181
        # for match in re.finditer(pattern, text):
        #     pointProgressMax = match.group(1)
        #     pointProgress = match.group(2)
        #     print(f"pointProgressMax: {pointProgressMax}, pointProgress: {pointProgress}")
        if len(matches) >= 5:
            return (
                {matches[1].group(1): matches[1].group(2),
                 matches[2].group(1): matches[2].group(2),
                 matches[3].group(1): matches[3].group(2),
                 matches[4].group(1): matches[4].group(2)}
            )
        else:
            return None

    today_score = 0
    result = extract_progress_values(response.text)
    if result:
        try:
            today_score = result['181']
        except:
            today_score = -1
    return today_score, result


# PC端的模拟搜索请求
def PC_search_task(search_text='hello'):
    # 定义URL和参数
    url = 'https://cn.bing.com/search'
    params = {
        'q': search_text,
        'cvid': '33a413af1215400bb94c5addecb353f2',
        'gs_lcrp': 'EgZjaHJvbWUqBggDEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCTIwODU5ajBqMagCALACAA',
        'FORM': 'ANAB01',
        'PC': 'U531'
    }

    # 定义请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Cookie': 'MUID=1403F992615664E622EBEDD6602E6575; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=2DBCD5071A6649D1B23911A9AA0D9F5D&dmnchg=1; ANON=A=86C2E4898087F7B1A49F4FAAFFFFFFFF; MUIDB=1403F992615664E622EBEDD6602E6575; SRCHUSR=DOB=20240316&T=1710618863000; BFBUSR=BAWAS=1&BAWFS=1; BFB=AxDuEe_l2G8QBQqwuyxKGntWqPRyAFGZbV84A2w5EnWct83gbDrNRHq-Nwb0VCEz1F0M4dBqSejdYM_DhVRrsMFoa2waHQvY0I-j6GVU8GVCsxd170T1Zn9OIKXXJw9-U6FyZPfFSGIh8NQmF8fPa8hIrm0o-zeOvmG-JvSCoGZYxsHTswn5d1l5hk1SdeJUPJk; OIDI=AxCPo05uYN8mh9-Pl4HhWkT57grxqP_vEcmCIZGBLZ0jZw; MMCASM=ID=D35B11A548F04E1BA86B6289BEF6823B; ANIMIA=FRE=1; MSCCSC=1; MSPTC=QRDvrE7HLtIaxiNi4Xgj9r1ncOMjvfOzEBJFoe7-PpQ; MUIDB=1403F992615664E622EBEDD6602E6575; mapc=rm=0; _clck=15qwo4i%7C2%7Cfld%7C1%7C1544; WLS=C=d4f13ef6c1b0be3a&N=%e6%be%b3%e7%82%af; SRCHS=PC=U531; _Rwho=u=d&ts=2024-05-06; EDGSRCHHPGUSR=CIBV=1.1719.0; _uetvid=0d273760e9bc11ee81e12d9fa88bc004; SnrOvr=X=rebateson; _EDGE_S=SID=2917DAE1B6B9686C3F84CE96B79769CE&mkt=EN-US&ui=zh-cn; MSCC=cid=saj132lqys7meaj2ho8bsro8-c1=2-c2=2-c3=2; BFPRResults=FirstPageUrls=A362573359DDE14CAD37767E64103398%2C3B85F5930A4AFC329DE7C4EB4956D9FB%2CAAE5EEABB86B766B9B7AA0FE7B60DA75%2CAB20F4FDB1BAFF3EF816812D824EC0A3%2CF2D53E5113CBD54C9EB7B45F0B662153%2C53F71A4F75C9037424108C3FE42C1F1D%2C4583F56BA0F296043C3B47A3C5726BE8%2CEAB388DEB6612D60549C8FABB07AD465%2C45A9665DC32D2068BCB953A8D6285595%2C58F8B78CA6E2C4BBE4A0ACAAAF13ADC5&FPIG=9C58268C710D4F4CB626ECE316D06108; OID=gxDc5N5DQPKsHWzWu1OLpyldGuVBNh53s5byMbjb9U9HZA; SNRHOP=I=&TS=; GC=WuG-OTnKv1wzRv-rsSaWPbO6issFavXdEthRs_ZDEyBjuQWkLDQTX6hv1pKSVgc07hJduyJGURcfMEe0euBnJw; _SS=SID=2917DAE1B6B9686C3F84CE96B79769CE&PC=U531&R=4684&RB=4684&GB=0&RG=89570&RP=4681&RA=-&BTOID=-&BTQID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-&BTSTKey=-&OCID=ML2BFU; dsc=order=BingPages; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&HV=1715316353&BRW=HTP&BRH=M&CW=869&CH=966&SCW=1164&SCH=3926&DPR=1.0&UTC=480&DM=0&EXLTT=31&CIBV=1.1719.0&PRVCW=869&PRVCH=966&BZA=0&IG=F50DEA4D65484AC79E2CBDE3027D4D06; USRLOC=HS=1&ELOC=LAT=30.471839904785156|LON=114.29669189453125|N=%E6%B4%AA%E5%B1%B1%E5%8C%BA%EF%BC%8C%E6%B9%96%E5%8C%97%E7%9C%81|ELT=4|&DLOC=LAT=30.4805|LON=114.3049|A=10458|N=%e6%ad%a6%e6%b1%89%e5%b8%82%e6%b4%aa%e5%b1%b1%e5%8c%ba|C=|S=|TS=240510044552|ETS=240510045552|&BID=MjQwNTA5MjMxMDE3Xzc5MWIxNGE1MGQ0NTE2ZWEzODY1OGI2MTFlZjQ2Y2E0NmVjMjZlNThkYWY0NGM2MTI5NTMwYjYwNjljZDllNTc=; ipv6=hit=1715319954410; _RwBf=r=1&mta=0&rc=4684&rb=4684&gb=0&rg=89570&pc=4681&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=37&l=2024-05-09T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-05-07T18:36:07.4079092-07:00&rwflt=2024-05-06T21:38:49.2395147-07:00&o=16&p=WINDOWSBARACQ201902&c=M5001O&t=4878&s=2022-08-16T01:47:02.9424911+00:00&ts=2024-05-10T04:45:48.3251034+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&e=tK3Ul9rmy4R0_mIa8RCAMeP1F8nRy7fV3aUMdPo2-wwFnYMrLnAl2zhVSYvPpN7S5_LQgYZLX2tHwXeepqoyrg&A=86C2E4898087F7B1A49F4FAAFFFFFFFF&cpt=0; _U=1_uDD0G64NuecI69b0SJfsGSMhMfEUmQ_WRIiTruZmQdgmbkp5eNWS7e9vbMxNh8uk3TgYp3ZisW-bImkzWfPhlHmVOkvAya7OiEi8c3g5GwaM7rZH1fr8_K91dX0Y70YtIWefzEuyPoetpjzFOJLKPU80wzTycBOoDJ1IK07tIi_eelDygJo2_R5p8X_FTS33mlvKCh-1ZOurkyEiZOomn9x8_BqO7MpfbHfJLBgIKs',
        'Pragma': 'no-cache',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)
    return response.status_code
    # 输出响应内容
    # print(response.status_code)


# Mobile的模拟搜索请求
def Android_search_task(search_text='hello'):
    # 定义请求头和Cookie
    headers = {
        'Host': 'cn.bing.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-full-version': '117.0.2045.53',
        'sec-ch-ua-arch': '',
        'sec-ch-ua-platform': 'Android',
        'sec-ch-ua-platform-version': '13.0.0',
        'sec-ch-ua-model': 'PDSM00',
        'sec-ch-ua-bitness': '',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="117.0.2045.53", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.132"',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36 EdgA/117.0.2045.53',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'X-Edge-Shopping-Flag': '1',
        'Sec-MS-GEC': 'E0A7F60AB5513D464E005DD0CC260B51BCB1556E9CAB9883CDBC7569C702031D',
        'Sec-MS-GEC-Version': '1-117.0.2045.53',
        'X-Client-Data': 'eyIxIjoiMiIsIjEwIjoiXCI0Sk5yWFlVbklBVHNVVElpK1pxS29icm5GcExVKzgvMVBoYnZKNDZLTU84PVwiIiwiMiI6IjEiLCIzIjoiMSIsIjQiOiI1MzE2NjY1MzEyMTgxNzA4Mj6yIiwiNSI6IlwiUnhZSGhFd2xnRmZacHVZbVZjVlI1NXpHQzJFWWzVjVlRDNjh3NFp4QWZHTVxHSjFzWlNscFwibkk4az1cIiIsIjYiOiJzdGFibGUiLCI3IjoiMzE1MjUwNTk5NTI2NiIsIjkiOiIifQ==',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    cookies = {
        'SRCHD': 'AF=LBT003',
        'SRCHUID': 'V=2&GUID=7E6A9312CFB544B397AB141CF420FF49&dmnchg=1',
        'PPLState': '1',
        '_tarLang': 'default=zh-Hans',
        '_TTSS_OUT': 'hist=WyJ6aC1IYW5zIl0=',
        '_UR': 'QS=0&TQS=0',
        'SnrOvr': 'X=rebateson',
        'MUID': '1811E610FEDD6F850434F4FDFF1D6E75',
        '_EDGE_V': '1',
        'MUIDB': '1811E610FEDD6F850434F4FDFF1D6E75',
        'MMCASM': 'ID=37CE5242E7304A1A814B966F4933E77F',
        '_TTSS_IN': 'hist=WyJlbiIsImphIiwiYXV0by1kZXRlY3QiXQ==&isADRU=0',
        'imgv': 'gt=1',
        'MSCC': 'cid=dzmko1ncac3iyxx9souuvgu9-c1=2-c2=2-c3=2',
        'ANON': 'A=86C2E4898087F7B1A49F4FAAFFFFFFFF&E=1cbd&W=1',
        'NAP': 'V=1.9&E=1c4f&C=PJakZJcBocGpjbrhI_iSv8NZKC_80Zc5ttOrEvK5KThykRPuNHlsnA&W=1',
        'KievRPSSecAuth': 'FABSBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACAuUOdSuxlgMEARX+kkqvNsJe04kYbY/UrwuNRNwC9tG4e2tkNfT4Hc8NSOdBT/jc+4lOUJwR5vpw5Ol1rsxYcwdIxfeI79uBVgXjE8fta99/SSg1XHDIOEclWVvoA9nUyZBBLdXpRfDAvbMVwkrKcgZemF0WtFQMoTRJeL7YwzJUwTZLpWQ+HUzxDhYI4ENHvWwYDIEXGvb5EJes5a/mDJxTFaDatnlKqn/c5MPFt68QyLP34K85ZKYLzwfV6B/2J6hGUTde/fkBSXKT5/DIGvduqcRLmkab9qH/6CB+/oR0ffkNmiviuQE00Oc0kyOboGefReOu/NRDMSmxcYUVStPP5G9HQ33HAu34F03paiwu0mZHKBHx8SOouMH3rmo7wWk7zfdJXDmOztjEjlSpdmwZC9tn/ydpyhXOBAkhRE92qHgHfbGJWjJCmuhw6ah7MA5ZJdz2zXfhXgxTjSU8iQaYIP+1PP8BdX9majAA7TVTr9U2acudpRt4x4taw/rSG7bATIsswuegjlylY0ZEQChU7h6i1bNUMHomHaAMiTyaccdIe8ccrc7fX0akQq+caFZG3Mv3E4ICXTZ+fiIkpcply2iAZAEO0pRoW3KsiZjjDc7RQTaRk6nECVb8l52J/eqtTbVEVIrCxb6IP0u7RS8SmYrqqWmcwQgin6eYJ5nM2KvlqWWr+QLEl6fUBDLtlL27BEDu7dtIT0syCVxWzi61adfHLLKeYEoBtmv4GQa+UtDtWYKDoGiVJYJiNvlYdMmYjpclJBWJEkvmpd1iFnLY/1kgSuYJBHrY+ffvqDX+/oR0ffkNmiviuQE00Oc0kyOboGefReOu/NRDMSmxcYUVStPP5G9HQ33HAu34F03paiwu0mZHKBHx8SOouMH3rmo7wWk7zfdJXDmOztjEjlSpdmwZC9tn/ydpyhXOBAkhRE92qHgHfbGJWjJCmuhw6ah7MA5ZJdz2zXfhXgxTjSU8iQaYIP+1PP8BdX9majAA7TVTr9U2acudpRt4x4taw/rSG7bATIsswuegjlylY0ZEQChU7h6i1bNUMHomHaAMiTyaccdIe8ccrc7fX0akQq+caFZG3Mv3E4ICXTZ+fiIkpcply2iAZAEO0pRoW3KsiZjjDc7RQTaRk6nECVb8l52J/eqtTbVEVIrCxb6IP0u7RS8SmYrqqWmcwQgin6eYJ5nM2KvlqWWr+QLEl6fUBDLtlL27BEDu7dtIT0syCVxWzi61adfHLLKeYEoBtmv4GQa+UtDtWYKDoGiVJYJiNvlYdMmYjpclJBWJEkvmpd1iFnLY/1kgSuYJBHrY+ffvqDX+/oQTeulGzFtgmuBaQRyZZ2Si3sTFpIhj4dnRf9kYqtGKKJrhHiMx6mqPSlPJKtPO9N4aUZHHGJkEBiSa6qPAYosD1pOVdXT5sJxZ86M5wWCg9w/i/j/Gqu1Fp3KbU8UnT/RpsTfRWblNtuSePZtpm+TmpqzQ1xgmbsCtz2k5t0xf3Jy/TNUIbT6hppZ1b6SYOCRddkhlMjydm/6Ms6aL/ms/nTlLfmKEKyxyNLS+T16sgt3M6l+c3oJzDyCPdU+W1OIoyemwr7Ps42+k2z/wCo3XZQj7Y2smTB7U+wpKWTTTpvkugtKmMh4VoS2+4wRjXy6oltNv6xSss+yoMo9xT0IftNiQiPSduWwr7/oFC4fOFqU6haiEMeNduWR8mjiFFcmJTaW3duP6IUNFZpsVwRZazdHOkAEqd3fpumq3eRaRe31I1zJoVdyzfs30wqoEF/hwyP/0X7U6PomOD+SkWF+BRs9/s3DcOjqH/PEfvNxQePOfjl0M9x7bp/P/4CKMB1NNYxEw5diQ6a71lGUPIO0V5cU8JSojGJUxy7WayPUsBzEjEgw/WFng6R7B4LtVgRl5GfMZowHJRQAhMYudd0IAJ2dRwbWdPeLdLvrlRw=',
        'ANIMIA': 'FRE=1',
        '_clck': '1or1dq1|2|ffj|1|1333',
        '_uetvid': '84e90d9040ff11ee9ea973192ca448c7',
        '_HPVN': 'CS=eyJQbiI6eyJDbiI6MywiU3qiOjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MywiU3qiOjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MywiU3qiOjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMC0wMFowMDowMFoiLCJJb3RkIjowLCJHd2IiOjowLCJEdmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjowLCJltcCI6MTh9',
        '_RwBf': 'r=1&mta=0&rc=6704&rb=6704&gb=0&rg=0&pc=6701&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2023-10-03T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=WINDOWSBARACQ201902&c=M5001O&t=4878&s=2022-08-16T01:47:02.9424911+00:00&ts=2023-10-03T14:30:00.3430688+00:00&rwred=0&wls=2&lka=0',
        '_U': '1bgFSDgUz0BooV9lsJfM4W_EtvI2PIcFX3LubDV8e2B7oIB1lP1_S-nH8KfGrLVuuPwf7htFKZ-t7XAJgnV8KvUR1YdqNjCNI6JKeGMwIZI-_dPK9-nf8UmBzh459QOraUSTHbvKDctpmS99zE8oSHH44ArSLsDHOR8hdrtv37Lka19zRqtylJNTucHhZNn_NZjJwyMsMw5Cv-4-fciD8d8JT4W-JMrpdH3gvd-0KOOg',
        'SRCHUSR': 'DOB=20220310&T=1697275775000&POEX=W',
        'SRCHHPGUSR': 'SRCHLANG=zh-Hans&DM=1&CW=360&CH=645&SW=360&SH=800&DPR=3&UTC=480&PR=3&OR=0&HV=1697275778&RL=0&BRW=MM&BRH=MM&PV=13.0.0&PRVCW=360&PRVCH=645&SCW=360&SCH=645&WTS=63829186660&HBOPEN=2&IG=BFC5DF2A7B3D46D1A09F09390CB670BA&THEMEDMUP=0&SHOWFLG=0&DMOPTOUTTS=1692281509373&DMOPTOUTCT=1&THEME=0',
        'USRLOC': 'HS=1&ELOC=LAT=30.482038497924805|LON=114.3089370727539|N=%E6%B4%AA%E5%B1%B1%E5%8C%BA%EF%BC%8C%E6%B9%96%E5%8C%97%E7%9C%81|ELT=4|&BLOCK=TS=231014092938',
    }

    # 构建请求URL
    url = f'https://cn.bing.com/search?q={search_text}&setmkt=zh-CN&PC=EMMX01&form=LWS002&scope=web'

    # 发送GET请求
    response = requests.get(url, headers=headers, cookies=cookies)

    # # 检查响应
    # if response.status_code != 200:
    #     print(f'请求失败{response.status_code}')
    #     # print('响应状态码:', response.status_code)
    return response.status_code


def random_chinese_GBK2312(n=1):
    strGB = ""
    while n > 0:
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        n -= 1
        strGB += bytes.fromhex(val).decode('gb2312')
    return strGB


def main():
    count = 0
    while count < 30:
        today_all, today_item = get_today_score()
        count += 1
        if int(today_item['90']) < 90:
            # print(PC_search_task())
            if PC_search_task(random_chinese_GBK2312(random.randint(5, 12))) == 200:
                print("完成一次PC搜索。")
        else:
            break
        time.sleep(random.randint(5, 12))
    count = 0
    while count < 20:
        today_all, today_item = get_today_score()
        count += 1
        if int(today_item['60']) < 60:
            # print(PC_search_task())
            if Android_search_task(random_chinese_GBK2312(random.randint(5, 12))) == 200:
                print("完成一次mobile搜索。")
        else:
            break
        time.sleep(random.randint(5, 12))
    today_all, today_item = get_today_score()
    Total_scores = get_total_scores()
    return Total_scores, today_all
    # print(f"总积分：{get_total_scores()}\n今日总积分：{today_all}\n")


if __name__ == "__main__":

    Total_scores, today_all = main()
    WxPusher_send_message("Microsoft",f"总积分：{Total_scores}\n今日总积分：{today_all}\n")
