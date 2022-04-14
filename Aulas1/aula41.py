'''
Split, join e enumerate em Python
* split - dividir uma str #str
* join - juntar uma lista #str
* enumerate - enumerar elementos da lista #lista
'''
# string = 'O Brasil é o país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
# palavra = ''
# contagem = 0
#
# for valor in lista_1:
#     qtd_x = lista_1.count(valor)
#     if qtd_x > contagem:
#         contagem = qtd_x
#         palavra = valor
# print(f'A palavra que apareceu mais vezes é: {palavra} ({contagem}x)')
'''---------------------------------------------------------------------------'''
# string = 'O brasil é penta.'
# lista = string.split(' ')
# string_2 = ' '.join(lista)
# print(string)
# print(lista)
# print(string_2)
'''--------------------------------------------------------------------------------'''
lista = ['Luis', 'João', 'Maria']
# for indice, nome in enumerate(lista):
#     print(indice, nome)

n1, n2, n3 = lista
print(n2)