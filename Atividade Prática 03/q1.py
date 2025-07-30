idade = int(input())

if idade >= 60:
    print("Idoso")
elif (idade < 60) and (idade >= 18):
    print("Adulto")
elif (idade < 18) and (idade >= 13):
    print("Adolescente")
else:
    print("Criança")