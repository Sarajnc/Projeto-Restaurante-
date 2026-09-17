import random
from faker import Faker

from comanda import Comanda
from cardapio import ItemCardapio
from estoque import Estoque, RegistroEstoque
from fechamento import fechar_e_pagar
from historico import HistoricoPagamentos, HistoricoComandas
from relatorios import relatorio_vendas, relatorio_consumo
from dados import salvar_dados, carregar_dados

fake = Faker("pt_BR")

Cardapio = [
    ItemCardapio("Taco", "refeicao", 28.00),
    ItemCardapio("Burrito", "refeicao", 36.00),
    ItemCardapio("Quesadilla", "refeicao", 30.00),
    ItemCardapio("Coca-Cola", "bebida", 10.00),
    ItemCardapio("Suco", "bebida", 8.00),
    ItemCardapio("Agua", "bebida", 4.00),
]

Refeicoes = [item for item in Cardapio if item.tipo == "refeicao"]
Bebidas = [item for item in Cardapio if item.tipo == "bebida"]

Forma_pagamento = ["Pix", "Cartão", "Dinheiro"]

def gerar_estoque():
    estoque = Estoque()
    nomes_produtos = [item.nome for item in Cardapio]

    for nome_produto in nomes_produtos:

        for _ in range(3):
            data_compra = fake.date_between(start_date="-90d", end_date="today")
            data_validade = fake.date_between(start_date="today", end_date="+60d")
            registro = RegistroEstoque(
                nome_produto,
                random.randint(10, 30),
                round(random.uniform(2.0, 10.0), 2),
                round(random.uniform(10.0, 25.0), 2),
                data_compra,
                data_validade,
            )
            estoque.adicionar_registro(registro)
 
    return estoque

def gerar_comandas(quantidade, estoque, historico_pagamentos, historico_comandas):
    comandas_geradas = []
 
    for numero in range(1, quantidade + 1):
        comanda = Comanda(numero, fake.name())
        comanda.adicionar_refeicao(random.choice(Refeicoes))
        comanda.adicionar_bebida(random.choice(Bebidas))
 
        forma_pagamento = random.choice(Forma_pagamento)
        fechar_e_pagar(comanda, estoque, forma_pagamento, historico_pagamentos, historico_comandas)
 
        comandas_geradas.append(comanda)
 
    return comandas_geradas
if __name__ == "__main__":
    estoque = gerar_estoque()
    historico_pagamentos = HistoricoPagamentos()
    historico_comandas = HistoricoComandas()

    comandas = gerar_comandas(
        10,
        estoque,
        historico_pagamentos,
        historico_comandas
    )

    print(f"{len(comandas)} comandas geradas e pagas.\n")

    estoque.mostrar_estoque()

    relatorio_vendas(historico_pagamentos)
    relatorio_consumo(historico_comandas)

    dados_sistema = {
        "estoque": estoque,
        "pagamentos": historico_pagamentos,
        "comandas": historico_comandas
    }

    salvar_dados(dados_sistema, "dados_restaurante.pkl")
    print("\nDados salvos com sucesso!")

dados_carregados = carregar_dados("dados_restaurante.pkl")
print("\nDados carregados com sucesso!")

estoque_carregado = dados_carregados["estoque"]
estoque_carregado.mostrar_estoque()