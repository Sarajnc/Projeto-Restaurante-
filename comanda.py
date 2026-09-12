class Comanda:
    def __init__(self, numero, nome, data, hora):
        self.numero = numero
        self.nome = nome
        self.data = data
        self.hora = hora

        self.refeicao = Historico()
        self.bebida = Historico()

    def adicionar_item(self, novo_item):
        if novo_item.tipo == "refeicao":
            self.refeicao.adicionar(novo_item)
        elif novo_item.tipo == "bebida":
            self.bebida.adicionar(novo_item)

    def remover_item(self, item_retirado):
        if item_retirado.tipo == "refeicao":
            self.refeicao.remover(item_retirado)
        elif item_retirado.tipo == "bebida":
            self.bebida.remover(item_retirado)
    
class Item:
    def __init__(self, nome,tipo):
        self.nome = nome
        self.tipo = tipo

class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
 
class Historico:
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