# Acesso ao sistema e variaveis

nome = str(input('Bem-vindo! Digite seu nome completo: '))
idade = int(input('Digite sua idade: '))
saldo = float(input('Digite seu saldo: '))

# Digitar numeros no sistema


digitar = int(input('Digite 1 para sacar, \n2 para fazer depósito, \n3 para solicitar emprestimo, \n4 para visualizar informaçoes, \nqualquer outro numero para sair: '))



# Funçoes
def saque():
    saq = float(input('Digite o quanto você deseja sacar: '))

    if saq > 1000 or saq > saldo:
        print('Saque maior que R$1000 ou saldo insuficiente')

    else:
        print('Seu saldo agora é: ' + str(saldo - saq))


def deposito():
    dep = float(input('Digite quanto você quer depositar: '))

    if dep > 5000:
        print('Valor muito incompatível com nosso banco!')

    else:
        print('Seu saldo agora é: ' + str(saldo + dep))

def emprestimo():
    emp = float(input('Digite o valor desejado do empréstimo: '))
    if idade < 21 and emp <= 1000 and emp <= 2000 and emp > saldo*15:
        print('Empréstimo inválido')

    else:
        print('Emprestimo aprovado! Seu saldo agora é: ' + str(emp + saldo))

def informacoes():
    print(nome)
    print(idade)
    print(saldo)

# Condições teclado
if digitar == 1:
    saque()

elif digitar == 2:
    deposito()

elif digitar == 3:
    emprestimo()

elif digitar == 4:
    informacoes()

else:
    print('Falou parceiro!')
