from lista_encadeada import ListaEncadeada

class ItemCardapio:
    def __init__(self, nome, tipo, preco_item):
        self.nome = nome
        self.tipo = tipo
        self.preco_item = preco_item

class Cardapio:
    def __init__(self):
        self.itens = ListaEncadeada()

    def adicionar_item(self, item):
        self.itens.adicionar(item)

    def mostrar_cardapio(self):
        print("\n- CARDÁPIO -")
        self.itens.mostrar_itens()

    def buscar_item(self, nome_buscado):
        no_atual = self.itens.inicio
        while no_atual is not None:
            if no_atual.item.nome == nome_buscado:
                return no_atual.item
            
            no_atual = no_atual.proximo
        print('Item não encontrado')