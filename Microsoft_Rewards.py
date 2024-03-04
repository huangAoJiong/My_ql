# -*- coding:utf-8 -*-
import random
import time
from sendNotify import send
cookie = "SRCHD=AF=LBT003; SRCHUID=V=2&GUID=7E6A9312CFB544B397AB141CF420FF49&dmnchg=1; PPLState=1; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; _UR=QS=0&TQS=0; SnrOvr=X=rebateson; MUID=1811E610FEDD6F850434F4FDFF1D6E75; _EDGE_V=1; MUIDB=1811E610FEDD6F850434F4FDFF1D6E75; MMCASM=ID=37CE5242E7304A1A814B966F4933E77F; _TTSS_IN=hist=WyJlbiIsImphIiwiYXV0by1kZXRlY3QiXQ==&isADRU=0; imgv=gt=1; MSCC=cid=dzmko1ncac3iyxx9souuvgu9-c1=2-c2=2-c3=2; ANON=A=86C2E4898087F7B1A49F4FAAFFFFFFFF&E=1cbd&W=1; NAP=V=1.9&E=1c4f&C=PJakZJcBocGpjbrhI_iSv8NZKC_80Zc5ttOrEvK5KThykRPuNHlsnA&W=1; KievRPSSecAuth=FABSBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACAuUOdSuxlgMEARX+kkqvNsJe04kYbY/UrwuNRNwC9tG4e2tkNfT4Hc8NSOdBT/jc+4lOUJwR5vpw5Ol1rsxYcwdIxfeI79uBVgXjE8fta99/SSg1XHDIOEclWVvoA9nUyZBBLdXpRfDAvbMVwkrKcgZemF0WtFQMoTRJeL7YwzJUwTZLpWQ+HUzxDhYI4ENHvWwYDIEXGvb5EJes5a/mDJxTFaDatnlKqn/c5MPFt68QyLP34K85ZKYLzwfV6B/2J6hGUTde/fkBSXKT5/DIGvduqcRLmkab9qH/6CB+/oR0ffkNmiviuQE00Oc0kyOboGefReOu/NRDMSmxcYUVStPP5G9HQ33HAu34F03paiwu0mZHKBHx8SOouMH3rmo7wWk7zfdJXDmOztjEjlSpdmwZC9tn/ydpyhXOBAkhRE92qHgHfbGJWjJCmuhw6ah7MA5ZJdz2zXfhXgxTjSU8iQaYIP+1PP8BdX9majAA7TVTr9U2acudpRt4x4taw/rSG7bATIsswuegjlylY0ZEQChU7h6i1bNUMHomHaAMiTyaccdIe8ccrc7fX0akQq+caFZG3Mv3E4ICXTZ+fiIkpcply2iAZAEO0pRoW3KsiZjjDc7RQTaRk6nECVb8l52J/eqtTbVEVIrCxb6IP0u7RS8SmYrqqWmcwQgin6eYJ5nM2KvlqWWr+QLEl6fUBDLtlL27BEDu7dtIT0syCVxWzi61adfHLLKeYEoBtmv4GQa+UtDtWYKDoGiVJYJiNvlYdMmYjpclJBWJEkvmpd1iFnLY/1kgSuYJBHrY+ffvqDX+/oQTeulGzFtgmuBaQRyZZ2Si3sTFpIhj4dnRf9kYqtGKKJrhHiMx6mqPSlPJKtPO9N4aUZHHGJkEBiSa6qPAYosD1pOVdXT5sJxZ86M5wWCg9w/i/j/Gqu1Fp3KbU8UnT/RpsTfRWblNtuSePZtpm+TmpqzQ1xgmbsCtz2k5t0xf3Jy/TNUIbT6hppZ1b6SYOCRddkhlMjydm/6Ms6aL/ms/nTlLfmKEKyxyNLS+T16sgt3M6l+c3oJzDyCPdU+W1OIoyemwr7Ps42+k2z/wCo3XZQj7Y2smTB7U+wpKWTTTpvkugtKmMh4VoS2+4wRjXy6oltNv6xSss+yoMo9xT0IftNiQiPSduWwr7/oFC4fOFqU6haiEMeNduWR8mjiFFcmJTaW3duP6IUNFZpsVwRZazdHOkAEqd3fpumq3eRaRe31I1zJoVdyzfs30wqoEF/hwyP/0X7U6PomOD+SkWF+BRs9/s3DcOjqH/PEfvNxQePOfjl0M9x7bp/P/4CKMB1NNYxEw5diQ6a71lGUPIO0V5cU8JSojGJUxy7WayPUsBzEjEgw/WFng6R7B4LtVgRl5GfMZowHJRQAhMYudd0IAJ2dRwbWdPeLdLvrlRw=; ANIMIA=FRE=1; _clck=1or1dq1|2|ffj|1|1333; _uetvid=84e90d9040ff11ee9ea973192ca448c7; _HPVN=CS=eyJQbiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMC0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTh9; _RwBf=r=1&mta=0&rc=6704&rb=6704&gb=0&rg=0&pc=6701&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2023-10-03T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=WINDOWSBARACQ201902&c=M5001O&t=4878&s=2022-08-16T01:47:02.9424911+00:00&ts=2023-10-03T14:30:00.3430688+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&e=tK3Ul9rmy4R0_mIa8RCAMeP1F8nRy7fV3aUMdPo2-wwFnYMrLnAl2zhVSYvPpN7S5_LQgYZLX2tHwXeepqoyrg&A=86C2E4898087F7B1A49F4FAAFFFFFFFF&wlb=0; SRCHUSR=DOB=20220310&T=1697018614000&POEX=W; USRLOC=HS=1&ELOC=LAT=30.49041748046875|LON=114.30842590332031|N=%E6%B4%AA%E5%B1%B1%E5%8C%BA%EF%BC%8C%E6%B9%96%E5%8C%97%E7%9C%81|ELT=0|&BLOCK=TS=231011100404; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&CW=360&CH=645&SW=360&SH=800&DPR=3&UTC=480&PR=3&OR=0&HV=1697018644&RL=0&BRW=MM&BRH=MM&PV=13.0.0&PRVCW=360&PRVCH=645&SCW=360&SCH=645&WTS=63829186660&HBOPEN=2&IG=BFC5DF2A7B3D46D1A09F09390CB670BA&THEMEDMUP=0&SHOWFLG=0&DMOPTOUTTS=1692281509373&DMOPTOUTCT=1&THEME=0; _EDGE_S=SID=32F86BDAA87F6F0029967870A9EE6EDE; WLS=C=d4f13ef6c1b0be3a&N=%e6%be%b3%e7%82%af; _U=1bgFSDgUz0BooV9lsJfM4W_EtvI2PIcFX3LubDV8e2B7oIB1lP1_S-nH8KfGrLVuuPwf7htFKZ-t7XAJgnV8KvUR1YdqNjCNI6JKeGMwIZI-_dPK9-nf8UmBzh459QOraUSTHbvKDctpmS99zE8oSHH44ArSLsDHOR8hdrtv37Lka19zRqtylJNTucHhZNn_NZjJwyMsMw5Cv-4-fciD8d8JT4W-JMrpdH3gvd-0KOOg; _SS=SID=32F86BDAA87F6F0029967870A9EE6EDE&PC=EMMX01; SRCHS=PC=EMMX01"
import requests
import requests
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

# 定义要搜索的文本
search_text = "hello文本"


def android_get_url(search_text):
    # 构建请求URL
    url = f'https://cn.bing.com/search?q={search_text}&setmkt=zh-CN&PC=EMMX01&form=LWS002&scope=web'

    try:
        # 发送GET请求
        response = requests.get(url, headers=headers, cookies=cookies)

        # 检查响应
        if response.status_code != 200:
            print(f'请求失败{response.status_code}')
            # print('响应状态码:', response.status_code)
    except requests.exceptions.TooManyRedirects as e:
        print("Too many redirects:", e)
# 随机汉字
def random_chinese_char():
    return chr(random.randint(0x4e00, 0x9fa5))

def random_chinese_GBK2312(n=1):
    str = ""
    while n > 0:
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        n -= 1
        str += bytes.fromhex(val).decode('gb2312')
    return str


if __name__ == "__main__":
    print("你好")
    keys = random_chinese_GBK2312(random.randint(5, 12))
    android_get_url(keys)
