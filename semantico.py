import json

with open(".\\saida_lexica.obj", "r", encoding="utf-8") as f:
    lexico = f.read()

with open(".\\saida_sintatico.obj", "r", encoding="utf-8") as f:
    sintatico = f.read()

tokens = sintatico.split()
variavel_definida = False
i = 0

while i < len(tokens):

    #print(tokens[i]) 
    # verifica declara
    if (
        i + 2 < len(tokens)
        and tokens[i] == "TIPO"
        and tokens[i + 1] == "DOISP"
        and tokens[i + 2] == "id"
    ):

        variavel_definida = True
        print("variavel definida")

        i += 3
        continue

    #print(tokens[i]) 
    # verifica uso da var
    if tokens[i] == "id":

        if variavel_definida == False:
            print("erro: variavel não definida")

    i += 1

print("sem erros, variaveis definidas")
