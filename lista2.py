#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
#def q01():

  #  num1 = int(input('digite um valor eniteiro '))
   # num2 =  int(input('digite um valor eniteiro '))
    #soma = num1 + num2

    #if soma > 10:
       #    print(f'maior que 10')
   

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
#def q02():

    #num1 = int(input('digite o primeiro numero '))
 #   num2 = int(input('digite o segundo numero '))

  #  soma = num1 + num2 

   # if soma >20:
    #    print(f'resultado: {soma+8}')
    #else:
     #   print(f'resultado: {soma + 5 }') 
#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
#def q03():
 #   n = int(input('digite um numero '))


  #  if n % 3 :
   #     print('e divisivel ')
    #else:
     #   print('nao e divisivel')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
#def q04():

 #   numero = int(input('digite um numero'))

  #  if numero % 5 == 0:
   #     print(f'{numero }nao divisivel por 5')
    #else:
     #   print(f'{numero}  e divisivel por 5 ')


#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
#def q05():

 #   numero = int(input('digite um numero'))

  #  if numero % 7 == 0 and numero % 3 == 0:
   #     print(f'{numero } e divisivel por 7 ou 3 ')
    #else:
     #   print(f'{numero}  nao e divisivel por 7 ou 3 ')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
#ef q06():


   # salario_bruto = float(input('digite o valor salarial'))
   # prestacao = float(input('digite a prestacao '))

   # limite_prestacao = salario_bruto * 0.3

   # if prestacao <= limite_prestacao:
    #    print('emprestimo concedido') 
    #else:
    #    print('emprestimo nao concedido')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
#def q07():
#
 #   numero = int (input('digite um numero '))
#
 #   if numero >= 20 and numero <= 50:
  #      print(f'{numero } esta compreendido')
   # else:
    #    print (f'{numero} nao e ta compeendido')     

#8. Faça um programa que leia um número e imprima uma das mensagens:
  # "Maior do que 20", "Igual a 20"ou "Menor do que 20".
#def q08():

 #   n1 = int(input('digite um numero: '))

  #  if n1 > 20:
   #     print(f'{n1} maior do que 20 ')
    #elif n1 == 20:
   #     print(f'{n1} igual a 20')
    #else:
    # 3   print(f'{n1} menor doque 20')


#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
#def q09():
ano_nascimento = int(input('digite a data de nascimento'))

 #   ano_nascimento = int(input('digite o ano de nascimento'))
  #  ano_atual = int(input('digite o ano atual'))


 #   idade = ano_atual-ano_nascimento 
#
 #   if ano_nascimento >= 2024:
  #3      print(f'a idade e -> {idade } e esta valida')
   # else:
    #    print(f'a idade e -> {idade} e nao e valida')



#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
#def q10():
#outro exemplo 


 #   n1 = int(input('digite uma numero '))
  #  n2 = int(input('digite uma numero '))
   # n3 = int(input('digite uma numero '))

    #umeros = [n1,n2,n3]
    #numeros_ordeneados = sorted(numeros)

    #print('numeros ordenados ',numeros_ordeneados)


#11. Faça um programa que leia 3 números e imprima o maior deles.
#def q11():

 #   n1 = int(input('digite uma numero '))
  #  n2 = int(input('digite uma numero '))
   # n3 = int(input('digite uma numero '))

    #numeros = [n1,n2,n3]
    #maior_numero = max(numeros)

    #print('O maior numero e  ',maior_numero)


#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
#def q12():

 #   idade = int(input('digite a idade '))


  #  if idade >= 65:
   # print(f'{idade} maior que 65')
    #elif idade >=18  :
    #print(f'{idade} de maior ')
    #elif idade <= 18 :
    #print(f'{idade} de menor')


#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
#nome = input("Digite o nome do aluno: ")
#nota_prova1 = float(input("Digite a nota da prova 1: "))
#nota_prova2 = float(input("Digite a nota da prova 2: "))

#media = (nota_prova1 + nota_prova2) / 2

#print("\nNome do Aluno:", nome)
#print("Nota da Prova 1:", nota_prova1)
#print("Nota da Prova 2:", nota_prova2)
#print("Média das Notas:", media)

#if media >= 7:
 #   print("Situação: Aprovado")
#elif media < 3:
 #   print("Situação: Reprovado")
#else:
#    print("Situação: Em Prova Final")



#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

#salario = float(input("Digite o salário da pessoa: "))


#if salario <= 600.00:
 #   desconto_inss = 0.00  
#elif salario <= 1200.00:
 #   desconto_inss = salario * 0.20  
#elif salario <= 2000.00:
 #   desconto_inss = salario * 0.25  
#else:
 #   desconto_inss = salario * 0.30  

#print("\nSalário: R$ {:.2f}".format(salario))
#print("Desconto do INSS: R$ {:.2f}".format(desconto_inss))

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#valor_compra = float(input("Digite o valor do produto: "))

#if valor_compra < 20.00:
 #   percentual_lucro = 0.45 
#else:
 #   percentual_lucro = 0.30  

#valor_venda = valor_compra * (1 + percentual_lucro)

#print("\nValor de Compra: R$ {:.2f}".format(valor_compra))
#print("Percentual de Lucro: {}%".format(int(percentual_lucro * 100)))
#print("Valor de Venda: R$ {:.2f}".format(valor_venda))

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#idade = int(input("Digite a idade do nadador: "))


#if idade >= 5 and idade <= 7:
 #   categoria = "Infantil A"
#elif idade >= 8 and idade <= 10:
 #   categoria = "Infantil B"
#elif idade >= 11 and idade <= 13:
 #   categoria = "Juvenil A"
#elif idade >= 14 and idade <= 17:
 #   categoria = "Juvenil B"
#else:
 #   categoria = "Sênior"

#print("\nIdade do Nadador: {}".format(idade))
#print("Categoria: {}".format(categoria))

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#nome = input("Digite o nome da pessoa: ")
#idade = int(input("Digite a idade da pessoa: "))


#if idade <= 10:
 #   valor_plano = 30.00
#elif idade <= 29:
#    valor_plano = 60.00
#elif idade <= 45:
 #   valor_plano = 120.00
#elif idade <= 59:
 #   valor_plano = 150.00
#elif idade <= 65:
 #   valor_plano = 250.00
#else:
 #   valor_plano = 400.00


#print("\nNome: {}".format(nome))
#print("Idade: {}".format(idade))
#print("Valor do Plano: R$ {:.2f}".format(valor_plano))


#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))


#if 1 <= numero_mes <= 12:
 
    #meses = [
        #"Janeiro", "Fevereiro", "Março", "Abril",
        #"Maio", "Junho", "Julho", "Agosto",
        #"Setembro", "Outubro", "Novembro", "Dezembro"
   # ]

 
    #nome_mes = meses[numero_mes - 1]

    # Exibe o resultado
    #print(f"O mês correspondente ao número {numero_mes} é {nome_mes}.")
#else:
    #print("Erro: Não existe mês com este número. Por favor, insira um número entre 1 e 12.")
 
 #-------------------------------------------------------------------------------------------------------------
#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada"


#ponto_j1 = int(input('informe os pontos obtidos do joagador 1 '))
#ponto_j2 = int(input('informe os pontos obtidos do joagador 2 '))
#ponto_j3 = int(input('informe os pontos obtidos do joagador 3 '))


#soma_pontos = ponto_j1 + ponto_j2 + ponto_j3


#if(ponto_j3 > ponto_j2):
#        aux = ponto_j3
#        ponto_j3 = ponto_j2
#        ponto_j2 = aux

#if(ponto_j2 > ponto_j1):
#        aux = ponto_j2
#        ponto_j2 = ponto_j1
#        ponto_j1 = aux

#if(ponto_j3 > ponto_j2):
#        aux = ponto_j3
#        ponto_j3 = ponto_j2
#        ponto_j2 = aux

#print('pontos em ordem decrescente',ponto_j1,'-',ponto_j2,'-',ponto_j3)        


#if soma_pontos > 100:
#    media = soma_pontos/3 
#    print(f'equipe classificada, media de pontos {media}')
#else:
#    print ('equipe desclassificada ')

#---------------------------------------------------------------------------------------------------------------

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#saldo_medio = float(input("Digite o saldo médio do cliente: "))


#if saldo_medio >= 0 and saldo_medio <= 500:
 #   percentual_credito = 0
#elif saldo_medio <= 1000:
  #  percentual_credito = 0.3
#elif saldo_medio <= 3000:
 #   percentual_credito = 0.4
#else:
 #   percentual_credito = 0.5


#valor_credito = saldo_medio * percentual_credito

#print(f"Saldo Médio: R$ {saldo_medio:.2f}")
#print(f"Valor do Crédito: R$ {valor_credito:.2f}")


#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#nome_livro = input("Digite o nome do livro: ")
#tipo_usuario = input("Digite o tipo de usuário (professor ou aluno): ")

#if tipo_usuario.lower() == "professor":
 #  total_dias = 10
#elif tipo_usuario.lower() == "aluno":
 #   total_dias = 3
#else:
 #   total_dias = 0 

#print("\nRecibo:")
#print(f"Nome do livro: {nome_livro}")
#print(f"Tipo de usuário: {tipo_usuario}")
#print(f"Total de dias para devolução: {total_dias} dias")


#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.


#percurso_km = float(input("Digite o percurso em quilômetros: "))
#tipo_carro = input("Digite o tipo do carro (A, B ou C): ")

#consumo_carro_A = 12 
#consumo_carro_B = 9   
#consumo_carro_C = 8   

#if tipo
#if tipo_carro.upper() == "A":
#    consumo_estimado = percurso_km / consumo_carro_A
#elif tipo_carro.upper() == "B":
#    consumo_estimado = percurso_km / consumo_carro_B
#elif tipo_carro.upper() == "C":
#    consumo_estimado = percurso_km / consumo_carro_C
#else:
#    print("Tipo de carro inválido. Por favor, insira A, B ou C.")
#    consumo_estimado = 0

#if consumo_estimado > 0:
#    print(f"\nConsumo estimado de combustível: {consumo_estimado:.2f} litros.")


#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal


#prato = input("Escolha o prato (Vegetariano, Peixe, Frango, Carne): ")
#sobremesa = input("Escolha a sobremesa (Abacaxi, Sorvete diet, Mousse diet, Mousse chocolate): ")
#bebida = input("Escolha a bebida (Chá, Suco de laranja, Suco de melão, Refrigerante diet): ")


#calorias_prato = {"vegetariano": 180,"peixe": 230,"frango": 250,"carne": 350 }
#calorias_sobremesa = { "abacaxi": 75, "sorvete diet": 110,"mousse diet": 170, "mousse chocolate": 200 }
#calorias_bebida = { "cha": 20, "suco de laranja": 70,"suco de melão": 100, "refrigerante diet": 65 }
    


#if prato in calorias_prato and sobremesa in calorias_sobremesa and bebida in calorias_bebida:
   
#    total_calorias = calorias_prato[prato] + calorias_sobremesa[sobremesa] + calorias_bebida[bebida]

#    print(f"\nA quantidade total de calorias da refeição é: {total_calorias} calorias.")
#else:
#    print("Opção inválida. Por favor, escolha pratos, sobremesas e bebidas válidos.")

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

placa = input('placa do veiculo')
mes = placa[len(placa)-1]

if mes





#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
 
 
 
 
 



 
  #sair do progama = quit()                #python3 -i lista2.py


#def q01():

