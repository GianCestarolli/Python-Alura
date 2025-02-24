class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}'

    def ativar_conta(self):
        self._ativo = not self._ativo

carlos = ContaBancaria("Carlos", 2000)
ana = ContaBancaria("Ana", 5000)

carlos.ativar_conta()
print(carlos)
print(ana)




    
        
