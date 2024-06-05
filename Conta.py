# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
def mostrar_menu():
    menu = '''
    Escolha:
    [d] depósitar
    [s] sacar
    [e] extrato
    [x] sair
    '''
    opcao = input(menu)
    return opcao

def depositar(saldo, extrato):
    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: R$ '))
        if valor > 0 :
            saldo += valor  # equivale a saldo + valor
            resultado = f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {saldo}'
            print(resultado)
            extrato += f"Depósito de R$ {valor}! Saldo atualizado: R$ {saldo}\n"
    return saldo, extrato


def sacar(saldo, extrato):
    if opcao == 's':
        valor = float(input('Digite o valor do saque: R$ '))
        if quantidade_de_saques > 0:
            if valor <= saldo:
                saldo -= valor
                print(f'Saque de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
                extrato += f'Saque de R$ {valor}! Saldo atualizado: R$ {saldo}\n'
            else:
                print(f'Infelizmente não será possível sacar o dinheiro por falta de saldo\nSaldo: R$ {saldo}')
        else:
            print(f'Infelizmente não será possível sacar o dinheiro por limite de saques')
    return saldo, extrato

saldo = 0
limite_de_saque = 500
quantidade_de_saques = 3
extrato = ""

while True:
    opcao = mostrar_menu()    
    if opcao == 'x': break
    elif opcao == 'd': saldo, extrato = depositar(saldo, extrato)
    elif opcao == 's': saldo, extrato = sacar(saldo, extrato)
    elif opcao == 'e': print(extrato)
    else : print('Opção inválida!')
