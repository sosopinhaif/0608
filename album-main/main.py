from catalogo import (
    filmes,
    cadastrar_filme,
    cadastrar_personagem,
    cadastrar_figurinha,
    listar_filmes,
    cadastrar_pacote
)
from venda import realizar_venda, exibir_venda
from persistencia import salvar_filmes, carregar_filmes

vingadores = cadastrar_filme(titulo="Vingadores", preco_album=15, preco_pacote=5)
hulk = cadastrar_filme(titulo="Hulk", preco_album=10, preco_pacote=4)

homem_ferro = cadastrar_personagem(filme=vingadores, nome="Homem de ferro")
xenoman = cadastrar_personagem(filme=vingadores, nome="Xenoman")
capitao_america_sul = cadastrar_personagem(filme=vingadores, nome="Capitão América do Sul")
scooby_doo = cadastrar_personagem(filme=vingadores, nome="Scooby Doo")
lippy = cadastrar_personagem(filme=vingadores, nome="Lippy")
hardy = cadastrar_personagem(filme=vingadores, nome="Hardy")

fig1=cadastrar_figurinha(filme=vingadores, numero=1, personagem=homem_ferro)
fig2=cadastrar_figurinha(filme=vingadores, numero=2, personagem=xenoman)
fig3=cadastrar_figurinha(filme=vingadores, numero=3, personagem=capitao_america_sul)
fig4=cadastrar_figurinha(filme=vingadores, numero=4, personagem=scooby_doo)
fig5=cadastrar_figurinha(filme=vingadores, numero=5, personagem=lippy)
fig6=cadastrar_figurinha(filme=vingadores, numero=6, personagem=hardy)

pacote1 = cadastrar_pacote(fig1, fig2, fig3)
pacote2 = cadastrar_pacote(fig1, fig2, fig4)
pacote3 = cadastrar_pacote(fig3, fig5, fig6)
pacote4 = cadastrar_pacote(fig4, fig5, fig6)
pacote5 = cadastrar_pacote(fig5, fig2, fig6)
pacote6 = cadastrar_pacote(fig2, fig4, fig5)

#listar_filmes()

venda = realizar_venda(vingadores, 1, [pacote1, pacote2, pacote3, pacote4, pacote5, pacote6])
exibir_venda(venda)

salvar_filmes([vingadores, hulk])


filmes = carregar_filmes()

for f in filmes:
    print(f)

