import math
a,b = [int(i) for i in input().split()]
if a == b:
    print("infinity")
elif a < b:
    print(0)
else:
    n = a-b
    limit = int(math.sqrt(n))
    count = 0
    for i in range(1,limit+1):
        if (n%i)==0:
            if n//i > b:
                count+=1
            if i > b and not (n//i==i):
                count+=1
    print(count)