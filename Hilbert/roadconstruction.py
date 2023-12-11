
def dfs (v,comp):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            dfs(u,comp.append(u))


n,m = [int(i) for i in input().split()]
adj = [[] for i in range(n+1)]
for i in range(m):
    u,v = [int(i) for i in input().split()]
    adj[u].append(v)
    adj[v].append(u)
    visited = [False for i in range(n+1)]
    s_comp = 1
    bridges = []
    for i in range(1,n+1):
        if visited[i] == False:
            bridges.append(i)
            comp = [i]
            dfs(i,comp)
            if len(comp)>s_comp:
                s_comp = len(comp)
    print(bridges)
    print(adj)
    print(f"{len(bridges)} {s_comp}")

