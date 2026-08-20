# Catálogo com filme, álbum, personagem, figurinhas.

filmes = []

def cadastrar_filme(titulo, preco_album, preco_pacote):
    filme = {
        "titulo": titulo,
        "preco_album": preco_album,
        "preco_pacote": preco_pacote,
        "personagens": [],
        "figurinhas": []
    }
    filmes.append(filme)
    return filme

def cadastrar_personagem(filme, nome):
    personagem = {'nome': nome}
    filme["personagens"].append(personagem)
    return personagem

def cadastrar_figurinha(filme, numero, personagem):
    figurinha = {
        "numero": numero,
        "personagem": personagem
    }
    filme["figurinhas"].append(figurinha)
    return figurinha

def cadastrar_pacote(fig1, fig2, fig3):
    pacote = [fig1, fig2, fig3]
    return pacote

def listar_filmes():
    for indice, filme in enumerate(filmes):
        print(f"{indice + 1} - {filme['titulo']}")
        print(f"    Álbum: R$ {filme['preco_album']:.2f}")
        print(f"    Preço do pacote: R$ {filme['preco_pacote']:.2f}")
        print("    Figurinhas:")
        for figurinha in filme['figurinhas']:
            print(f"       {figurinha['numero']}-{figurinha['personagem']['nome']}")
