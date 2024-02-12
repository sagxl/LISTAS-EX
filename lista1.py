#1. Faça um programa que imprima o seu nome.

nome = input('digite seu nome ')
print(f'ola {nome}. bom dia (a)!')
#ou

print('luis eduardo')

#----------------------------------------------------------------------------------------------------------------------------

#2. Faça um programa que imprima o produto dos valores 30 e 27.

   print(30*27)

#----------------------------------------------------------------------------------------------------------------------------
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.

n1 = 6
n2 = 8
n3 = 12
soma = (n1+n2+n3) / 3
print(f'{soma}')

#----------------------------------------------------------------------------------------------------------------------------

#4. Faça um programa que leia e imprima um número inteiro.

numero = int(input('digite um numero:'))
print(f'{numero}')

#----------------------------------------------------------------------------------------------------------------------------

#5. Faça um programa que leia dois números reais e os imprima.

nn1 = float(input('digite um primeiro numero:'))
nn2 = float(input('digite o segundo numero:'))
 
print(f'{nn1}\t{nn2}') 
print(f'{nn1}') 
print(f'{nn2}') 

#----------------------------------------------------------------------------------------------------------------------------

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.

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

nome = input('digite o seu nome:')
print(nome)
endereco = input('digite seu indereço: ') 
print(endereco)
telefone = input('disce o seu numero de telefone: ')
print(telefone)



#----------------------------------------------------------------------------------------------------------------------------

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.

numero1 = int(input('digite um numero inteiro:'))
numero2 = int(input('digite outro numero inteiro: '))

subtracao = numero1 + numero2

print(f'o resultado sera {subtracao}')


#----------------------------------------------------------------------------------------------------------------------------

#9. Faça um programa que leia um número real e imprima ¼ deste número.

numero_real = float(input("Digite um número real: "))
um_quarto = numero_real / 4

print(f"1/4 de {numero_real} é: {um_quarto}")

#----------------------------------------------------------------------------------------------------------------------------
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.

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

numero1 = float(input('digite um numero em real '))

quad = (numero1**2)

#print(f'o quadradado sera {quad}')




#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.


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

    
    
celsius = float(input("Digite a temperatura em graus Celsius: "))
conversao = fahrenheit = (9 * celsius + 160) / 5
print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")



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

# Função para calcular a distância e litros consumidos
def calcular_viagem(tempo, velocidade_media):
    # Fórmula para calcular a distância
    distancia = tempo * velocidade_media

    # Fórmula para calcular os litros consumidos
    litros_consumidos = distancia / 12

    return distancia, litros_consumidos

# Entrada do usuário para o tempo e a velocidade média
tempo = float(input("Digite o tempo decorrido na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média do carro (em km/h): "))

# Chamada da função para calcular a distância e litros consumidos
distancia, litros_consumidos = calcular_viagem(tempo, velocidade_media)

# Exibição do resultado
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Litros de combustível consumidos: {litros_consumidos:.2f} litros")

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.


 # Função para calcular o valor da prestação em atraso
def calcular_prestacao_atrasada(valor_prestacao, taxa_juros, periodo_atraso):
     Fórmula para calcular juros simples
    juros = valor_prestacao * (taxa_juros / 100) * periodo_atraso

     Valor da prestação acrescido dos juros
    prestacao_atrasada = valor_prestacao + juros

    return prestacao_atrasada, juros

 
valor_prestacao = float(input("Digite o valor da prestação vencida: "))
taxa_juros = float(input("Digite a taxa periódica de juros (em porcentagem): "))
periodo_atraso = int(input("Digite o período de atraso em meses: "))
 Chamada da função para calcular a prestação em atraso
prestacao_atrasada, juros = calcular_prestacao_atrasada(valor_prestacao, taxa_juros, periodo_atraso)

# Exibição do resultado
print(f"Valor da prestação atrasada: R$ {prestacao_atrasada:.2f}")
print(f"Período de atraso: {periodo_atraso} meses")
print(f"Juros cobrados pelo período de atraso: R$ {juros:.2f}")
print(f"Valor total da prestação acrescido dos juros: R$ {prestacao_atrasada:.2f}")

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

real_dolar = 4.95
reais = float(input('digite o valor em real '))

conversao = reais * real_dolar
print(f'a valor em dolar sera {conversao} ')



# def q10():
