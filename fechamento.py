from datetime import datetime
from historico import Pagamento

def fechar_e_pagar(comanda, estoque, forma_pagamento, registro_pagamentos, historico_comandas):
    valor_total = calcular_total(comanda)
    dar_baixa_estoque(comanda, estoque)

    novo_pagamento = Pagamento(
        comanda.nome_cliente, 
        comanda.numero, forma_pagamento,
        valor_total, datetime.now()
    )
    
    comanda.fechar_comanda()

    registro_pagamentos.adicionar_pagamento(novo_pagamento)
    historico_comandas.adicionar_comanda(comanda)

    return novo_pagamento

# Tira do estoque os itens que foram consumidos
def dar_baixa_estoque(comanda, estoque):    
    no_atual = comanda.refeicoes.inicio
    while no_atual is not None:
        estoque.dar_baixa(no_atual.item.nome, 1)
        no_atual = no_atual.proximo

    no_atual = comanda.bebidas.inicio
    while no_atual is not None:
        estoque.dar_baixa(no_atual.item.nome, 1)
        no_atual = no_atual.proximo

def calcular_total(comanda):
    total = 0

    no_atual = comanda.refeicoes.inicio
    while no_atual is not None:
        total += no_atual.item.preco_item
        no_atual = no_atual.proximo

    no_atual = comanda.bebidas.inicio
    while no_atual is not None:
        total += no_atual.item.preco_item
        no_atual = no_atual.proximo

    return total    
