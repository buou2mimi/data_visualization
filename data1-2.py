# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/4 17:27
# 文件名称：data1-2.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,edgecolors = 'none',s = 20)

plt.title("Cube Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Cube Value",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.axis([0,5100,0,5100**3])
plt.show()
