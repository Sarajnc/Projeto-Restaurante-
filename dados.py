import pickle

def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, "wb") as arquivo:
        pickle.dump(dados, arquivo)

def carregar_dados(nome_arquivo):
    with open(nome_arquivo, "rb") as arquivo:
        dados = pickle.load(arquivo)

    return dados