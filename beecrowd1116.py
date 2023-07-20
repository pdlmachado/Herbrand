n = int(input())
for m in range (n):
    x,y = [int(i) for i in input().split()]
    if y  == 0:
        print ("divisao impossivel")
    else:
        print (f'{x / y:.1f}')

    