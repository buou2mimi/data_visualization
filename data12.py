# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/6 11:03
# 文件名称：data12.py
# 开发软件：PyCharm
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(filename,dates,highs,lows):
    """Get the highs and lows from a data file"""
    with open(filename,'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                high = int(row[1])
                low =int(row[3])
            except ValueError:
                print(current_date,"missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

dates,highs,lows = [], [], []
get_weather_data('sitka_weather_2014.csv',dates,highs,lows)

fig = plt.figure(dpi = 128,figsize = (10,6))
plt.plot(dates,highs,c = 'red',alpha = 0.6)
plt.plot(dates,lows,c = 'blue',alpha = 0.6)
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.15)

dates,highs,lows = [], [], []
get_weather_data('death_valley_2014.csv',dates,highs,lows)

plt.plot(dates,highs,c = 'red',alpha = 0.3)
plt.plot(dates,lows,c = 'blue',alpha = 0.3)
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.05)

plt.title("Daily high and low temperatures - 2014\nSitka,Ak and Death Valley,CA",fontsize = 20)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize = 16)
plt.ylim((10,120))

plt.show()