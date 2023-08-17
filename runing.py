import requests
import urllib3
from urllib import parse
from getpass import getpass

def runing(phone,password,my_run):
    parse.quote(phone)
    in_url = "https://motion.faithxy.com/motion/api/motion/Xiaomi"

    head_ = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200",
        "Content-Length":"64",
        'Referer': 'https://motion.faithxy.com/'
    }

    js_ = {
        'phone':phone,
        'pwd':password,
        'num':my_run
    }

    urllib3.disable_warnings()
    r = requests.post(url=in_url,headers=head_,data=js_,verify=False)
    parse.unquote(phone)
    code = 200
    
    if code == r.status_code:
        print(f"成功执行！{phone}已跑{my_run}步" + '\n========')
    else:
        print("发送请求失败" + '\n========')

try:
    phone = input("请输入账号（邮箱或手机号）：")
    password = getpass("请输入密码：")
    my_run = input("请输入要跑的步数（默认20000步）：")
    if my_run == "":
       my_run = 20000
except:
    print("发生未知错误，请重新运行程序")
    exit()
else:
    runing(phone,password,my_run)
finally:
    print("感谢使用，程序运行结束")