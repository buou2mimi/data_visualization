# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 10:02
# 文件名称：rw_visual2.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt
from random_walk import RandomWalk

 #只要程序处于活动状态，就不断地模拟随机漫步
while True:
     #创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s = 15)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break