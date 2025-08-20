#dar o comando "pip install requests" sem aspas para rodar o código
import requests

def consultar_cotacao(moeda):
  url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados = resposta.json()
    chave = moeda + "BRL"

    if chave in dados:
      cotacao = dados[chave]
      
      valor_atual = float(cotacao['bid'])
      maximo = float(cotacao['high'])
      minimo = float(cotacao['low'])
      
      print(f"=== Cotação {moeda}/BRL ===")
      print(f"Valor atual: R$ {valor_atual:.2f}")
      print(f"Máximo     : R$ {maximo:.2f}")
      print(f"Mínimo     : R$ {minimo:.2f}")
      print(f"Data/Hora  : {cotacao['create_date']}")
    else:
      print("Moeda não encontrada na API")
  else:
    print("Erro ao acessar a API")

moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda_usuario)