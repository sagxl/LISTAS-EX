#1. Faça um programa que imprima o seu nome.
def q01():
#nome = input('digite seu nome ')
#print(f'ola {nome}. bom dia (a)!')
#ou

print('luis eduardo')

#----------------------------------------------------------------------------------------------------------------------------

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q02():
    print(30*27)

#----------------------------------------------------------------------------------------------------------------------------
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q03():
n1 = 6
n2 = 8
n3 = 12
soma = (n1+n2+n3) / 3
print(f'{soma}')

#----------------------------------------------------------------------------------------------------------------------------

#4. Faça um programa que leia e imprima um número inteiro.
def q04():
numero = int(input('digite um numero:'))
print(f'{numero}')

#----------------------------------------------------------------------------------------------------------------------------

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
nn1 = float(input('digite um primeiro numero:'))
nn2 = float(input('digite o segundo numero:'))
 
print(f'{nn1}\t{nn2}') 
print(f'{nn1}') 
print(f'{nn2}') 

#----------------------------------------------------------------------------------------------------------------------------

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
numero1 = int(input('digite um numero inteiro'))

antecessor = numero1 - 1
sucessor = numero1 + 1

print(f'o seu antecessor sera: {antecessor}\t E o sucessor sera : {sucessor}')

#ou 

numero =  int(input('digite um numero inteiro  '))

print(f'sucessor : {numero+1}')
print(f'antecessor: {numero-1}')
#----------------------------------------------------------------------------------------------------------------------------

#7Faça um programa que leia o nome o endereço e o telefone de
#  um cliente e ao final, imprima esses dados.
def q07():
nome = input('digite o seu nome:')
print(nome)
endereco = input('digite seu indereço: ') 
print(endereco)
telefone = input('disce o seu numero de telefone: ')
print(telefone)



#----------------------------------------------------------------------------------------------------------------------------

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
numero1 = int(input('digite um numero inteiro:'))
numero2 = int(input('digite outro numero inteiro: '))

subtracao = numero1 + numero2

print(f'o resultado sera {subtracao}')


#----------------------------------------------------------------------------------------------------------------------------

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
numero_real = float(input("Digite um número real: "))
um_quarto = numero_real / 4

print(f"1/4 de {numero_real} é: {um_quarto}")

#----------------------------------------------------------------------------------------------------------------------------
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
num_1 = float(input('digite um numero  em real')) 
num_2 = float(input('digite  numero  em real')) 
num_3 =float(input('digite  numero  em real')) 

media = (num_1 +num_2+ num_3) / 3

print(f'a media sera: {media}')
 
#----------------------------------------------------------------------------------------------------------------------------

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
num1 =  float(input('digite um nuemro real  '))
num2 = float(input('digite um nuemro real '))

print (f'{num1} + {num2} = {num1+num2}')
print (f'{num1} - {num2} = {num1-num2}')
print (f'{num1} * {num2} = {num1*num2}')
print (f'{num1} / {num2} = {round ((num1/num2),1)}')

#----------------------------------------------------------------------------------------------------------------------------

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
numero1 = float(input('digite um numero em real '))

quad = (numero1**2)

print(f'o quadradado sera {quad}')




#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():

saldo = float(input('digite seu saldo'))
print(f'{saldo*1.02}')


#----------------------------------------------------------------------------------------------------------------------------
#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).

base = int(input('digite a base '))
altura = int(input('digite a altura  '))

area = base*altura
perimetro = base + altura

print(f'a base area sera {area}\t e o perimetro sera {perimetro}')

#----------------------------------------------------------------------------------------------------------------------------
#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
    preco = float(input('Preço do produto: R$ '))
    desconto = float(input('Desconto (%): '))
    valor_desconto = preco * desconto / 100
    preco_final = preco - valor_desconto
    print(f'Valor do desconto: R$ {valor_desconto}')
    print(f'Preço final do produto: R$ {preco_final}')


#----------------------------------------------------------------------------------------------------------------------------
#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
#----------------------------------------------------------------------------------------------------------------------------
salario = float(input('Salário: R$ '))
reajuste = float(input('Reajuste (%): '))
novo_salario = salario * (1 + (reajuste / 100))
print(f'Novo salário: R$ {novo_salario:.2f}') #trunca até a segunda casa
 
 
#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
c



#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.




# def q10():