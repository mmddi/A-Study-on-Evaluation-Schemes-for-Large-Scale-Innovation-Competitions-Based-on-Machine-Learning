import numpy as np
import math
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.ndimage import gaussian_filter1d
import pandas as pd  # 引入pandas库

expert = 125
product = 3000

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
length = 25
b = [0]*length         #b是期望
c = [0]*length         #c是标准差
def combination(m, n):
  return math.factorial(m) / (math.factorial(n) * math.factorial(m-n))

for i in range(1,26):
    expert_group = math.ceil(expert/i)

    if expert_group-5 >= 5:
        zero_person = combination(expert_group-5,5)/combination(expert_group,5)
    else:
        zero_person = 0
    if expert_group-5 >= 4:
        one_per = 5*combination(expert_group-5,4)/combination(expert_group,5)
    else:
        one_per = 0
    if expert_group - 5 >= 3:
        two_per = 10*combination(expert_group-5,3)/combination(expert_group,5)
    else:
        two_per = 0
    if expert_group - 5 >= 2:
        three_person = 10*combination(expert_group-5,2)/combination(expert_group,5)
    else:
        three_person = 0
    if expert_group - 5 >= 1:
        four_person = 5*combination(expert_group-5,1)/combination(expert_group,5)
    else:
        four_person = 0
    if expert_group - 5 >= 0:
        five_person = 1/combination(expert_group,5)
    else:
        five_person = 0
    m = one_per*1+two_per*2+three_person*3+four_person*4+five_person*5
    b[i-1] = round(m, 2)  # 保留2位小数
    n = one_per*1+two_per*4+three_person*9+four_person*16+five_person*25
    j = int((n-m*m)*10000)
    c[i-1] = round(math.sqrt(j)/100, 2)  # 保留2位小数

# 创建一个名为result.csv的CSV文件，并将数据写入其中
data = {'Group': a, 'Mean': b, 'Standard Deviation': c}
df = pd.DataFrame(data)
df_transposed = df.transpose()  # 进行表格转置

# 将数据保存到CSV文件
df_transposed.to_csv('result.csv', index=False)

# 绘制图表（你的图表绘制代码不变）
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('standard deviation tendency chart')
ax1.set_xlabel('the group')
ax1.set_ylabel('the standard deviation')
y_smoothed = gaussian_filter1d(c, sigma=5)
plt.scatter(a, c, linewidths=1, s=30, c='b')
plt.plot(a, c, color='r')
plt.show()