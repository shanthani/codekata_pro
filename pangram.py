#shanu
n=input()
a={}
for j in range(97,123):
    a.update({chr(j):0})
n=n.replace(" ","")
n=n.lower()
c=0
for i in n:
    s=n.count(i)
    a.update({i:s})
for x,y in a.items():
    if y>=1:
        c=c+1
if c==26:
    print("yes")
else:
    print("no")
