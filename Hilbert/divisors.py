n, k = [int(i) for i in input().split()]
divisors = [1,n]
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        x = len(divisors)//2
        divisors.insert(x,n//i)
        divisors.insert(x,i)
