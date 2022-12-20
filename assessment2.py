import pandas as pd
x=open('answer.txt','a')
n=int(input("enter the range:"))
s=[]
t=[]
for i in range(n):
    p=int(input("enter the number:"))
    t.append(p)

    s.append(p*p)
q = pd.Series(s,index=t)
print(q)
print(q,file=x)
x.close()