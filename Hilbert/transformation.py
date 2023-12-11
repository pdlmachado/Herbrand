def dfs(x,lista,step):
    if (x == k):
        return True, lista
    elif x > k:
        return False, lista
    else:
        achou, nlista = dfs(x*10+1,lista + [x*10+1],step+1)
        if achou: return achou, nlista
        return dfs(x*2,lista + [x*2],step+1)
    
n,k = [int(i) for i in input().split()]
achou, lista = (dfs(n,[n],1))
if achou:
    print("YES")
    print(len(lista))
    print(" ".join([str(i) for i in lista]))
else:
    print("NO")
