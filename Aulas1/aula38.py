'''
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, min, max
range
'''

# A lista é uma variável que  pode ter mais de um valor
# lista = [1, 2, 3, 4, 'Luis', 1.1]

#         0    1    2    3    4
lista = ['A', 'Bacana', 'C', 'D', 'E']
#    -    5    4    3    2    1

# str = 'ABCDE'
# print(lista[1])

'''_____________________________________'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4= list(range(1,10))  # l4 = l3


# l2.append("a")  #adcina algo no final da lista
# l1.extend(l2)  #junta uma variavel com alguma coisa
# l2.insert(0, 'BANANA')  #ADICONA ALGO NO INDICE SELECIONADO
# l2.pop()  #remove o último elemnto da lista
# del(l3[3:6])  #romeve o elemto que seliciona na lista
# # print(max(l3))  #mostrar o maximo da lista
# print(min(l3))  #mostrar o minimo da lista


"""ATIVIDADE"""
secreto = 'PERFUME'
digitadas = []
chances = 6
perdeu = 'Você PERDEU!!'
ganhou = 'Você GANHOU!!'

while True:
    letra = input('Digite uma letra: ')
    letra = letra.upper()
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra {letra} existe na palavra.')
    else:
        print(f'Poxa, não tem essa letra na palavra.')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta.upper()
        else:
            secreto_temporario += "*"
    if secreto_temporario == secreto:
        print(f'{ganhou:-^50}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if chances <= 0:
        print(f'A palavra era {secreto.upper()}')
        break
    if letra not in secreto:
        chances -= 1
        if chances > 0:
            print(f'Você tem {chances} chances.')
        else:
            print(f'{perdeu:-^50}')
            print(f'A palavra secreta era:')
            print(f'{secreto.upper():_^50}')
            break
