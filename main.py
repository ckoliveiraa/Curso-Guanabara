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

# 22: Crie um programa que leia o nome completo de uma pessoa e mostre:0
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# nome = 'Carlos Oliveira'

# print(nome)
# print(len(nome))
# print(len(nome: 6))


#28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
# import random
# from time import sleep

# pc = random.randrange(0,5)
# user = int(input('Qual o número escolhido pelo pc? '))

# print ("PROCESSANDO...")
# sleep(2)
# if pc == user :
#     print(f'O número escolhido foi {pc}, você acertou!!!')
# else:
#     print(f'O número escolhido foi {pc}, você errou =(')

#29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
    #A multa vai custar R$7,00 por cada Km acima do limite.

# velo = int(input('Em qual velocidade você passou no radar? '))
# velo_max = 80
# multa = ((velo - velo_max)*7)

# if velo>velo_max:
#     print(f'Você ultrapassou o limite de velocidade em {velo-velo_max}Km/h, sua multa será de {multa}R$')
# else:
#     print(f'Você passou a {velo}Km/h o limite é {velo_max}Km/h, parabéns!')

#30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# num = int(input('Digite um número: '))
# par= (num%2==0)

# if par == True:
#     print('Seu número é par')
# else:
#     print('Seu número é impar')

##31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
#e R$0,45 parta viagens mais longas.

# km = float(input('Qual a distância em km da viagem? '))

# if km <= 200:
#     print(f'O custo por km é de 0,50R$, sua viagem tem {km}km logo seu custo será de R${km*0.50}')
# else:
#      print(f'O custo por km é de 0,45R$, sua viagem tem {km}km logo seu custo será de R${km*0.45}')

#32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# import calendar

# ano= int(input('Digite um ano: '))

# if calendar.isleap(ano) == True:
#     print ("Bissexto")
# else:
#     print('Normal')

#33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# num1 = 13
# num2 = 5
# num3 = 6

# lista = [num1 , num2, num3]

# print(f'Seu maior número é {max(lista)}, e o menor é {min(lista)}')


#34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

# salario = float(input('Digite seu salário: '))
# bonus1 = 0.1
# bonus2 = 0.15

# if salario> 1250:
#     print(f'Seu salário era de R${salario} você recebeu um aumento de 10% e agora receberá R${(salario*bonus1)+salario}')
# else:
#     print(f'Seu salário era de R${salario} você recebeu um aumento de 15% e agora receberá R${(salario*bonus1)+salario}')

# r1 = 5
# r2 = 10
# r3 = 16

# condicao = ((r1 + r2) < r3 or
# (r2 + r3) < r1 or
# (r3+r1) < r2)

# if condicao == True:
#     print('Pode ser formado um triângulo')
# else:
#     print('Não pode ser formado um triângulo')