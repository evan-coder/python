import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"]=["SimHei"]
n = 5
numbers = ['1', '2', '3', '4', '5']
chinese = [72, 80, 66, 77, 92]
math = [62, 92, 72, 75, 88]
english = [76, 81, 73, 75, 88]

chma = [math[i]+chinese[i] for i in range(5)]
x = np.arange(n)
print(x)

plt.bar(x, chinese, bottom=0, color='r', label='语文')
plt.bar(x, math, bottom=chinese, color='g', label="数学")
plt.bar(x, english, bottom=chma, color='c', label="英语")

plt.ylim(0, 300)
plt.title("成绩")
plt.legend(loc="upper right")
plt.grid(axis='y', color='gray', linestyle=':', linewidth=2)
plt.xticks(x, numbers)
plt.xlabel("学号")
plt.show()
