from datetime import datetime
from lista_encadeada import ListaEncadeada

class Comanda:
    def __init__(self, numero, nome_cliente):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_abertura = datetime.now()

        self.refeicoes = ListaEncadeada()
        self.bebidas = ListaEncadeada()

        self.aberta = True
        self.data_fechamento = None

    def fechar_comanda(self):
        if not self.aberta:
            print('A comanda já está fechada')
            return
        
        self.aberta = False
        self.data_fechamento = datetime.now()
        
    def adicionar_refeicao(self, nova_refeicao):
        if self.aberta:
            self.refeicoes.adicionar(nova_refeicao)      
        else:
            print('Comanda fechada, não é possível adicionar itens')      

    def adicionar_bebida(self, bebida):
        if self.aberta:
            self.bebidas.adicionar(bebida) 
        else:
            print('Comanda fechada, não é possível adicionar itens')

    def remover_item(self, item_retirado):
        if not self.aberta:
            print('Comanda fechada, não é possível remover itens')
            return

        if item_retirado.tipo == "refeicao":
            self.refeicoes.remover(item_retirado)

        elif item_retirado.tipo == "bebida":
            self.bebidas.remover(item_retirado)
    
class Item:
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
                return  no_atual.item
            
            no_atual = no_atual.proximo
        print('Item não encontrado')
