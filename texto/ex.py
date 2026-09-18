nome = "joão paulo lira"
email = "usuario@gmail.com"

# descobre o número do caracter
posicao = email.find("@") 
print(posicao) 

# descobre o tipo do servidor 
cortador = email[posicao+1:] 
print(cortador) 

# descobre o primeiro nome do usuário
posicao_nome = nome.find(" ")
primeiro_nome = nome[:posicao_nome]
print(primeiro_nome)

# mensagem final 
print(f"Usuario {primeiro_nome} foi cadastrado com sucesso no email {email}")