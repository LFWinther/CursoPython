'''
1- Criar uma função que exibe uma saidação com os parâmetros "saudacao" e "nome".
'''
# def saudacao(msg='Saudações', nome=input('Nome: ')):
#     print(msg, nome)
# saudacao()

'''
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
'''

# def soma(n1=input('Digite um número: '), n2= input('Digige outro número: '), n3= input('Digite mais um número: ')):
#     n1 = int(n1)
#     n2 = int(n2)
#     n3 = int(n3)
#     return (n1+n2+n3)
# somar = soma()
# if somar:
#     print(somar)
# else:
#     print('Conta inválida')


'''
3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo é um persentual. (Ex:10%) Retorne (return) o
valor do primeiro número somado do aumento do percentual do mesmo.
'''
# print('Para descobrir a soma de um número por um porcentual dele, basta..')
# print()
# n1 = input('Digite o número que deseja samar: ')
# n2 = input('Digite o porcentual do número anterior: ')
# n1 = int(n1)
# n2 = int(n2)
# def soma(n1, n2):
#     if n2 > 0:
#         return n1 * n2 / 100
# somar = soma(n1, n2)
# if somar:
#     somar = int(somar)
#     print(n1+somar)
# else:
#     print('Conta inválida')

'''----------------------------------------------------------------------'''
# print('Para descobrir o percentual de um número.')
# n1=input('Digite um número que deseja descocobrir o percentual: ')
# n2=input('Digite um número para ser o percentual: ')
# n1=int(n1)
# n2=int(n2)
# def percentual(n1, n2):
#     if n2 > 0:
#         return (n1 * n2) / 100
# porcentagem = percentual(n1, n2)
# if porcentagem:
#     porcentagem = int(porcentagem)
#     print(porcentagem)
# else:
#     print('Conta inválida.')
'''-----------------------------------------------------------------------'''
'''
4- Fizz Buzz - Se o parâmetro  de função for divisivel por 3, retorne Fizz,
se o parâmetro da função for divisivel por 5, retorne Buzz, Se o parâmentroda função for 
divisivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorne número inválido.
'''
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'buzz'
    return 'n'