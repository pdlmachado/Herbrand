n = int(input())
lista = [int(i) for i in input().split()]
maximo = lista[0]
l = len(lista)
for x in range(l):
    for y in range(x+1,l):
        subarray = lista[x:y+1]
        soma = sum(subarray)
        #print(subarray,soma)
        if soma > maximo:
            maximo = soma
print(maximo)