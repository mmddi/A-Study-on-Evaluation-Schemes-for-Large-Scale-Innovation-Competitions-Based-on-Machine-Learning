import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import xlrd as xl
from collections import Counter
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from pylab import legend

df = pd.read_excel(r"C:\Users\lenovo\Desktop\d.xls",usecols =[5])
df1 = pd.read_excel(r"C:\Users\lenovo\Desktop\d.xls",usecols =[14])

data_list = df.values.tolist()
data = [b for a in data_list for b in a]

data_list1 = df1.values.tolist()
data1 = [b for a in data_list1 for b in a]


bins = [70,100,130,160,190,220,250,280,310,340,370]




segments=pd.cut(data,bins,right=False)
segments1=pd.cut(data1,bins,right=False)


counts=pd.value_counts(segments,sort=False)
counts1=pd.value_counts(segments1,sort=False)


#y = gaussian_filter1d(counts, sigma=5)
#y1 = gaussian_filter1d(counts1, sigma=5)

b=plt.plot(counts.index.astype(str),counts,label='befor_method1')
b1=plt.plot(counts1.index.astype(str),counts1,label='befor_method2')
legend(bbox_to_anchor=(0.15, 1.15),)
plt.xticks(fontsize=7,rotation =45)
plt.show()



print(np.mean(df))
print(np.mean(df1))
print(np.var(df))
print(np.var(df1))
print(np.std(df))
print(np.std(df1))
print(np.max(df) - np.min(df))
print(np.max(df1) - np.min(df1))