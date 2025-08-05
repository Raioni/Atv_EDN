def media_turma():
    notas = []
    while True:
        entrada = input("\nDigite a nota do aluno (0 a 10)\nOu digite 'fim' para concluir: ")
        if entrada.lower() == "fim":
            break
        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("\nPor favor digite uma nota entre 0 e 10")
            else:
                notas.append(nota)
        except ValueError:
            print("Erro: entrada inválida")
    try:
        print(f"\n-----> Media da turma: {sum(notas) / len(notas):.2f}")
    except:
        print("Nenhuma nota registrada")

media_turma()
