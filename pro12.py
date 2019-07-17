p,aj=map(int,input().split())
c=list(map(int,input().split()))
for i in range(aj):
  u,v=map(int,input().split())
  print(sum(c[u-1:v]))
