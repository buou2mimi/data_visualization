# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 11:05
# 文件名称：data3.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt

from random_walk import  RandomWalk
#创建一个RandomWalk实例，并将其包含的点都绘制出来
rw =RandomWalk()
rw.fill_walk()
plt.plot(rw.x_values,rw.y_values,linewidth = 1)
plt.show()