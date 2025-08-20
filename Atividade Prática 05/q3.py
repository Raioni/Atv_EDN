def calc_desconto(preco:float, percent:float):
    desconto = preco * (percent / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)
    
user_price = float(input("Digite o valor do produto: R$ "))
porcentagem = float(input("Digite a porcentagem de desconto: "))
print(f"Preço final com desconto: {calc_desconto(user_price, porcentagem)}")