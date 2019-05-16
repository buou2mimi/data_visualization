# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/6 11:48
# 文件名称：data13.py
# 开发软件：PyCharm
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_rainfall_2015.csv'
with open(filename,'r') as f:
    reader =csv.reader(f)
    header_row =next(reader)

    dates,rainfalls = [],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            rainfall = float(row[19])
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

fig = plt.figure(dpi = 128,figsize = (10,6))
plt.plot(dates,rainfalls,c = 'blue',alpha = 0.5)
plt.fill_between(dates,rainfalls,facecolor = 'blue',alpha = 0.2)

plt.title("Daily rainfall amounts - 2015\nSitka,AK",fontsize = 20)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)",fontsize = 16)
plt.tick_params(axis = 'both',which = 'major',labelsize = 16)
plt.ylim((0,4.5))
plt.xlim((dates[0],dates[-1]))

plt.show()
