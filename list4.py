'''
Lista de Exercícios referentes a coleções em python
'''
#exemplo de coleções.
#lista = [1,4,10,2,3,3,4,'maria',True, 24.4]

#print(lista[4])
#-----------------------------------------
#lista.append(5)
#print(lista)
#-----------------------------------------
#lista.extend([9,10,11])
#print(lista)
#-----------------------------------------
#lista.insert(4,5)
#print(lista)

#for elemento in lista:
#    print(elemento)

#lista.clear()
#print(lista)

#lista2 = [3,7,1]
#lista2.sort()
#print(lista2)

#---------------------------------------------------------
#tupla = [0,1,2,3,[4,5,6]]


#tupla[4].clear() - remove tudo a lista

#tupla[4].remove(6)
#print(tupla)



#------------------------------------
#matriz

#matriz = [[1,3,5,7,98,1],[10,15,20],[30,40,50]]
#for linha in matriz:

 #   print(linha)
#print(matriz [1][])

#set 
#a = {0,1,2,3,4,5,6}
#b = {5,1,96,7,8,9}


#print(a|b)
#print(a-b)
#print(a&b)
#print(a^b)


#dicionaty
 
#clientes = {
  #  '65987654':'luis'
   # '65000234''kaka'
    #'65930912':'baba'
#}


#print(clientes['65987654'])
#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q01():
    numeros = []

    for i in range(15):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    numero_busca = int(input("Digite o número inteiro que deseja buscar na lista: "))

    if numero_busca in numeros:
        posicao = numeros.index(numero_busca)
        print(f"O número {numero_busca} foi encontrado na posição {posicao}.")
    else:
        print("Nao encontrado!")


def ex2():
    listas = []

    for i in range(15):
        listas.append(random.randrange(100))
    print(listas)
    busca = int(input('digite o numer a ser localizado'))
    try:
        posicao = listas.index(busca)
        print(f'posição do numero {busca}:{posicao} ')
    except ValueError:
        print('valor não encontrado')




#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q02():
    letras = []

    for i in  range (10):
        letra = int(input(f'digite a{i+1}° letra'))
        letras.append(letra)
    
    print('listagem numerada')

    for idx, letra in enumerate(letras, start=1):
        print(f"{idx}. {letra}")

def ex3():
    lista = []
    i  = 0

    for i in range(10):
        lista.append(chr(random.randrange(54,91)))
        print(f'{i}: {lista[i]}')
        i+=1
    



#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q03():
    numeros = []

    for i in range(15):
        numero = int(input ('digite o um numero '))
        numeros.append(numero)
    
    print('listagem numerada')

    for idx,num in enumerate (numeros, start=1):
        if num % 2 == 0:
            tipo = "par"
        else:
            tipo = "impar"
        print(f"{idx}. {num} - {tipo}")

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q04():
    numeros = []
    

    for i in range(8):
        numero = int(input(f'digite o {i+1}° numrero '))
        numeros.append(numero)

    print('numeros digitados na lista ')
    
    
    for num in numeros :
        print(num)

    multiplos_8 = 0

    for num in numeros:
        if num % 6 == 0:
            multiplos_8 += 1

    print(f'{multiplos_8}')

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q05():
    alunos = []

    for i in range(3):
        aluno = dict()
        aluno['nome'] = input('nome: ')
        aluno ['n1'] = float(input('nota 1: ' ))
        aluno ['n2'] = float(input('nota 2: ' ))
        aluno ['media'] = (aluno ['n1'] + aluno['n2'] ) / 2
        aluno ['situacao'] = 'APROVADO' if aluno ['media']>= 6 else 'REPROVADO'

        alunos.append(aluno)
    print ('NOME\tN1\tN2\tMEDIA\tSITUACAO')


    for a in alunos:
        print(f"{a['nome']}\t {a['n1']}\t {a['n2']} \t {a['media']}\t {a['situacao']}")


#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q06():
    salario_atual = []
    reajuste_salario = []

    for i in range(2):
        salario = float(input(f'digite o salario da {i+1}° pessoa '))
        salario_atual.append(salario)
        novo_salario = salario * 1.08
        reajuste_salario.append(novo_salario)
    
    print('\n listahem do salario')
    print('n° \t salario atual \t reajuste  ')
    for i in range(2):
        print(f'{i+1}\t R${salario_atual[i]:.2f}\t R${reajuste_salario[i]:.2f}') 

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q07():
    precos_compra  = []
    precos_venda = []

    lucro_menor_10 = 0
    lucro_entre_10_20 = 0
    lucro_maior_20 = 0


    for i in range(100):
        preco_compra = float(input(f"Digite o preço de compra da mercadoria {i+1}: "))
        preco_venda = float(input(f"Digite o preço de venda da mercadoria {i+1}: "))
        precos_compra.append(preco_compra)
        precos_venda.append(preco_venda)


    for i in range(100):
        lucro = (precos_venda[i] - precos_compra[i]) / precos_compra[i] * 100
        if lucro < 10:
            lucro_menor_10 += 1
        elif 10 <= lucro <= 20:
            lucro_entre_10_20 += 1
        else:
            lucro_maior_20 += 1

    print("\nResultados:")
    print(f"Mercadorias com lucro menor que 10%: {lucro_menor_10}")
    print(f"Mercadorias com lucro entre 10% e 20%: {lucro_entre_10_20}")
    print(f"Mercadorias com lucro maior que 20%: {lucro_maior_20}")




#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q08():

    for i in range(2):
        codigo = input("digite o codigo:  ")
        quantidade = int(input("qual a quantidade: "))
        valor_compra = float(input('qual o valor da compra:  '))
        valor_venda = float(input('qual o valor da venda: '))
        codigo_do_produto = {

            'quantidade':quantidade,
            'valor_compra':valor_compra,
            'valor_venda':valor_venda

        }
       

    for i in range(2):
        opcao = input('escolha uma opcao [1] ou [2]')
        if opcao == 'q':
            codigo = input("digite o codigo para buscar :  ")      
                if  not  codigo_do_produto:
                    print('codigo não cadastrado')
                else:

                    print('\ncodigo encontrado com sucesso  ')
        

                    print(f'codigo do produto : {codigo}')
                    print(f'quantidade do produto: {quantidade}')
                    print(f'O valor da compra : R$ {valor_compra}')
                    print(f'O valor da venda: {valor_venda}')
        else 


        
        





    

       # if not codigo_do_produto:
        #    print('o codigo do produto não foi encontrado')
        #else:

        
















#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.multiplos_de_seis = 0
   


#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.








#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.