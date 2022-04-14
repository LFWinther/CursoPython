# ''' CPF = 150.793.057-70'''
# '''
# 1 * 10 = 10  # 1 * 11 = 11
# 5 * 9 = 45   # 5 * 10 = 50
# 0 * 8 = 0    # 0 * 9 = 0
# 7 * 7 = 49   # 7 * 8 = 56
# 9 * 6 = 54   # 9 * 7 = 63
# 3 * 5 = 15   # 3 * 6 = 18
# 0 * 4 = 0    # 0 * 5 = 0
# 5 * 3 = 15   # 5 * 4 = 20
# 7 * 2 = 14   # 7 * 3 = 21
#              # 7 * 2 = 14       253
#
# 11 - (202 % 11) =
# 7 > 9 = 0
# digito 1 = 0
# '''
# print(11+50+0+56+63+18+0+20+21+14)
#
# if (11-(253%11)) > 9:
#     print(0)
# else:
#     print(11-(253%11))
'''-------------------------------------------------'''
cpf = input('Digite um CPF: ')
novo_cpf = cpf[:9]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11-(total%11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
if cpf == novo_cpf:
    print('Válido.')
else:
    print('Inválido.')