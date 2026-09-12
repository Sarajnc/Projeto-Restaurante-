from lista_encadeada import ListaEncadeada

class Ingrediente:
    def __init__(self, nome_produto, unidade):
        self.nome_produto = nome_produto
        self.unidade = unidade

class RegistroEstoque:
    def __init__(self, ingrediente, quantidade, preco_compra, data_compra, data_validade):
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.data_compra = data_compra
        self.data_validade = data_validade

class Estoque:
    def __init__(self):
        self.registros = ListaEncadeada()

    def adicionar_registro(self, novo_registro):
        self.registros.adicionar(novo_registro)

    def mostrar_estoque(self):
        no_atual = self.registros.inicio

        while no_atual is not None:
            registro_atual = no_atual.item

        print("Produto:", registro_atual.ingrediente.nome_produto)
        print(
            "Quantidade:",
            registro_atual.quantidade,
            registro_atual.ingrediente.unidade
        )
        print("Preço da compra: R$", registro_atual.preco_compra)
        print("Data da compra:", registro_atual.data_compra)
        print("Data de validade:", registro_atual.data_validade)

        no_atual = no_atual.proximo