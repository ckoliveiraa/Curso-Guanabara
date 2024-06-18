# 06 - monte um valor que receba um número int e de seu sucesso e antecessor
# numero = int(input ('Digite um número: '))
# print (f'Sucessor: {numero+1}, Antecessor: {numero-1}')

# 07 - Crie um algoritimo que leia um número e mostre seu dobro, tripo e raiz quadrada

# numero = int(input('Digite um número inteiro '))
# print (f'Seu dobro é {numero*2} \n Seu triplo é {numero*3} \n Sua raiz quadrada é {numero** (1/2)}')


# 08 -Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
# nota = float(input('Digite a nota do 1ª Prova '))
# nota_1 = float(input('Digite a nota do 2ª Prova '))

# print (f'A média do aluno é de {(nota+nota_1)/2}')

# 09 - Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
# numero = int(input('Digite um número inteiro '))

# print(f'{numero} x 1 = {numero*1} \n {numero} x 2 = {numero*2} \n {numero} x 3 = {numero*3} \n {numero} x 4 = {numero*4}')


# 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 1dol = 3,27
# d = float(input('Quanto vc tem na carteira em R$? '))
# print (f'Você pode comprar {(d/3.27):.2f}$ dolls')

# 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la. 1l tinta = 2m²

# b = float(input('Qual o tamanho da largura da sua parede em metros? '))
# c = float(input('Qual o tamanho do comprimento da sua parede em metros? '))
# tinta = (b*c)/2
# print (f'Sua parede tem {b*c}m², serão necessários {tinta} latas de tinta para pinta-lá')


# 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# produto = float(input('Qual o preço do produto? '))
# print (f'O valor com 5% de desconto fica em R$ {produto-(produto*0.05)}')


# 13 -Faça um algoritomo que leia o salário e mostre seu novo salário com 15% de aumento
# salario = int(input('Qual o seu salário? '))
# print(f'O valor com o reajuste de 15% fica em R$ {salario+(salario*0.15)}')

# 4: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# t = int(input('Digite a temperatura em Celsius: '))
# f = (t * 1.8) +32
# print (f'A temperatura em Fahrenheit é de {f}ºF. ')

# 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# km = float(input('Quantos km foram percorridos? '))
# dia = int(input('Quantos dias o carro ficou alugado? '))

# calc_km = km * 0.15
# calc_dia = dia * 60

# print (f'Você ira pagar {calc_km}R$ pelos {km}KM rodados e {calc_dia}R$ pelo o aluguel de {dia} dias')

# 6: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# import math as mt

# n = float(input('Digite um número decimal: '))
# print(f'O valor novo é {mt.trunc(n)}')

# 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# import math as mt

# co = int(input('Digite o valor do cateto oposto '))
# ca = int(input('Digite o valor do cateto adjacente '))

# hp = mt.hypot(co,ca)

# print (f'O valor da hipotenusa é {hp:.2f}')

# 18Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# import math as mt
# ang = int(input('Digite o valor de um ângulo'))

# print (f'O seno desse ângulo é {mt.sin(mt.radians(ang)):.2f}')
# print (f'O cosseno desse ângulo é {mt.cos(mt.radians(ang)):.2f}')
# print (f'A tangente desse ângulo é {mt.tan(mt.radians(ang)):.2f}')

# 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# import random as rd

# lista_alunos = ['João', 'Maria', 'Pedro', 'José']

# print (rd.choice(lista_alunos))

# 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# import random as rd

# lista_alunos = ['João', 'Maria', 'Pedro', 'José']
# rd.shuffle (lista_alunos)

# print (lista_alunos)

# 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# N/A

# 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = 'Carlos Oliveira'

print(nome)
print(len(nome))
print(len(nome: 6))
