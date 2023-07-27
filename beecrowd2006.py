saída = 0
numero_chá = int(input())
#a, b, c, d, e = [int(i) for i in input().split()]
#if a == numero_chá:
#    saída += 1
#if b == numero_chá:
#    saída += 1
#if c == numero_chá:
#    saída += 1
#if d == numero_chá:
#    saída += 1
#if e == numero_chá:
#    saída += 1
#print (saída)

lista = [int(i) for i in input().split()]
print(lista)
for i in range(5):
    if lista[i] == numero_chá:
        saída += 1
print(saída)
