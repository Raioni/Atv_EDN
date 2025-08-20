#1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
#gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
#Parâmetros:
#a - valor_conta (float): O valor total da conta
#b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
#c - retorna: float: O valor da gorjeta calculada#

def calc_gorjeta(valor_conta:float, porcentagem_gorgeja:float):
    gorjeta = valor_conta * (porcentagem_gorgeja/100)
    return round(gorjeta,2)

print(f'Valor da conta : 132.00 \nValor da gorjeta (10%): {calc_gorjeta(132.0,10)}')
    

