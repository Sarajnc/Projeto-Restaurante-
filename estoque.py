from lista_encadeada import ListaEncadeada, No

class Ingrediente:
    def __init__(self, nome_produto, unidade):
        self.nome_produto = nome_produto
        self.unidade = unidade

class RegistroEstoque:
    def __init__(self, ingrediente, quantidade, preco_compra, preco_venda, data_compra, data_validade):
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade

    def editar_quantidade(self, quantidade):
        if quantidade < 0:
            print("A quantidade não pode ser negativa")
            return False

        self.quantidade = quantidade
        return True

class FilaEstoque:
    def __init__(self):
        self.inicio_fila = None
        self.fim_fila = None

    def enfileirar(self, novo_registro):
        novo_no = No(novo_registro)
        if self.fim_fila is None:
            self.inicio_fila = novo_no
            self.fim_fila = novo_no
        else:
            self.fim_fila.proximo = novo_no
            self.fim_fila = novo_no

    def desenfileirar(self):
        if self.inicio_fila is None:
            print("Estoque vazio")
            return None

        registro_removido = self.inicio_fila.item
        self.inicio_fila = self.inicio_fila.proximo

        if self.inicio_fila is None:
            self.fim_fila = None
        return registro_removido
    
class Estoque:
    def __init__(self):
        self.registros = FilaEstoque()

    def adicionar_registro(self, novo_registro):
        self.registros.enfileirar(novo_registro)

    def dar_baixa(self, nome_produto, quantidade_necessaria):
        no_anterior = None
        no_atual = self.registros.inicio_fila
        restante = quantidade_necessaria

        while no_atual is not None and restante > 0:
            registro = no_atual.item

            if registro.ingrediente.nome_produto == nome_produto:
                if registro.quantidade <= restante:
                    restante -= registro.quantidade
                    registro.quantidade = 0
                    if no_anterior is None:
                        self.registros.inicio_fila = no_atual.proximo
                    else:
                        no_anterior.proximo = no_atual.proximo
                    if no_atual is self.registros.fim_fila:
                        self.registros.fim_fila = no_anterior
                else:
                    registro.quantidade -= restante
                    restante = 0

            no_anterior = no_atual
            no_atual = no_atual.proximo

        if restante > 0:
            print(f"Estoque insuficiente de {nome_produto}")

    def mostrar_estoque(self):
        no_atual = self.registros.inicio_fila

        while no_atual is not None:
            registro_atual = no_atual.item

            print("Produto:", registro_atual.ingrediente.nome_produto)
            print(
                "Quantidade:",
                registro_atual.quantidade,
                registro_atual.ingrediente.unidade
            )
            print("Preço da compra: R$", registro_atual.preco_compra)
            print("Preço de venda: R$", registro_atual.preco_venda)
            print("Data da compra:", registro_atual.data_compra)
            print("Data de validade:", registro_atual.data_validade)

            no_atual = no_atual.proximo
