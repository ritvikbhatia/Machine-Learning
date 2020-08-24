import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("C:\\Users\\Ritvik\\Documents\\zomato.csv",encoding='latin-1')
b=a[['Restaurant Name','City','Aggregate rating']]
c=b.groupby('City')
d=list(c.groups.keys())
g={}
t=[]
for i in range(len(d)):
    co=c.get_group(d[i])['Restaurant Name'].count()
    g[co]=d[i]
top=sorted(g,reverse=True)[:5]
for i in range(5):
    print(g[top[i]],":",top[i])
    t.append(g[top[i]])

plt.plot(t,top)
plt.show()
