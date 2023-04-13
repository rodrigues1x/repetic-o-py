
nome = input("Digite seu login: ")
senha = input("Digite sua senha:")

while nome == senha:
    print("Erro: A senha não deve ser igual ao nome")
    senha = input("Digite sua senha: ")
print("Login Ok")