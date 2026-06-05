import json

with open(".\saida_lexica.obj", "r", encoding="utf-8") as f:conteudo = f.read()

tokens_entrada = conteudo.split()

tokens = []

operadores = [
"OPMAIS",
"OPMENOS",
"OPMULTI",
"OPDIV",
"LOGMAIOR",
"LOGMENOR",
"LOGIGUAL",
"LOGDIF",
"ATRIB"
]

delimitadores = [
"PARAB",
"PARFE",
"PVIR",
"DOISP",
"VIRG"
]

reservadas = [
"TIPO",
"ESCREVA",
"STRING",
"SEe",
"ENTAO",
"SENAO",
"FIMSE",
"PARAa",
"ATE",
"PASSO",
"FIMPARA"
]

for token in tokens_entrada:


    if token.isdigit():
        tokens.append({
            "tipo": "NUMERO",
            "valor": token
        })
        
    elif token in operadores:

        tokens.append({
            "tipo": "OPERADOR",
            "valor": token
        })

    elif token in delimitadores:

        tokens.append({
            "tipo": "DELIMITADOR",
            "valor": token
        })

    elif token in reservadas:

        tokens.append({
            "tipo": "RESERVADA",
            "valor": token
        })

    else:

        tokens.append({
            "tipo": "IDENTIFICADOR",
            "valor": token
        })

conteudo_sintatico = {
"tokens": tokens,
"quantidade_tokens": len(tokens)
}

caminho = r"C:\Users\vinih\OneDrive\Área de Trabalho\comp\saida_sintatico.obj"
with open(caminho, "w", encoding="utf-8") as f:
    f.write(json.dumps(conteudo_sintatico, indent=4, ensure_ascii=False))

print(conteudo_sintatico)
