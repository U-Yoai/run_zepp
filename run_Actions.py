import requests
import urllib3
from urllib import parse
import os
import random


def runing(phone, password, my_run):
    parse.quote(phone)
    in_url = "https://motion.faithxy.com/motion/api/motion/Xiaomi"

    head_ = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200",
        "Content-Length": "64",
        'Referer': 'https://motion.faithxy.com/'
    }

    js_ = {
        'phone': phone,
        'pwd': password,
        'num': my_run
    }

    urllib3.disable_warnings()
    r = requests.post(url=in_url, headers=head_, data=js_, verify=False)
    parse.unquote(phone)
    code = 200

    if code == r.status_code:
        print(f"成功执行！已跑{my_run}步" + '\n========')
    else:
        print("发送请求失败" + '\n========')


phone = os.environ["PHONE"]
password = os.environ["PASSWORD"]
my_run = os.environ["RUN"]

# my_run = ""
# run_end = ""

try:
    run_end = os.environ["RUN_END"]
except:
    pass
else:
    if run_end not in "":
        my_run = random.uniform(int(my_run), int(run_end))
        print('%.0f' % my_run)

runing(phone, password, my_run)
