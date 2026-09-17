def relatorio_vendas(historico_pagamentos):
    total_vendido = 0
    quantidade_comandas = 0
    total_por_forma = {"Pix": 0, "Cartão": 0, "Dinheiro": 0}

    no_atual = historico_pagamentos.pagamentos.inicio
    while no_atual is not None:
        pagamento = no_atual.item

        total_vendido += pagamento.valor_total
        quantidade_comandas += 1
        total_por_forma[pagamento.forma_pagamento] += pagamento.valor_total

        no_atual = no_atual.proximo

    print("\n--- RELATÓRIO DE VENDAS ---")
    print(f"Total vendido: R$ {total_vendido:.2f}")
    print(f"Comandas pagas: {quantidade_comandas}")
    for forma, valor in total_por_forma.items():
        print(f"  {forma}: R$ {valor:.2f}")

def relatorio_consumo(historico_comandas):
    contagem_itens = {}

    no_comanda = historico_comandas.comandas.inicio
    while no_comanda is not None:
        comanda = no_comanda.item

        no_item = comanda.refeicoes.inicio
        while no_item is not None:
            nome = no_item.item.nome
            contagem_itens[nome] = contagem_itens.get(nome, 0) + 1
            no_item = no_item.proximo

        no_item = comanda.bebidas.inicio
        while no_item is not None:
            nome = no_item.item.nome
            contagem_itens[nome] = contagem_itens.get(nome, 0) + 1
            no_item = no_item.proximo

        no_comanda = no_comanda.proximo

    print("\n--- RELATÓRIO DE CONSUMO ---")
    for nome_item, quantidade in sorted(contagem_itens.items(), key=lambda x: -x[1]):
        print(f"{nome_item}: {quantidade}x")