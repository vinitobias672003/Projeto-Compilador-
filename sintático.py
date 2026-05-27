import json

with open(".\\saida_lexica.obj", "r", encoding="utf-8") as f:
    conteudo = f.read()

    # print(conteudo)

# var para imprimir o resultado e atuar durante o font
tokens = []
palavra = ""

# ajuda para manter possivel a lógica
operadores = "+-*/="
delimitadores = "(){};,"

# afd's que irão atuar para gerar o a analise sintática
for caractere in conteudo:

    # afd de numeros e simbolos 
    if caractere.isalnum() or caractere == "_":
        palavra += caractere

    else:

        # salva oq acaboud de definir/identificar
        if palavra != "":

            if palavra.isdigit():
                tokens.append({
                    "tipo": "NUMERO",
                    "valor": palavra
                })

            else:
                tokens.append({
                    "tipo": "IDENTIFICADOR",
                    "valor": palavra
                })

            palavra = ""

        # mesma apkicação para operadores 
        if caractere in operadores:
            tokens.append({
                "tipo": "OPERADOR",
                "valor": caractere
            })

        # # mesma apkicação para delimitadores
        elif caractere in delimitadores:
            tokens.append({
                "tipo": "DELIMITADOR",
                "valor": caractere
            })

# se terminace em palavra teria de ter outra 
if palavra != "":

    if palavra.isdigit():
        tokens.append({
            "tipo": "NUMERO",
            "valor": palavra
        })

    else:
        tokens.append({
            "tipo": "IDENTIFICADOR",
            "valor": palavra
        })

# fiz oq o senhor falou, tratei tudo em uma string zona reta
print(tokens)
# mesmo conceito do sintatico, juntar tudo em uma varia para facilitar a impresão 
conteudo_sintatico = {
    "tokens": tokens,
    "quantidade_tokens": len(tokens)
}

#  usei a ia para deixar mais facil de ler e ver se deu certo ou não
# print(json.dumps(conteudo_sintatico, indent=4, ensure_ascii=False))

# comecei a fazer no dia 25/05, facilitou muito a revisão para eu entender essa parte 

caminho = r"C:\Users\vinih\OneDrive\Área de Trabalho\comp\saida_sintatico.obj"

with open(caminho, "w", encoding="utf-8") as f:
    f.write(conteudo_sintatico)

print("Arquivo .obj criado!")


