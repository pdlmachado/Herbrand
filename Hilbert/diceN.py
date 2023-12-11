def find (N,temp):
    if N == 0:
        return 1
    if temp[N] != -1:
        return temp[N]
    count = 0
    for i in range(1,7):
        if (N-i >= 0):
            count = count + find(N-i,temp)
    temp[N] = count
    return temp[N]

N = int(input())
resultados = [-1 for i in range(N+1)]
print(find(N,resultados)%1000000007)
