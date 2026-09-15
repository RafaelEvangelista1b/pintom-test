email = 'USUARIO@GMAIL.COM'
print(email)
print(email.lower()) # lower deixa o texto em letra minuscula

heroi = "batman"
print(heroi)
print(heroi.upper()) # upper deixa o texto em letra maiuscula

objeto = " lapis "
print(objeto)
print(objeto.strip()) # strip tira os espaços

palavra = "Carta"
print(palavra)
print(len(palavra)) # len conta o tamanho da palavra

posicao = email.find("@")
print(posicao) # find mostra a posicao do caracter

cortador = email[posicao:]
print(cortador)
cortador = email[:posicao]
print(cortador)
cortador = email[posicao+1:]
print(cortador)
cortador = email[7:9]
print(cortador) # o couchetes serve para colocar a posição do texto que deseja cortar

novo_email = email.replace("@GMAIL.COM", "@PORTALSEISI.ORG.BR")
print(novo_email) # replace troca um pedaço do texto

nome = "ricardo oliveira"
nome = nome.capitalize()
print(nome) # o capitalize deixa a primeira letra em maiusculo da primeira palva 
nome = nome.title()
print(nome) # o title coloca a primeira letra de cada palavra em maiusculo 


nome = "joão paulo lira"
email = "usuario@gmail.com"
posicao = email.find("@")
print(posicao) 
cortador = email[posicao+1:]
print(cortador) 
primeiro_nome = nome.find(" ")
primeiro_nome = nome.find(" ")
print(primeiro_nome)



