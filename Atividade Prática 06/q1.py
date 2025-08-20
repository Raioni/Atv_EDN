import random, string

def gerar_senha(numero:int):
  senha = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=numero))
  return senha

tamanho = int(input("Digite o tamanho da senha: "))
print(f"Sua senha: {gerar_senha(tamanho)}")