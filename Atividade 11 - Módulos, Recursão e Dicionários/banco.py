saldo = 0

def depositar(valor):
    global saldo
    saldo += valor
    return saldo

def sacar(saque):
    global saldo
    if saque < saldo:
        saldo -= saque
        return True
    else:
        return False

def visualizarSaldo():
    return saldo