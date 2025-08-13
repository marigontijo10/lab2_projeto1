print ("Hello World")

import random 

def cumprimento (texto):
    return f"Olá {texto}"

def media_7_numeros():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return numeros, media

 if_name_=="_main_":
    nome_completo = "Mariana Gontijo"
    print (cumprimento(nome_completo))
    numeros, media = media_7_numeros()
    print (f"Números sorteados: {números}")
    print (f"Média dos números: {média}")


