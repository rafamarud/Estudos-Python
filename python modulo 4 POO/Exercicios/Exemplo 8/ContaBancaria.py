class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # público (+)
        self._titular = nome  # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f"Conta {self .id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def __str__(self):
        #return f"A conta {self.id} de {self.titular}, possui R${self.saldo:.2f} de saldo"
        return f"Estado atua da conta: {self.__dict__}"
    def sacar(self, valor):
        valor = abs(valor)
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor:.2f} autorizado na conta {self.id}")
            return self.__saldo
        else:
            print("Saldo insuficiente!!!")

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de {valor:.2f} autorizado na conta {self.id}")
        return self.__saldo

