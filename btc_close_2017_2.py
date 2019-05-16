# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/6 15:30
# 文件名称：btc_close_2017_2.py
# 开发软件：PyCharm
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
#将数据写入文件
with open('btc_close_2017_request.json','w') as f:
    f.write(req.text)
file_requests = req.json()