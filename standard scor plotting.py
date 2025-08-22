import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.ndimage import gaussian_filter1d

df = pd.read_excel(r"C:\Users\lenovo\Desktop\as.xls",usecols =[2])
df1 = pd.read_excel(r"C:\Users\lenovo\Desktop\as.xls",usecols =[3])
df2 = pd.read_excel(r"C:\Users\lenovo\Desktop\as.xls",usecols =[4])


df_list = df.values.tolist()
dff = []
for i in df_list:
    dff.append(i[0])

df1_list = df1.values.tolist()
dff1 = []
for i in df1_list:
    dff1.append(i[0])

df2_list = df2.values.tolist()
dff2 = []
for i in df2_list:
    dff2.append(i[0])


x = [i for i in range(2015)]
y = gaussian_filter1d(dff, sigma=5)
y1 = gaussian_filter1d(dff1, sigma=5)
y2 = gaussian_filter1d(dff2, sigma=5)

plt.plot(x,y,linewidth=2,label='Original standard score')
plt.plot(x,y1,color='r',linewidth=2,label='New standard score')
plt.plot(x,y2,color='g',linewidth=2,label='great standard score')

#plt.plot(dff,label='Original standard score',color='g')
#plt.plot(dff1,color = 'r',label='New standard score')
#plt.plot(dff2,color = 'r',label='great standard score')


plt.legend()
plt.show()
