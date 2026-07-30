class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular}, possui R${self.saldo:.2f} de saldo"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} autorizado na conta {self.id}")
            return self.saldo
        else:
            print("Saldo insuficiente!!!")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor:.2f} autorizado na conta {self.id}")
        return self.saldo

c1 = ContaBancaria(112, "Rafael", 3000)
print(c1)
print("")
c1.sacar(200000)
print("")
print(c1)
print("")
c1.depositar(10000)
print("")
print(c1)