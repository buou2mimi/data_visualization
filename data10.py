# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/5 16:20
# 文件名称：data10.py
# 开发软件：PyCharm
import matplotlib.pyplot as plt
from die import Die

die = Die()

results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(1,die.num_sides + 1)]
plt.title("Results of rolling one D6 1000 times.",fontsize = 24)
plt.xlabel("Result",fontsize = 14)
plt.ylabel("Frequencies of Result",fontsize = 14)
plt.bar([str(x) for x in range(1,die.num_sides + 1)],frequencies,color = 'rgb')
plt.show()

