import os

os.mkdir('exemplo')



nome_pasta = "minha_pasta"

# verifique se a pasta já existe
if not os.path.exists(nome_pasta):
    # se a pasta não existir, crie-a
    os.makedirs(nome_pasta)
    print(f"A pasta {nome_pasta} foi criada com sucesso!")
else:
    # se a pasta já existir, imprima uma mensagem
    print(f"A pasta {nome_pasta} já existe!")