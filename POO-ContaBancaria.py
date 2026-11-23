class ContaBancaria:
    def _init_(self, saldo):
        self._saldo = saldo #Privado

    def get_saldo(self): #getter
        return self._saldo

    def depositas(self, valor): # setter
        if valor > 0:
         self.__saldo += valor
    