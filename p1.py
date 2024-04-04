'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2024/1
Mensagem:   NOME COMPLETO DO ESTUDANTE
Anexo:      p1.py
'''

#1. Faça um programa que leia o valor unitário de um produto,
#   a quantidade desejada e imprima o valor total a pagar. (2,5pt)
def q01():

    produto = input('qual o produto que deseja:')
    valor = int(input('qual e o valor desse produto: '))
    quant = int(input('digite a quantidade que deseja: '))


    valor_unitario =  valor * quant

    print(f'o produto que voce escolheu foi : {produto}')
    print (f'O total a pagar desse produto sera de {valor_unitario:.2f}R$')

#2. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#   reprovação e as demais em prova final). (2,5pt)
def q02():
    nome = input('digite o seu nome ')
    nota1 = float(input('digite a sua primeira nota:'))
    nota2 = float(input('digite a sua segunda nota:'))
    
    media = nota1 + nota2 / 2

    if media >= 7:
        print('Aprovado')
    elif media > 3:
        print('Prova final')
    else:
        print('Reprovado')
#3. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)
def q03():
    while True:

        menu = int(input('escolha uma opção ===> [1],[2],[3],[0]  obs: para sair digite 0)'))

        if menu == 0:
           break    
        if menu == 1:
            print('CADRASTAR')
        elif menu == 2:
            print('EXCLUIR')
        elif menu == 3:
            print('PESQUISAR ')

#4. Faça um programa que calcule o retorno de um investimento. (2,5pt)
#   O programa deve solicitar do usuário o:
#   - valor que será investido;
#   - prazo do investimento (meses);
#   - juros mensal (juros composto).
def q04():

    valor_investido = float(input('qual sera o valor investido '))
    prazo = int (input('digite o prazo'))
    juros_mensal = int(input('digite o juros mensal'))

    investimento = (valor_investido + prazo ) / juros_mensal 


    print(f'O valor investido foi de {valor_investido}R$')
    print(f'com prazo de {prazo} meses ')
    print(f'com juros mensal de {juros_mensal:.2f}%')
    print (f'o retorno do investimento sera de {investimento}')