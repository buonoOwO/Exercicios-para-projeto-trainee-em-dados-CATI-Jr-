"""

-------------------------------------------------------------------------------------

Exercício 1.1 - Criando Variáveis e Verificando Tipos

-------------------------------------------------------------------------------------

Crie variáveis para armazenar as seguintes informações:

Nome (string)
Idade (inteiro)
Altura (float)
É estudante (booleano)
Em seguida, use a função print() para exibir cada variável e seu tipo usando type().

"""

nome = 'Juliana'
idade = 22
altura = 1.62
estudante = True

print(f'Nome: {nome}, tipo: {type(nome)}')
print(f'Idade: {idade}, tipo: {type(idade)}')
print(f'Altura: {altura}, tipo: {type(altura)}')
print(f'É estudante: {estudante}, tipo: {type(estudante)}')


"""

-------------------------------------------------------------------------------------

Exercício 1.2 - Formulário de Cadastro

-------------------------------------------------------------------------------------

Crie um programa que solicite ao usuário:

Nome completo
Idade (converta para inteiro)
Altura em metros (converta para float)
Depois, exiba uma mensagem formatada com todas as informações coletadas.

"""

nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros: '))

print('Cadastro realizado com sucesso!')

print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Altura: {altura:.2f} metros')

"""
-------------------------------------------------------------------------------------

Exercício 1.3 - Calculadora de IMC

-------------------------------------------------------------------------------------
Crie um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.

A fórmula do IMC é: IMC = peso / (altura)²

O programa deve:

Solicitar o peso em quilogramas (float)
Solicitar a altura em metros (float)
Calcular o IMC
Exibir o resultado formatado com 2 casas decimais

"""

print('Por favor, digite as seguintes informações')

peso = float(input('Peso (quilogramas): '))
altura = float(input('Altura (metros): '))

imc = peso / (altura ** 2)

print(f'Seu IMC é: {imc:.2f}')

"""

-------------------------------------------------------------------------------------

Exercício 1.4 - Sistema de Cadastro Completo

-------------------------------------------------------------------------------------

Crie um sistema de cadastro que:

Solicite ao usuário:

Nome completo
CPF (apenas números, como string)
Data de nascimento (formato DD/MM/AAAA)
Salário (float)
É funcionário ativo? (True/False)
Adicione comentários explicativos no código

Exiba um relatório formatado com todas as informações

Verifique e exiba o tipo de cada variável coletada

"""

# Coletando dados dos funcionários

nome = input('Digite seu nome completo: ')
cpf = input('Digite seu CPF (somente números): ')
nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
salario = float(input('Digite seu salário: '))
ativo = input('É funcionário ativo? (True/False): ')

# Comparação de string

if ativo == 'True':
    ativo = True
    status = 'Ativo'
else:
    ativo = False
    status = 'Inativo'
  
# Exibição das informações

print(' === Relatório de Cadastro ===')

print(f'Nome: {nome} (tipo: {type(nome)})')
print(f'CPF: {cpf} (tipo: {type(cpf)})')
print(f'Data de Nascimento: {nascimento} (tipo: {type(nascimento)})')
print(f'Salário: R${salario:.2f} (tipo: {type(salario)})')
print(f'Status: {status} (tipo: {type(ativo)})')

print(f'=============================')

"""

-------------------------------------------------------------------------------------

Exercício 2.1 - Transformações de Texto

-------------------------------------------------------------------------------------

Dada a string: " python para dados "

Realize as seguintes transformações e exiba cada resultado:

Remova os espaços nas extremidades
Converta para maiúsculas
Converta para minúsculas
Capitalize (primeira letra maiúscula)

"""

texto = ' python para dados '

print(f'Original: {texto}')

texto = texto.strip()

print(f'Sem espaços: {texto}')
print(f'Maiúsculas: {texto.upper()}')
print(f'Minúsculas: {texto.lower()}')
print(f'Capitalizado: {texto.capitalize()}')

"""

-------------------------------------------------------------------------------------

Exercício 2.2 - Validador de Email

-------------------------------------------------------------------------------------

Crie um programa que valide um endereço de email. O email é válido se:

Contém o caractere @
Termina com .com ou .com.br
Não contém espaços
Solicite o email ao usuário e exiba se é válido ou inválido.

"""

email = input('Digite seu email: ')

if '@' in email and ' ' not in email and email.endswith(('.com', '.com.br')):
    print('Email válido!')
else:
    print('Email inválido!')

"""

-------------------------------------------------------------------------------------

Exercício 2.3 - Extraindo Informações de uma String

-------------------------------------------------------------------------------------

Dada a string: "2024-03-15" (formato de data)

Extraia e exiba:

O ano (primeiros 4 caracteres)
O mês (caracteres 5 a 7)
O dia (últimos 2 caracteres usando índice negativo)
A data formatada como DD/MM/AAAA

"""

data = '2024-03-15'

ano = data[:4:]
mes = data[5:7:]
dia = data[-2::]

print(f'Ano: {ano}')
print(f'Mês: {mes}')
print(f'Dia: {dia}')
print(f'Data formatada: {dia}/{mes}/{ano}')

"""

-------------------------------------------------------------------------------------

Exercício 2.4 - Relatório Formatado com F-Strings

-------------------------------------------------------------------------------------

Crie um relatório de vendas formatado usando f-strings com os seguintes dados:

Nome do produto: "Notebook Gamer"
Quantidade vendida: 125
Preço unitário: 3299.99
Desconto aplicado: 0.15 (15%)
Total bruto: quantidade × preço
Total com desconto: total bruto × (1 - desconto)
Exiba um relatório formatado com:

Nome do produto centralizado (20 caracteres)
Quantidade com preenchimento de zeros (3 dígitos)
Preço unitário como moeda (R$ com 2 decimais)
Desconto como porcentagem (2 decimais)
Total bruto com separador de milhar e 2 decimais
Total com desconto com separador de milhar e 2 decimais

"""

nome = 'Notebook Gamer'
vendidos = 125
preco = 3299.99
desconto = 0.15
total_bruto = vendidos * preco
total_final = total_bruto * (1 - desconto)

print('========= Relatório de Vendas ==========')
print (f'Produto: {nome:^20}')
print (f'Quantidade: {vendidos:03d} unidades')
print (f'Preço Unit.: R${preco:.2f}')
print (f'Desconto: {desconto:.2%}')
print(f'Total bruto: R$ {total_bruto:,.2f}')
print(f'Total final: R$ {total_final:,.2f}')
print('==========================================')

"""

Exercício 3.1 - Calculadora de Operações Aritméticas
Dados dois números: a = 15 e b = 4

Realize e exiba os resultados de todas as operações aritméticas:

Soma (+)
Subtração (-)
Multiplicação (*)
Divisão (/)
Divisão inteira (//)
Resto da divisão (%)
Potência (**)

"""

a = 15
b = 4

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} ** {b} = {a**b}')

"""

-------------------------------------------------------------------------------------

Exercício 3.2 - Contador com Operadores de Atribuição

-------------------------------------------------------------------------------------

Crie um programa que simule um contador que começa em 10 e realiza as seguintes operações:

Some 5
Subtraia 3
Multiplique por 2
Divida por 4 (divisão normal)
Faça divisão inteira por 2
Calcule o resto da divisão por 3
Eleve à potência 2
Use operadores de atribuição composta (+=, -=, *=, etc.) e exiba o valor após cada operação.

"""


contador = 10

print(f'Valor inicial: {contador}')

contador += 5

print(f'Após somar 5: {contador}')

contador -=3

print(f'Após subtrair 3: {contador}')

contador *= 2

print(f'Após multiplicar por 2: {contador}')

contador /= 4

print(f'Após dividir por 4: {contador}')

contador //= 2

print(f'Após divisão inteira por 2: {contador}')

contador %= 3

print(f'Após resto da divisão por 3: {contador}')

contador **= 2

print(f'Após elevar a potência de 2: {contador}')

"""

-------------------------------------------------------------------------------------

Exercício 3.3 - Sistema de Validação com Operadores Lógicos

-------------------------------------------------------------------------------------

Crie um sistema que valide se uma pessoa pode dirigir baseado nas seguintes condições:

Idade mínima: 18 anos
Possui carteira de motorista: True/False
Não está com a carteira suspensa: True/False
A pessoa pode dirigir se:

Tiver 18 anos ou mais E
Possuir carteira de motorista E
Não estiver com a carteira suspensa
Solicite as informações ao usuário e exiba se pode ou não dirigir.

"""

idade = int(input('Digite sua idade: '))
possui_carteira = input('Possui carteira de motorista? (True/False): ') 
carteira_suspensa = input('Está com a carteira suspensa? (True/False): ') 

if possui_carteira == 'True':
    possui_carteira = True
else:
    possui_carteira = False

if carteira_suspensa == 'True':
    carteira_suspensa = True
else:
    carteira_suspensa = False

if idade >= 18 and possui_carteira and not carteira_suspensa:
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')

"""

-------------------------------------------------------------------------------------

Exercício 3.4 - Calculadora de Desconto Progressivo

-------------------------------------------------------------------------------------

Crie uma calculadora de desconto que aplica descontos progressivos baseados no valor da compra:

Compras até R 100:semdesconto−ComprasentreR  100 e R 500:5−ComprasentreR  500 e R 1000:10−ComprasacimadeR  1000: 15% de desconto
Além disso, se o cliente for VIP (True/False), adicione 2% de desconto extra.

O programa deve:

Solicitar o valor da compra
Solicitar se é cliente VIP
Calcular o desconto baseado na faixa de valor
Adicionar desconto VIP se aplicável
Calcular o valor final
Exibir: valor original, desconto aplicado (%), valor do desconto (R$), valor final

"""

valor_compra = float(input('Digite o valor da compra:'))
tipo_cliente = input('É cliente VIP? (True/False): ')

if valor_compra < 100:
    desconto = 0.00
elif valor_compra >= 100 and valor_compra < 500:
    desconto = 0.05
elif valor_compra >= 500 and valor_compra < 1000:
    desconto = 0.10
else:
    desconto = 0.15

if tipo_cliente == 'True':
    desconto += 0.02

valor_desconto = valor_compra * desconto
valor_final = valor_compra * (1 - desconto)

print(f'Valor original: R${valor_compra:.2f}')
print(f'Desconto aplicado: {desconto:.2%}')
print(f'Valor do desconto: R${valor_desconto:.2f}')
print(f'Valor final: R${valor_final:.2f}')

"""

-------------------------------------------------------------------------------------

Exercício 4.1 - Classificador de Idade

-------------------------------------------------------------------------------------

Crie um programa que classifique uma pessoa em categorias de idade:

Menor de 18 anos: "Menor de idade"
Entre 18 e 64 anos: "Adulto"
65 anos ou mais: "Idoso"
Solicite a idade ao usuário e exiba a classificação usando if, elif e else.

"""

while True:

  idade = int(input('Digite sua idade (-1 para sair): '))

  if idade == -1:
      break
  elif idade < 18:
      print('Menor de idade')
  elif idade < 65:
      print('Adulto')
  else:
      print('Idoso')

"""

-------------------------------------------------------------------------------------

Exercício 4.2 - Gerador de Tabuada

-------------------------------------------------------------------------------------

Crie um programa que gere a tabuada de um número fornecido pelo usuário.

O programa deve:

Solicitar um número inteiro
Gerar e exibir a tabuada de 1 até 10
Usar for com range()
Formatá-la de forma clara

"""

numero = int(input('Digite um número para ver sua tabuada: '))

print()

print(f'Tabuada do {numero}')

for i in range(1,11):
  print (f'{numero} x {i} = {numero * i}')

"""

-------------------------------------------------------------------------------------

Exercício 4.3 - Validador de Senha com WHILE

-------------------------------------------------------------------------------------

Crie um programa que valide uma senha. A senha deve:

Ter pelo menos 8 caracteres
Conter pelo menos uma letra maiúscula
Conter pelo menos uma letra minúscula
Conter pelo menos um número
O programa deve solicitar a senha repetidamente até que uma senha válida seja fornecida, usando while.

"""

while True:

    senha = input('Digite uma senha: ')

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    if len(senha) >= 8:

        for caractere in senha:

            if caractere.islower():
                tem_minuscula = True

            if caractere.isupper():
                tem_maiuscula = True

            if caractere.isnumeric():
                tem_numero = True

        if tem_minuscula and tem_maiuscula and tem_numero:
            print('Senha válida! Cadastro realizado com sucesso.')
            break
        else:
            print('Senha inválida! Tente novamente.')

    else:
        print('Senha inválida! Tente novamente.')

"""

-------------------------------------------------------------------------------------

Exercício 4.4 - Menu Interativo com While True

-------------------------------------------------------------------------------------

Crie um menu interativo que permite ao usuário:

Calcular área de um retângulo
Calcular área de um círculo
Verificar se um número é par ou ímpar
Sair do programa
O programa deve:

Exibir um menu numerado
Solicitar a opção do usuário
Executar a operação escolhida
Voltar ao menu após cada operação (exceto ao sair)
Usar while True com break para sair
Usar continue para voltar ao início do loop em caso de opção inválida

"""

while True:

    print ('=== MENU ===')
    print ('1. Calcular área do retângulo')
    print ('2. Calcular área do círculo')
    print ('3. Verificar se número é par/ímpar')
    print ('4. Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 4:

        print('Programa encerrado. Até logo!')
        break

    elif opcao == 1:

        largura = float(input('Digite a largura: '))
        altura = float(input('Digite a altura: '))
        print(f'Área do retângulo: {largura * altura:}')

    elif opcao == 2:

        pi = 3.14159
        raio = float(input('Digite o raio: '))
        print(f'Área do círculo: {pi * (raio ** 2)}')

    elif opcao == 3:

        numero = int(input('Digite um número: '))

        if numero % 2 == 1:
            print(f'O número {numero} é ímpar')
        else:
            print(f'O número {numero} é par')

    else:
        print('Opção inválida!')
        continue