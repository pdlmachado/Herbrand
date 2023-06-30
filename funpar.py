def é_impar (n):
    if n % 2 == 1:
        return True
    else:
        return False
    
numero1 = int(input("Digite o menor numero: "))
numero2 = int(input("Digite o maior numero: "))
for numero in range (numero1, numero2 + 1):
    if é_impar(numero) and numero < numero2-1:
        print (f"{numero}", end="-\n")
    elif é_impar(numero):
        print (f"{numero}")
