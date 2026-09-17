## guarda o item e aponta para o próximo
class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
        
## adiciona os itens no começo da lista
class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, novo_item):
        novo_no = No(novo_item)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio = novo_no

    def remover(self, item_retirado):
        if self.inicio is None:
            return
        elif self.inicio.item == item_retirado:
            self.inicio = self.inicio.proximo
            return

        no_anterior = self.inicio
        no_atual = self.inicio.proximo

        while no_atual is not None:
            if no_atual.item == item_retirado:
                no_anterior.proximo = no_atual.proximo
                return

            no_anterior = no_atual
            no_atual = no_atual.proximo

    def mostrar_itens(self):
        no_atual = self.inicio

        while no_atual is not None:
            print(f"{no_atual.item.nome} - R$ {no_atual.item.preco_item:.2f}")
            no_atual = no_atual.proximo
