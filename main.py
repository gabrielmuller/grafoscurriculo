from grafo import Digrafo
from curso import curriculo, Graduacao

# ---------- Testes Digrafo
grafo = Digrafo()

for disciplina in curriculo:
    grafo.adicionaVertice(disciplina)

for disciplina in curriculo:
    for requisito in curriculo[disciplina].requisitos:
        grafo.conecta(requisito, disciplina)

print("Um vértice: " + grafo.umVertice())
print("Ordem: " + str(grafo.ordem()))
print("Antecessores de ED:" + str(grafo.antecessores('INE5408')))
print("Sucessores de Grafos:" + str(grafo.sucessores('INE5409')))

print("Ordem topológica: " + str(grafo.ordemTopologica()))


# ---------- Testes Graduacao
graduacao = Graduacao(curriculo)

graduacao.plan()