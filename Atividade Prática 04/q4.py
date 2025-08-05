def contador():
    pares = 0
    impares = 0
    while True:
        try:
            num = int(input("Digite um número inteiro (0 cancela): "))
            if num == 0:
                break
            elif num % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Erro: entrada inválida")
        
    print("Números pares:", pares)
    print("Números impares: ", impares)

contador()
