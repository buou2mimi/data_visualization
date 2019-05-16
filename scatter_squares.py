# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 16:05
# 文件名称：scatter_squares.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s = 100)
#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel('Square of Value',fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)

plt.show()