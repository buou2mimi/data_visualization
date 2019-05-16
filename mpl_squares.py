# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 15:23
# 文件名称：mpl_squares.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5) #设置线宽

#设置图表标题，并给坐标轴加上标签
plt.title("Square Number",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

#设置刻度标记大小
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()