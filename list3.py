'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''

def exemploPara():
    for x in range(10):
        print(x) # imprime de 0 a 9

def exemploEnquanto():
    x = 0
    while x < 10:
        print(x)
        x += 1 # é a mesma coisa que x = x + 1

#1.Faça um programa que imprima todos os números de 1 até 100.
def q01():
    for x in range(1,101):
        print(x, end = " ")

#2. Faça um programa que imprima todos os números pares de 100 até 1.
def q02():
    for x in range(100,0,-2):
        print(x, end = " ")

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def q03():
    for i in range(500,0,-5):
         print(i, end = " ")

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.
def q04():
    nomes = []
    idades = []
    sexos = []

   
    for i in range(20):

        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade de {} : ".format(nome)))
        sexo = input("Digite o sexo de {} (M/F): ".format(nome)).upper()

        nomes.append(nome)
        idades.append(idade)
        sexos.append(sexo)

   
    print("\nPessoas do sexo masculino com mais de 21 anos:")
    for i in range(20):
        if sexos[i] == "M" and idades[i] > 21:
            print(nomes[i])


#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q05():
    soma = 0
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    #5*4 = 20 (4+4+4+4+4)
    for x in range(num1):
        soma += num2
    print(f'{num1} * {num2} = {soma}')

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21
def q06():
    anterior = 0
    atual = 1
    print(atual, end = " ")
    for x in range(19):
        proximo = anterior + atual
        print(proximo, end = " ")
        anterior = atual
        atual = proximo


#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
def q07():
    for i in range(15):
        nome = input('qual seu nome')
        nota1 = int(input('digite a primeira nota'))
        nota2 = int(input('digite a segunda nota'))

        media = nota1 + nota2 / 2

        print(f' O aluno{nome} com a notas {nota1} e {nota2} tem a media de {media}')


#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q08():
    dados_pessoas = 0

    for i in range(10):
        nome = input('digite o seu nome:')
        salario_bruto = float(input('qual o seu salario:'))

        print({"nome": nome, "salario": salario_bruto})

        if salario_bruto < 1300:
            print('isento')
        elif salario_bruto < 2300:
            print(f'10% do salário bruto: R${salario_bruto * 0.1:.2f}')   
        else:
            print(f'15% do salário bruto: R${salario_bruto * 0.15:.2f}')     


#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.
def q09():
    qtdePessoasExcelente = 0
    somaIdadeExcelente = 0
    qtdePessoasRegular = 0
    qtdePessoasBom = 0
    qtdeTotalPessoas = int(input('Número de Pessoas: '))
    for x in range(qtdeTotalPessoas):
        idade = int(input('Idade: '))
        opiniao = int(input('Opinião ([3]-Excelente - [2]-Bom - [1]-Regular): '))
        match(opiniao):
            case 1: qtdePessoasRegular += 1
            case 2: qtdePessoasBom += 1
            case 3:
                qtdePessoasExcelente +=1
                somaIdadeExcelente += idade
            case _: print('Opção Inválida!')
    print(f'Média idade excelente: {somaIdadeExcelente/qtdePessoasExcelente}')
    print(f'Qtde de pessoas regular: {qtdePessoasRegular}')
    print(f'% de pessoas que responderam bom: {qtdePessoasBom/qtdeTotalPessoas*100}%')

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
def q10():
    num_paises = 30
    num_jogadores_por_time = 2

    for pais in range(1, num_paises + 1):
        print(f"\nPaís {pais}:")

        peso_total_time = 0
        idade_total_time = 0
        peso_mais_pesado = 0
        atleta_mais_pesado = ""
        idade_mais_jovem = float('inf')
        atleta_mais_jovem = ""
        for jogador in range(1, num_jogadores_por_time + 1):
            peso = float(input(f"Informe o peso do jogador {jogador} (em kg): "))
            idade = int(input(f"Informe a idade do jogador {jogador}: "))

        peso_total_time += peso
        idade_total_time += idade

        if peso > peso_mais_pesado:
            peso_mais_pesado = peso
            atleta_mais_pesado = f"Jogador {jogador}"

        if idade < idade_mais_jovem:
            idade_mais_jovem = idade
            atleta_mais_jovem = f"Jogador {jogador}"

    peso_medio_time = peso_total_time / num_jogadores_por_time
    idade_medio_time = idade_total_time / num_jogadores_por_time

    print(f"Peso médio do time: {peso_medio_time:.2f} kg")
    print(f"Idade média do time: {idade_medio_time:.2f} anos")
    print(f"Atleta mais pesado: {atleta_mais_pesado} com {peso_mais_pesado} kg")
    print(f"Atleta mais jovem: {atleta_mais_jovem} com {idade_mais_jovem} anos")

    peso_total_geral = peso_total_time * num_paises
    idade_total_geral = idade_total_time * num_paises

    peso_medio_geral = peso_total_geral / (num_paises * num_jogadores_por_time)
    idade_medio_geral = idade_total_geral / (num_paises * num_jogadores_por_time)

    print("\nMédia geral de todos os participantes:")
    print(f"Peso médio: {peso_medio_geral:.2f} kg")
    print(f"Idade média: {idade_medio_geral:.2f} anos")


            
#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    contagem_numeros_entre_100_200 = 0

    while True:
        numero = int(input("Digite um número (ou 0 para sair): "))
    
        if numero == 0:
            break
    
        if 100 <= numero <= 200:
            contagem_numeros_entre_100_200 += 1

        print(f"\nQuantidade de números entre 100 e 200: {contagem_numeros_entre_100_200}")

    



#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():
    populacao_a = 5000000
    taxa_natalidade_a = 0.03
    populacao_b = 7000000
    taxa_natalidade_b = 0.02
    anos = 0
    while populacao_a <= populacao_b:
        populacao_a *= 1 + taxa_natalidade_a
        populacao_b *= 1 + taxa_natalidade_b
        anos += 1
        print(f"Levará {anos} anos para a população do país A ultrapassar a população do país B.")


#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2
def q13():
    total_consumo_residencial = 0
    total_consumo_industrial = 0
    total_consumo_comercial = 0
    total_custo = 0
    consumo_tipos_1_e_2 = 0

    while True:
        num_consumidor = int(input('qual o numero do consumidor (para encerrar o progama digite 0)'))

        if num_consumidor == 0 :
            break
        
        consumo_kwh = float(input('digite o consumo gastos em kwh '))
        tipo_consumidor = int(input("escolha o tipo de consumidor (1-residencial, 2-comercial, 3-industrial): "))
    
        if tipo_consumidor == 1 or tipo_consumidor == 2:
            consumo_tipos_1_e_2 += 1
    
        if tipo_consumidor == 1:
            preco_kwh = 0.3
            total_consumo_residencial += consumo_kwh
        elif tipo_consumidor == 2:
            preco_kwh = 0.5
            total_consumo_comercial += consumo_kwh
        elif tipo_consumidor == 3:
            preco_kwh = 0.7
            total_consumo_industrial += consumo_kwh
        else:
            print("Tipo de consumidor inválido. tente novamente.")


        custo_consumidor = preco_kwh * consumo_kwh
        total_custo += custo_consumidor 

    if consumo_tipos_1_e_2 != 0:
        media_consumo_tipos_1_e_2 = (total_consumo_comercial + total_consumo_residencial) / consumo_tipos_1_e_2
    else:
        media_consumo_tipos_1_e_2 = 0 

    print(f'\n O custo total de cada consumidor e : R$ {total_custo}')    
    print(f' o total de consumo residencial :{total_consumo_residencial} KWH')
    print(f' o total de consumo comercial :{total_consumo_comercial} KWH')
    print(f' o total de consumo indrustrial :{total_consumo_industrial} KWH')
    print(f"Média de consumo dos tip os 1 e 2: {media_consumo_tipos_1_e_2:.2f} kWh")

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n
def q14():
    n = int(input("Digite um, numero:"))

    for i in range(1,n):
        resultado = (i*n)
        n = resultado
        
    print (resultado)


#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos
def q15():
    pessoas_com_21 = 0 
    pessoas_com_50 = 0

 
        
    while True:
        idade = int(input('digite a sua idade '))
        if idade < 1:
            break

        if idade < 21:
            pessoas_com_21 += 1
        elif idade > 50:
            pessoas_com_50 += 1
            
        print(f'pessao co mais de 50 anos sao : {pessoas_com_21}')
        print(f'pessoas com 21 anos sao : {pessoas_com_50}')       


#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão
def q16():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    dividendo = num1
    divisor = num2
    quociente = dividendo/divisor
    resto = dividendo%divisor

    print("O dividendo é: ", dividendo)
    print("O divisor é: ", divisor)
    print("O quociente é: ", quociente)
    print("E o resto é: ", resto)
#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.
def q17():
    pedidos = []

    while True:
        numero_pedido = input("Digite o número do pedido (ou 0 para sair): ")
        if numero_pedido == '0':
            break

        data_pedido = input("Digite a data do pedido (dia/mês/ano): ")
        preco_unitario = float(input("Digite o preço unitário: "))
        quantidade = int(input("Digite a quantidade: "))

        total_pedido = preco_unitario * quantidade

        pedido = {
            'numero_pedido': numero_pedido,
            'data_pedido': data_pedido,
            'preco_unitario': preco_unitario,
            'quantidade': quantidade,
            'total_pedido': total_pedido
        }

        pedidos.append(pedido)

    valor_total = sum(pedido['total_pedido'] for pedido in pedidos)
    print(f"O valor total da compra é: R${valor_total:.2f}")

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário di;gite 0 (zero) como
#número da conta.
def q18():
    total_faturado = 0

    while True:
        nome_cliente = input("Digite o nome do cliente (ou 0 para sair): ")
        if nome_cliente == '0':
            break

        numero_conta = input("Digite o número da conta: ")
        numero_dias = int(input("Digite o número de dias de estadia: "))

        preco_diaria = 30.00
        taxa_servico = 15.00 
        if numero_dias < 10:
            15.00
        else:
            8.00
        conta_cliente = numero_dias * preco_diaria + taxa_servico

        total_faturado += conta_cliente

        print(f"\nCliente: {nome_cliente}")
        print(f"Número da conta: {numero_conta}")
        print(f"Conta: R${conta_cliente:.2f}\n")
        print(f"\nTotal faturado pela pousada: R${total_faturado:.2f}")

#19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado comnota >= 7.0
def q19():
    total_alunos_aprovados = 0
    total_turmas = int(input("Digite o número total de turmas: "))

    for turma in range(1, total_turmas + 1):
        total_alunos_turma = int(input(f"Digite o número de alunos da turma {turma}: "))
        soma_notas = 0
        alunos_aprovados_turma = 0
        for aluno in range(1, total_alunos_turma + 1):
            nota = float(input(f"Digite a nota do aluno {aluno} da turma {turma}: "))
            soma_notas += nota
            if nota >= 7.0:
                alunos_aprovados_turma += 1

    media_turma = soma_notas / total_alunos_turma
    percentual_reprovados_turma = 100 - (alunos_aprovados_turma / total_alunos_turma) * 100

    total_alunos_aprovados += alunos_aprovados_turma

    print(f"\nTurma {turma}:")
    print(f"Quantidade de alunos aprovados: {alunos_aprovados_turma}")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Percentual de reprovados: {percentual_reprovados_turma:.2f}%\n")

    percentual_total_reprovados = 100 - (total_alunos_aprovados / (total_alunos_turma * total_turmas)) * 100

    print(f"\nTotal de alunos aprovados em todas as turmas: {total_alunos_aprovados}")
    print(f"Percentual total de reprovados: {percentual_total_reprovados:.2f}%")


#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.
def q20():
    cont_fluminense = 0
    cont_botafogo = 0
    cont_flamengo = 0
    cont_vasco = 0
    outros_times = 0
    botafogo_salario = 0
    n_pess_rio = 0
    n_pess_niteroi = 0

    while True:
        print(' Digite o número correspondente ao seu time de coração:')
        print("1 - Fluminense")
        print("2 - Botafogo")
        print("3 - Vasco")
        print("4 - Flamengo")
        print("5 - Outros")
        times = int(input('digite o nunero:'))
        

        if times == 0 :
            break

        if times == 1:
            cont_fluminense += 1
            localizacao = int(input("Você mora em qual cidade? (1 - RJ, 2 - Niterói, 3 - Outros): "))
            if localizacao == 2:
                n_pess_niteroi += 1 
        elif times == 2:
            cont_botafogo += 1
            salario = float(input("Qual é o seu salário? "))
            botafogo_salario += salario
        elif times == 3:
            cont_vasco += 1 
            localizacao = int(input("Você mora em qual cidade? (1 - RJ, 2 - Niterói, 3 - Outros): "))
            if localizacao == 1 and times != 3:
                n_pess_rio +=  1
        elif times == 4 :
            cont_flamengo += 1
            location_choice = int(input("Você mora em qual cidade? (1 - RJ, 2 - Niterói, 3 - Outros): "))
            if localizacao == 1  and times != 4:
                n_pess_rio += 1
        else:
            outros_times += 1 
    print("Número de torcedores por clube:")
    print(f"Fluminense:{cont_fluminense}")
    print(f"Botafogo:{cont_vasco}")
    print(f"Vasco:{cont_vasco}")
    print(f"Flamengo:{cont_flamengo}")
    print(f"Outros:{outros_times}")

    if cont_botafogo > 0:
        media_salarial = botafogo_salario / cont_botafogo
        print(f'media salarial dos torcedores do botafogo e :{media_salarial}') 
    else:
        print('Não ha torcedores do Botafogo')


    print(f'Número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes:{n_pess_rio}')
    print(f'Número de pessoas de Niterói torcedoras do Fluminense:{n_pess_niteroi}')

#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.
def q21():
    gastos_acima_200 = 0
    alunos_renda_maior_fml = 0
    total_alunos = 0

    while True:
        renda_pessoal = float(input('digite a sua renda pessoal:'))
        
        if renda_pessoal == 0:
            break
        
        renda_familiar = float(input('qua a sua renda familiar:'))
        custo_alimentação = float(input ('quanto foi o seu custo em alimentação:'))
        custo_em_outras_dispesas = float(input('qual o foi o seu custo em outras dispesas: '))
        total_alunos += 1

        if gastos_acima_200 > 200:
            gastos_acima_200 += 1

        if renda_pessoal > renda_familiar:
            alunos_renda_maior_fml += 1

        custo_alimentação += 1
        custo_em_outras_dispesas +=1


    p_alunos_acima_200 = (gastos_acima_200/total_alunos) * 100
    p_custo_alimentação = (custo_alimentação/total_alunos) * 100
    p_custo_em_outras_dispesas = (custo_em_outras_dispesas/total_alunos) * 100
    p_renda_maior_fml = (alunos_renda_maior_fml/total_alunos) * 100

    print(f'A porcentagem de alunos que gasta acima de 200 R$ são {p_alunos_acima_200:.2f}%')
    print(f'A porcentagem de alunos que gastam em alimentação são {p_custo_alimentação:.2f}%')
    print(f'A porcentagem de alunos que gastam em outas dispesas são {p_custo_em_outras_dispesas:.2f}%')
    print(f'A porcentagem com renda maior que a da familia são {p_renda_maior_fml:.2f}%')
    
    #precisa arrumar esse codigo 



#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.
def q22():
    total_recursos = 0
    maior_numero_multas = 0
    carteira_maior_multas = None
    
    while True:
        numero_carteira = int(input("Digite o número da carteira de motorista (ou 0 para encerrar): "))
        if numero_carteira == 0:
            break
        
        numero_multas = int(input("Digite o número de multas: "))
        
        if numero_multas > maior_numero_multas:
            maior_numero_multas = numero_multas
            carteira_maior_multas = numero_carteira 
            
            valor_total_multas = 0
            for i in range(numero_multas):
                valor_multa = float(input(f"Digite o valor da multa {i+1}: "))
                valor_total_multas += valor_multa
                total_recursos += valor_total_multas
                print(f"O valor da dívida para o motorista da carteira {numero_carteira} é R${valor_total_multas:.2f}\n")
    
    print(f"Total de recursos arrecadados: R${total_recursos:.2f}")
    if carteira_maior_multas is not None:
        print(f"O motorista com maior número de multas possui a carteira número {carteira_maior_multas}.")

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.
def q23():
    feminino_mais_alta = None
    altura_max_feminino = 0.0
    masculino_mais_pesado = None
    peso_max_masculino = 0.0
    soma_idades = 0
    contador_atletas = 0
    
    # Loop para ler informações de múltiplos atletas
    while True:
        nome = input("Digite o nome do atleta (ou '@' para sair): ")
        
       
        if nome == '@':
            break
        
        sexo = input("Digite o sexo do atleta (M/F): ")
        idade = int(input("Digite a idade do atleta: "))
        peso = float(input("Digite o peso do atleta (kg): "))
        altura = float(input("Digite a altura do atleta (m): "))

        
        soma_idades += idade
        contador_atletas += 1
        
        
        if sexo == 'F':
            if altura > altura_max_feminino:
                altura_max_feminino = altura
                feminino_mais_alta = nome
        elif sexo == 'M':
            if peso > peso_max_masculino:
                peso_max_masculino = peso
                masculino_mais_pesado = nome
        
    
    if contador_atletas > 0:
        media_idade = soma_idades / contador_atletas
    else:
        media_idade = 0
    
    
    print(f"\nAtleta feminina mais alta: {feminino_mais_alta} ({altura_max_feminino}m)")
    print(f"Atleta masculino mais pesado: {masculino_mais_pesado} ({peso_max_masculino}kg)")
    print(f"Média de idade dos atletas: {media_idade:.1f} anos")
   
#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração
def q24():
    total_combustivel = 0
    
    while True :

        velocidade = float(input("digite o valor da velocidade "))

        if velocidade == 0:
            break
        
        tempo = float(input("Informe o tempo de viagem neste trecho (horas): "))
        
        distancia = velocidade * tempo
        combustivel_gasto = distancia / 10
        
        total_combustivel += combustivel_gasto
        
        print(f"Distância percorrida neste trecho: {distancia:.2f} km")
        print(f"Combustível consumido neste trecho: {combustivel_gasto:.2f} litros")   
    
    print(f"Total de combustível consumido na viagem: {total_combustivel:.2f} litros")

        






#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.
def q25():
    total_imposto = 0
    total_isentos = 0

    while True:
        
        cic = input("Informe o CIC do contribuinte (ou 0 para encerrar): ")
        
        
        if cic == "0":
            break
        
        dependentes = int(input("Informe o número de dependentes: "))
        renda_bruta = float(input("Informe a renda bruta anual (R$): "))
        
       
        abatimento = 600 * dependentes
        renda_liquida = renda_bruta - abatimento
        
        
        if renda_liquida <= 1000:
            imposto = 0
            total_isentos += 1
        elif 1001 <= renda_liquida <= 5000:
            imposto = renda_liquida * 0.15
        else:
            imposto = renda_liquida * 0.25
        
        
        total_imposto += imposto
        
       
        print(f"CIC: {cic}, Imposto a ser pago: R${imposto:.2f}")
    
    
    print(f"Total de imposto arrecadado: R${total_imposto:.2f}")
    print(f"Número de contribuintes isentos: {total_isentos}")

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.
def q26():
    
    audiencia = {4: 0, 5: 0, 7: 0, 12: 0}
    total_pessoas = 0

    while True:
        
        canal = int(input("Informe o número do canal (4, 5, 7, 12) ou 0 para encerrar: "))
        
        if canal == 0:
            break
        
        if canal not in audiencia:
            print("Canal inválido. Informe um dos seguintes canais: 4, 5, 7, 12.")
            continue
        
        pessoas = int(input("Informe o número de pessoas assistindo: "))
        
        
        audiencia[canal] += pessoas
        total_pessoas += pessoas
    
    
    if total_pessoas > 0:
        print("\nPorcentagem de audiência por canal:")
        for canal, pessoas in audiencia.items():
            porcentagem = (pessoas / total_pessoas) * 100
            print(f"Canal {canal}: {porcentagem:.2f}%")
    else:
        print("Nenhuma audiência registrada.")


#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.
def q27():    
    melhor_cr = -1
    total_alunos = 0

    while True:
        
        matricula = int(input("Informe o número da matrícula (1 a 5000) ou fora deste intervalo para encerrar: "))
        
        
        if matricula < 1 or matricula > 5000:
            break
        
        qtd_disciplinas = int(input("Informe a quantidade de disciplinas cursadas: "))
        
     
        soma_notas = 0
        
        
        for i in range(qtd_disciplinas):
            nota = float(input(f"Informe a nota da disciplina {i + 1}: "))
            soma_notas += nota
        
        
        cr = soma_notas / qtd_disciplinas
        
       
        if qtd_disciplinas >= 5 and cr > melhor_cr:
            melhor_cr = cr
        
       
        total_alunos += 1

     
        print(f"Matrícula: {matricula}, CR: {cr:.2f}")

  
    if melhor_cr >= 0:
        print(f"\nO melhor CR entre os alunos que cursaram 5 ou mais disciplinas: {melhor_cr:.2f}")
    else:
        print("\nNenhum aluno cursou 5 ou mais disciplinas.")



#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.
def q28():
    total_pessoas = 0
    total_idade_maior_50 = 0
    total_altura_10_20 = 0
    soma_altura_10_20 = 0
    total_peso_inferior_40 = 0

    while True:
        
        idade = int(input("Informe a idade (ou um número negativo para encerrar): "))
        
        
        if idade == 0:
            break
        
        altura = float(input("Informe a altura (em metros): "))
        peso = float(input("Informe o peso (em quilos): "))
        
        total_pessoas += 1

        
        if idade > 50:
            total_idade_maior_50 += 1
        
        if 10 <= idade <= 20:
            total_altura_10_20 += 1
            soma_altura_10_20 += altura
        
        if peso < 40:
            total_peso_inferior_40 += 1

   
    if total_altura_10_20 > 0:
        media_altura_10_20 = soma_altura_10_20 / total_altura_10_20
    else:
        media_altura_10_20 = 0

    
    if total_pessoas > 0:
        porcentagem_peso_inferior_40 = (total_peso_inferior_40 / total_pessoas) * 100
    else:
        porcentagem_peso_inferior_40 = 0

  
    print(f"\nQuantidade de pessoas com idade superior a 50 anos: {total_idade_maior_50}")
    print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_altura_10_20:.2f} metros")
    print(f"Porcentagem de pessoas com peso inferior a 40 quilos: {porcentagem_peso_inferior_40:.2f}%")


#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.
def q29():
    total_vendido = 0
    total_limpeza = 0
    total_alimentacao = 0
    total_higiene = 0

    while True:
      
        valor = float(input("Informe o valor da mercadoria (ou 0 para encerrar): "))
        
       
        if valor == 0:
            break
        
       
        codigo = input("Informe o código da mercadoria (L-limpeza, A-alimentação, H-higiene): ").upper()
        
       
        if codigo == 'L':
            total_limpeza += valor
        elif codigo == 'A':
            total_alimentacao += valor
        elif codigo == 'H':
            total_higiene += valor
        else:
            print("Código inválido. Tente novamente.")
            continue
        
        total_vendido += valor

 
    print(f"\nTotal vendido no dia: R${total_vendido:.2f}")
    print(f"Total vendido em produtos de limpeza: R${total_limpeza:.2f}")
    print(f"Total vendido em produtos de alimentação: R${total_alimentacao:.2f}")
    print(f"Total vendido em produtos de higiene: R${total_higiene:.2f}")


#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a idade
def q30():
    casados = 0
    solteiros = 0
    viuvas = 0
    idade_viuvas = 0
    desquitados_separados = 0
    total_pessoas = 0

    while True:
      
        idade = int(input("Informe a idade (ou um número negativo para encerrar): "))
        
       
        if idade == 0:
            break
        
        
        estado_civil = input("Informe o estado civil (C-casado, S-solteiro, V-viúvo, D-desquitado/separado): ").upper()
        
       
        if estado_civil == 'C':
            casados += 1
        elif estado_civil == 'S':
            solteiros += 1
        elif estado_civil == 'V':
            viuvas += 1
            idade_viuvas += idade
        elif estado_civil == 'D':
            desquitados_separados += 1
        
        total_pessoas += 1

   
    if viuvas > 0:
        media_idade_viuvas = idade_viuvas / viuvas
    else:
        media_idade_viuvas = 0

   
    if total_pessoas > 0:
        porcentagem_desquitados_separados = (desquitados_separados / total_pessoas) * 100
    else:
        porcentagem_desquitados_separados = 0

    
    print(f"Quantidade de pessoas casadas: {casados}")
    print(f"Quantidade de pessoas solteiras: {solteiros}")
    print(f"Média das idades das pessoas viúvas: {media_idade_viuvas:.2f}")
    print(f"Porcentagem de pessoas desquitadas ou separadas: {porcentagem_desquitados_separados:.2f}%")