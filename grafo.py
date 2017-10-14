from warnings import warn
class Digrafo:
    def __init__(self):
        # Arestas
        self.arestas = {}

        # Arestas inversas
        self.inverso = {}
            
    def adicionaVertice(self, v):
        if v in self.arestas:
            warn(UserWarning(str(v) + ' já está no grafo'))
        else:
            self.arestas[v] = set()
            self.inverso[v] = set()

    def removeVertice(self, v):
        if v not in self.arestas:
            warn(UserWarning(str(v) + ' não está no grafo'))
        else:
            for vertice, sucessores in self.arestas.items():
                sucessores.discard(v)
            for vertice, antecessores in self.inverso.items():
                antecessores.discard(v)
            del self.arestas[v]
            del self.inverso[v]

    def conecta(self, v1, v2):
        msg = ''
        for v in {v1, v2}:
            if v not in self.arestas:
                msg += str(v) + ' '
        if msg:
            raise Exception('Não há ' + msg + 'no grafo')

        self.arestas[v1].add(v2)
        self.inverso[v2].add(v1)

    def desconecta(self, v1, v2):
        msg = ''
        for v in {v1, v2}:
            if v in self.arestas:
                msg += str(v) + ' '
        if msg:
            warn(UserWarning('Não há ' + msg + 'no grafo'))
        else:
            self.arestas[v1].remove(v2)
            self.inverso[v2].remove(v1)

    def ordem(self):
        return len(self.arestas)

    def vertices(self):
        return set(self.arestas)

    def umVertice(self):
        return next(iter(self.vertices()), None)

    def sucessores(self, v):
        return self.arestas[v]

    def antecessores(self, v):
        return self.inverso[v]

    def grauDeEmissao(self, v):
        return len(self.sucessores(v))

    def grauDeRecepcao(self, v):
        return len(self.antecessores(v))

    def ordemTopologica(self):
        self.naoVisitados = set(self.arestas)
        self.L = []

        while self.naoVisitados:
            self.marcadosTemp = set()
            vertice = next(iter(self.naoVisitados))
            self.visita_rec(vertice)

        return list(reversed(self.L))

    def visita_rec(self, v):
        if v not in self.naoVisitados:
            return
        if v in self.marcadosTemp:
            raise Exception('Grafo tem um ciclo em ' + str(v) + '.')

        self.marcadosTemp.add(v)
        for sucessor in self.sucessores(v):
            self.visita_rec(sucessor)
        self.naoVisitados.remove(v)
        self.L.append(v)
