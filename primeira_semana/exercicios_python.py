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

print()

print(f'Nome: {nome}, tipo: {type(nome)}')
print(f'Idade: {idade}, tipo: {type(idade)}')
print(f'Altura: {altura}, tipo: {type(altura)}')
print(f'É estudante: {estudante}, tipo: {type(estudante)}')

print()

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

print()

print('Cadastro realizado com sucesso!')

print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Altura: {altura:.2f} metros')

print()

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

print()

peso = float(input('Peso (quilogramas): '))
altura = float(input('Altura (metros): '))

imc = peso / (altura ** 2)

print ()

print(f'Seu IMC é: {imc:.2f}')

print ()

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


