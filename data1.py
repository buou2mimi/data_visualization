# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 17:01
# 文件名称：data1.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]
plt.scatter(x_values,y_values,s = 100)

plt.title("Cube Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Cube Value",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.show()