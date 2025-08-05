def calculadora_simples():
    print("Calculadora Simples Iniciada.")
    print("Para sair do programa, pressione Ctrl + C.")

    while True:
        try:
            entrada = input("\nDigite a operação (ex: 5 + 3): ")
            n1_str, operador, n2_str = entrada.split()
            n1 = float(n1_str)
            n2 = float(n2_str)

            print("Resultado:")
            match operador:
                case "+":
                    print(n1 + n2)
                case "-":
                    print(n1 - n2)
                case "*":
                    print(n1 * n2)
                case "/":
                    if n2 == 0:
                        print("Erro: Divisão por 0")
                    else:
                        print(n1 / n2)
                case _:
                    print("Erro: Operador inválido. Use +, -, * ou /")
        except ValueError:
            print("Erro: Entrada inválida. Use o formato: número operador número (ex: 5 + 3)")
        except KeyboardInterrupt:
            print("Programa encerrando...")
            break

# Chamada da função principal
calculadora_simples()