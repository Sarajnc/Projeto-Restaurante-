from lista_encadeada import ListaEncadeada

class Pagamento:
    def __init__(self, nome_pagador, numero_comanda, forma_pagamento, valor_total, data_hora):
        self.nome_pagador = nome_pagador
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = data_hora

class HistoricoPagamentos:
    def __init__(self):
        self.pagamentos = ListaEncadeada()

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.adicionar(pagamento)

class HistoricoComandas:
    def __init__(self):
        self.comandas = ListaEncadeada()

    def adicionar_comanda(self, comanda):
        self.comandas.adicionar(comanda)
