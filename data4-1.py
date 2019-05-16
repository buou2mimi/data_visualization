# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 11:09
# 文件名称：data4-1.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt
from data4 import RandomWalk

 #只要程序处于活动状态，就不断地模拟随机漫步
while True:
     #创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
     # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
     # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break