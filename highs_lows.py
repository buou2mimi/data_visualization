# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 17:21
# 文件名称：highs_lows.py
# 开发软件：PyCharm
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename,'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #for index,column_header in enumerate(header_row):
        #print(index,column_header)
fig = plt.figure(dpi = 128,figsize = (10,6))
plt.plot(dates,highs,c = 'red',alpha = 0.5)
plt.plot(dates,lows,c = 'blue',alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor = 'yellow',alpha = 0.5)
#设置图形格式
plt.title("Daily high and low temperatures -2014\nDeath Valley,CA",fontsize = 20)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize = 16)
plt.tick_params(axis = 'both',which = 'major',labelsize = 16)

plt.show()