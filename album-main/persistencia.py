import json

def salvar_filmes(filmes):
    with open("filmes.json", "w", encoding="utf-8") as arquivo:
       json.dump(filmes, arquivo, indent=4) 

def carregar_filmes():
    try:
        with open("filmes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []
    
# Implementar as funções salvar_venda e carregar_venda