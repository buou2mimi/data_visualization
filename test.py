# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/15 19:54
# 文件名称：test.py
# 开发软件：PyCharm
import json
import pygal

#将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename,'r') as f:
    btc_data = json.load(f)

#创建5个列表，分别存储日期和收盘价
dates = []
months =[]
weeks = []
weekdays = []
close = []
#打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

idx_month = dates.index('2017-12-01')
#print(idx_month)
#print(months[:idx_month],close[:idx_month])

idx_week = dates.index('2017-12-11')
#print(idx_week)
#print(weeks[1:idx_week],close[1:idx_week])

from itertools import groupby
data = groupby(sorted(zip(weeks[1:idx_week],close[1:idx_week])),key = lambda _: _[0])
print(data)
xy_map = []
for x, y in data:
    y_list = [v for _, v in y]
    print(y_list)
    xy_map.append([x, sum(y_list) / len(y_list)])
    print(xy_map)
print(y_list)
print(xy_map)