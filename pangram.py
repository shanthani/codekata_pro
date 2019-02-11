#shanu
n=input()
a=[]
for i in range(65,91):
    a.append(chr(i))
for j in range(97,123):
    a.append(chr(j))
n=n.replace(" ","")
for k in n:
    if k in a:
        c=c+1
    else:
       

