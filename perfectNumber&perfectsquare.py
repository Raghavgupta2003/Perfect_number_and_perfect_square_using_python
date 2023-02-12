#perfect number_____________________________________
n=int(input())
for i in (1,n):
    sum=0
    if i%2==0:
        sum+=i
if sum==n:
    print("perfect")
else:
    print("not perfect")
# perfect square or not:_________________________________________
n=int(input())
flag=0
for i in range(1,n+1):
    if i*i ==n:
        flag=1
        break
if flag==1:
    print("perfect square")
else:
    print("not perfect square")

    
