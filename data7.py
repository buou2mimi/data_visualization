# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 15:50
# 文件名称：data7.py
# 开发软件：PyCharm
import pygal
from die import Die

#创建两个D6骰子
die_1 = Die(8)
die_2 = Die(8)
#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result =die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result + 1):
    frequency = results.count(value) #统计各个数字在列表results中出现的次数
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"

hist.add('D8 + D8',frequencies)
hist.render_to_file('same8_dice_visual.svg')

print(frequencies)