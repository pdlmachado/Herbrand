n = int(input())
lista = [int(i) for i in input().split()]
max_so_far = lista[0]
max_ending_here = 0
for x in range(len(lista)):
    max_ending_here = max_ending_here+lista[x]
    if (max_so_far<max_ending_here):
        max_so_far=max_ending_here
    if(max_ending_here<0):
        max_ending_here=0
print(max_so_far)