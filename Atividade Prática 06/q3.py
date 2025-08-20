#dar o comando "pip install requests" sem aspas para rodar o código
import requests

def consultar_endereco(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados = resposta.json()

    if "erro" in dados:
      print("CEP não encontrado")
    else:
      print("<=== Endereço Encontrado ===>")
      print(f"Logradouro: {dados['logradouro']}")
      print(f"Bairro    : {dados['bairro']}")
      print(f"Cidade    : {dados['localidade']}")
      print(f"Estado    : {dados['uf']}")
  else:
    print("Erro ao acessar a API")

cep_usuario = input("Digite o CEP (apenas números): ")
consultar_endereco(cep_usuario)