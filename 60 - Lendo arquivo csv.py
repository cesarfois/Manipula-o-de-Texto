# https://www.youtube.com/watch?v=AnJPtKLtc7o

# Lendo um arquivo csv


import csv
lista = []
with open('indexadores.csv', mode='r') as file:
    data_csv = csv.reader(file, delimiter=';')
    for i, linha in enumerate(data_csv):
        print(i, linha)
        if linha[0] == 'doc':
            print('achei')
            for j in linha:
                lista.append(j)


print(lista)
