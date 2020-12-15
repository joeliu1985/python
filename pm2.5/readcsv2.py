import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("深圳-air-quality - 副本.csv")
df['date']=pd.to_datetime(df['date'],format='%Y/%m/%d')
sort=df.sort_values(by='date',ascending=True)
plt.figure(num=1111,figsize=(26,16))
plt.plot(sort.date,sort.pm25)
#plt.tight_layout()
#plt.savefig("pm25-2.png", dpi=200)
plt.show()
array=np.array(df['pm25'].tolist(), dtype = float)
list=[x for x in array if x != 'nan']

list_a=[elem if not np.isnan(elem) else None for elem in array ]
while None in list_a:
	list_a.remove(None)

print(np.median(list_a))
print(np.mean(list_a))
t = np.array([1,2,3,4])

print(np.median(t))
print(df.describe())