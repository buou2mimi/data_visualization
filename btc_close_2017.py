# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/6 14:42
# 文件名称：btc_close_2017.py
# 开发软件：PyCharm
from __future__ import (absolute_import,division,print_function,unicode_literals)

try:
    #Python 2.x版本
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
#读取数据
req  = response.read()
with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)
#加载json格式
file_urllib = json.loads(req)
print(file_urllib)