a, b, c, d = [float(i) for i in input().split()]
media = (a*2 + b*3 + c*4 + d*1) / 10
print (f"Media: {media:.1f}")
if media >= 7:
    print ("Aluno aprovado.")
elif media < 5:
    print ("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_do_exame = float(input())
    media_final = (nota_do_exame + media) / 2
    print (f"Nota do exame: {nota_do_exame:.1f}")
    if media_final >= 5:
        print ("Aluno aprovado.")
        print (f"Media final: {media_final:.1f}")
    else: 
        print ("Aluno reprovado.")