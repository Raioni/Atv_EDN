def check_senha(senha):
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("\nSenha forte")
    else:
        print("\nSua senha é fraca, por favor digite uma senha")
        print("com pelo menos 8 digitos e um número\n")
    return

while True:
    try:
        password = input("Digite a senha (Ctrl + C para sair): ")
        check_senha(password)
    except KeyboardInterrupt:
        print("\nPrograma encerrando...")
        break


