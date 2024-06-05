from abc import ABC, abstractmethod

class cliente:
    def __init__(self, endereco):
        self._endereco = endereco
    
    def realizar_trasacao(self, conta, trasacao):
        Trasacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "01"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.transacoes.append(f"Depósito de R$ {valor:.2f}. Saldo atualizado: R$ {self._saldo:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self._saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar():
        pass

    def depositar():
        pass

    def criar_conta():
        pass

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Trasacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Trasacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.depositar(self._valor)
        print(f"Depósito de R$ {self._valor} realizado com sucesso. Novo saldo: R$ {conta.saldo:.2f}")
        successo_no_deposito = conta.deposito(self._valor)
        if successo_no_deposito:
            conta.historico.adicionar_transacao(self)

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
            trasacao = Deposito(valor)
            cliente = Cliente("João", "12345678901")
            cliente.realizar_trasacao(trasacao)
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
