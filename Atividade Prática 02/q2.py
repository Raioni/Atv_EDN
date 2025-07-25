nome = "Camiseta"
price = 50
discount = 0.20
discout_price = price * discount

print(f"Produto: {nome}")
print(f"Valor: R$ {price:.2f}")
print(f"Desconto: R${discout_price:.2f}")
print(f"\nValor Final: R${price - discout_price:.2f}")
