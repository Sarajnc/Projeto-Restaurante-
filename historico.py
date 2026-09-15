from lista_encadeada import ListaEncadeada

class RegistroPagamentos:
    def __init__(self):
        self.pagamentos = ListaEncadeada()

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.adicionar(pagamento)

class HistoricoComandas:
    def __init__(self):
        self.comandas = ListaEncadeada()

    def adicionar_comanda(self, comanda):
        self.comandas.adicionar(comanda)