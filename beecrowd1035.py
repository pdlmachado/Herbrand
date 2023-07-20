def é_par (n):
    if n % 2 == 0:
        return True
    else:
        return False

A, B, C, D = [int(i) for i in input().split()]
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and é_par (A):
    print ("Valores aceitos")
else: 
    print ("Valores nao aceitos")
