from grafo import Digrafo
from curso import curso

grafo = Digrafo()

for disciplina in curso:
    grafo.adicionaVertice(disciplina)

for disciplina, requisitos in curso.items():
    for requisito in requisitos:
        grafo.conecta(requisito, disciplina)

print("Um vértice: " + grafo.umVertice())
print("Ordem: " + str(grafo.ordem()))
print("Antecessores de ED:" + str(grafo.antecessores('Estruturas de Dados')))
print("Sucessores de Grafos:" + str(grafo.sucessores('Grafos')))

