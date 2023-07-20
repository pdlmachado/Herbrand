y = float(input())
x = int(y)
print("NOTAS:")
print(f"{x // 100} nota(s) de R$ 100.00")
x = x % 100
print(f"{x // 50} nota(s) de R$ 50.00")
x = x % 50
print(f"{x // 20} nota(s) de R$ 20.00")
x = x % 20
print(f"{x // 10} nota(s) de R$ 10.00")
x = x % 10
print(f"{x // 5} nota(s) de R$ 5.00")
x = x % 5
print(f"{x // 2} nota(s) de R$ 2.00")
x = x % 2
print ("MOEDAS:")
x = (y - x) * 100
print(x)






