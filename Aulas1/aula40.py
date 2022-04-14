''' for / else em Python '''

variavel = ['Luiz', 'Maria', 'Joao']
começa_j = False
for valor in variavel:
    if valor.startswith('J'):
        começa_j = True
if começa_j == True:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')
