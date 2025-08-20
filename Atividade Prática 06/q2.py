#dar o comando "pip install requests" sem aspas para rodar o código
import requests

def gerar_perfil():
  resposta = requests.get("https://randomuser.me/api/")

  if resposta.status_code == 200:
    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("<=== Usuário Gerado ===>")
    print(f"Nome : {nome}")
    print(f"Email: {email}")
    print(f"País : {pais}")
  else:
    print("Erro ao acessar a API!")

gerar_perfil()