'''Desempacotamento de listas de Python'''

lista = ['Luis', 'João', 'Maria', 1, 2, 3]
n1, n2, n3, *outra_lista = lista
print(outra_lista[-1])