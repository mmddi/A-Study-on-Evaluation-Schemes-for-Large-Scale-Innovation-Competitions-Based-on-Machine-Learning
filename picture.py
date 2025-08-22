import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.ndimage import gaussian_filter1d


df = pd.read_excel(r"C:\Users\lenovo\Desktop\2.2.xls",usecols =[36])
df1 = pd.read_excel(r"C:\Users\lenovo\Desktop\2.2.xls",usecols =[37])


df_list = df.values.tolist()
dff = []

for i in df_list:
    dff.append(i[0])

df1_list = df1.values.tolist()
dff1 = []

for i in df1_list:
    dff1.append(i[0])


print(df)

x = [i for i in range(1500)]
y = gaussian_filter1d(dff, sigma=5)
y1 = gaussian_filter1d(dff1, sigma=5)

plt.plot(x,y,linewidth=2,label='First review')
plt.plot(x,y1,color='r',linewidth=2,label='Second review')
#print(dff)
#plt.plot(dff,label='First review',color='b')
#plt.plot(dff1,color = 'r',label='Second review')

plt.legend()
plt.show()