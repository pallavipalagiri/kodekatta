a=int(input())
b=0
while(a>0):
    p=a%10
    a=int(a/10)
    b+=p*p
print(b)    
