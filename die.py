# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 11:45
# 文件名称：die.py
# 开发软件：PyCharm
from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides = 6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1,self.num_sides)
