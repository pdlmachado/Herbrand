y = float(input())
x = int(y)
d = int((y - x) * 100)
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
print(f"{x // 1} moeda(s) de R$ 1.00")
x = x % 1
print(f"{d // 50} moeda(s) de R$ 0.50")
d = d %50
print(f"{d // 25} moeda(s) de R$ 0.25")
d = d %25
print(f"{d // 10} moeda(s) de R$ 0.10")
d = d %10
print(f"{d // 5} moeda(s) de R$ 0.05")
d = d %5
print(f"{d // 1} moeda(s) de R$ 0.01")
d = d %1








