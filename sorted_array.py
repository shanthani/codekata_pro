#shanu
k=int(input())
s=[]
for i in range(k):
    l=list(map(int,input().split()))
    s=s+l
u=sorted(s)
c=0
for j in u:
    if c==0:
        print(j,end="")
        c=c+1
    else:
        print("",j,end="")
