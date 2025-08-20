#2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo
#(lê-se igual de trás para frente, ignorando espaços e pontuação).
#Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”0.
    
def palindromo_check(palavra:str):
    palavra = palavra.lower()
    reverso = palavra[::-1]
    if palavra.replace(" ", "") == reverso.replace(" ", ""):
        return "Sim"
    else:
        return "Não"


print(palindromo_check("a torre da derrota"))