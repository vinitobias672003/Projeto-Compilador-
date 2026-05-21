import json

with open(".\\EXEMPLO.POR", "r", encoding="utf-8") as f:
    conteudo = f.read()
with open(".\\tabela_tokens.json", "r", encoding="utf-8") as f:
    reservadas = json.load(f)

# print(reservadas)


# tokem string já resolvido, roda por caracteres, e usa uma pilha para ver as strings 
tem_string = False
e_string = ""

for c in conteudo:
    if c=="\"":
        e_string += c
        if tem_string and c=="\"" :
            tem_string = False
            conteudo = conteudo.replace(e_string," STRING ")
            e_string = ""
        else:
            tem_string = True

    elif tem_string:
        e_string += c

print(conteudo)

acumula_tokem = ""  # é preenchido pelo for 
c_tokem= "" # é o resultado de bater o acumulado de carecteres, no json que é a tabela de tokens 
fim_palavra= len(conteudo)-1 # index ao contrario do caracter/palavras

for c in range(len(conteudo)-1,-1,-1):

    acumula_tokem = conteudo[c] + acumula_tokem
    
    # se for espaço ou enter, pula o caracter 
    if acumula_tokem == "\n" or acumula_tokem ==" ": 
        acumula_tokem = ""
        fim_palavra = c-1
        
    try:
        c_tokem = reservadas[acumula_tokem]
        # print(c_tokem)
        # confere as exceções mais chatas
        if c_tokem == "SE"  or c_tokem == "E" or c_tokem == "NAO" or c_tokem == "PARA" or c_tokem != reservadas[acumula_tokem]:
            
            #  faz as mudança 
            if conteudo[c-1] == " " or conteudo[c-1] == "\n":
                
                conteudo = conteudo[:c] + c_tokem + conteudo[fim_palavra:]
                fim_palavra = c-1
                c_tokem = " "
                acumula_tokem = ""
            else:   # era para fazer a troca da exceção das exceções, confere !!!
                conteudo = conteudo[:c] + " " + "id" + conteudo[fim_palavra:]



        else:       # se não for uma exceção, só usa a tabela de tokens
            conteudo = conteudo[:c] + " " + c_tokem + conteudo[fim_palavra+1:]
            fim_palavra = c-1
            c_tokem = " "
            acumula_tokem = ""



    except Exception as e:
        1==1  #o except precisa ter algo se não dá erro
    
print(conteudo)
