# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 11:20
# 文件名称：data5.py
# 开发软件：PyCharm
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """确定方向和步长"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
