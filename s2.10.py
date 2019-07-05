p,k=map(int,input().split())
for i in range(p+1,k):
    s=0
    a=i
    while(a>0):
        c=a%10
        s+=c**3
        a//=10
    if(i==s):
            print(i,end=" ")
    
