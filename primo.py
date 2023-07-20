número = int(input("Digite um número: "))
é_primo = True
for x in range(2, número // 2):
    if número % x == 0:
        é_primo = False
        break
if é_primo == True:
    print ("é primo")
else:
    print ("não é primo")