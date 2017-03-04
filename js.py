import requests
import re
import time
print("欢迎使用军事理论挂机工具，本工具一次使用最多需要十分钟，可以增加约十几小时挂机时长，可能随网络状况不同而略有出入。")
username=input("请输入一卡通账号：")
pwd=input("请输入一卡通密码：")

postData={'returnUrl':'/PageView/Index/2','M_UserName':username,'M_Password':pwd}

s =[]
for i in range(0,300):
    s.append(requests.Session())
    try:
        r=s[i].post('http://js.shu.edu.cn/Account/LogOn?ReturnUrl=%2fPageView%2fIndex%2f2',data=postData,timeout=10)
        if(re.search("注销", r.text, flags=0)):
            print("第{}/300个模拟登陆成功".format(i))
        else:
            print("第{}/300个模拟登录失败，进入下一轮".format(i))
    except:
         print("第{}/300个模拟登录失败，进入下一轮".format(i))

print("即将进入挂机状态")
for i in range(0,61):
    time.sleep(1)
    print("已挂机{}/60秒".format(i))
for i in range(0,300):
    try:
        s[i].get('http://js.shu.edu.cn/Account/LogOff',timeout=10)
        print("第{}/300个模拟注销成功".format(i))
    except:
        print("第{}/300个模拟注销失败，进入下一轮".format(i))

print("本次挂机成功，请登录军事理论网站查询已挂时长")
  
  
