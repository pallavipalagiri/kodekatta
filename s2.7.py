p=int(input())
sum=0
k=p
while p>0:
    c=p%10
    sum=sum+c*c*c
    p=p//10
if k==sum:
    print("yes")
else:
    print("no")
