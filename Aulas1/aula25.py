''' Operados relacionais
== Igual
> Maior que
>= Igual ou maior que
< Menor que
<= Igual ou menor que
!= Diferente
'''

nome = input('Nome: ')
idade = input('Idade: ')
idade = int(idade)
#apenas maires de 18 anso podem pegar emprestimo
de_maior = 18
de_menor = 30

if idade >= de_maior and idade <= de_menor:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo.')