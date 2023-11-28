import numpy as np
import pandas as pd
from scipy.spatial import distance


df = pd.read_excel(r"C:\Users\lenovo\Desktop\3.2.xls",usecols =[8])
df1 = pd.read_excel(r"C:\Users\lenovo\Desktop\3.2.xls",usecols =[6])

rank_list = df.values.tolist()
rank = []

for i in rank_list:
    rank.append(i[0])

ranknew_list = df1.values.tolist()
rank_new = []

for i in ranknew_list:
    rank_new.append(i[0])

x = [rank,rank_new]

V=np.array([rank,rank_new])
S=np.cov(V)
SI = np.linalg.inv(S)

print("新旧排名之间——欧氏距离、canberra、马氏距离、切氏距离、明氏距离、角度相似系数分别为：")
for i in range(len(x)):
    for j in range(i+1,len(x)):
        print("x{}-x{}:".format(i+1,j+1),distance.euclidean(x[i],x[j]))
        print("x{}-x{}:".format(i + 1, j + 1), distance.canberra(x[i], x[j]))
        print("x{}-x{}:".format(i + 1, j + 1), distance.cityblock(x[i], x[j]))
        print("x{}-x{}:".format(i + 1, j + 1), distance.chebyshev(x[i], x[j]))
        print("x{}-x{}:".format(i + 1, j + 1), distance.minkowski(x[i], x[j]))
        print("x{}-x{}:".format(i + 1, j + 1), distance.cosine(x[i], x[j]))
k = 0
