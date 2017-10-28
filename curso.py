from grafo import Digrafo

class Disciplina():
    def __init__(self, nome, horas, requisitos):
        self.nome = nome
        self.horas = horas
        self.requisitos = requisitos

'''
    Graduacao é inicializada com um dicionário de todas as disciplinas do curriculo.
'''
class Graduacao():
    def __init__(self, curriculo):
        self.curriculo = curriculo

    '''
        Getter para currículo
    '''
    def get(self):
        return self.curriculo

    '''
        Considerando a quantidade máxima de horas/aula por semestre (30) e as disciplinas
        já cursadas, distribui as disciplinas restantes ao longo dos semestres subsequentes,
        respeitando os pré-requisitos
        Para isso, cria um grafo com as disciplinas do currículo
    '''
    def plan(self):
        grafo = Digrafo()
        for disciplina in self.curriculo:
            grafo.adicionaVertice(disciplina)
        for disciplina in self.curriculo:
            for requisito in self.curriculo[disciplina].requisitos:
                grafo.conecta(requisito, disciplina)
        print("Insira código das disciplinas cursadas")  
        cursadas = []
        inserida = input()
        while inserida != "":
            cursadas.append(inserida)
            inserida = input()
        for disciplina in cursadas:
            grafo.removeVertice(disciplina)
        semestre = set()
        horas = 0
        num_semestre = 1
        ordemTopologica = grafo.ordemTopologica()
        while grafo.ordem() > 0:
            for disciplina in ordemTopologica:
                if horas + self.curriculo[disciplina].horas <= 30 \
                and disciplina not in semestre:
                    if not grafo.antecessores(disciplina):
                        semestre.add(disciplina)
                        horas += self.curriculo[disciplina].horas             
                else:
                    print("\nRecomendação para o " + str(num_semestre) \
                    + "° semestre com " + str(horas) + " h/a:")
                    for disciplina in semestre:
                        print(disciplina + ': ' + self.curriculo[disciplina].nome)
                        grafo.removeVertice(disciplina)
                        ordemTopologica.remove(disciplina) 
                    semestre = set()
                    num_semestre += 1
                    horas = 0       

curriculo = {
    "INE5402": Disciplina("Programação Orientada a Objetos I", 6, {}),
    "INE5403": Disciplina("Matemática Discreta para Computação", 6, {}),
    "MTM3100": Disciplina("Cálculo 1", 4, {}),
    "EEL5105": Disciplina("Circuitos e Técnicas Digitais", 5, {}),
    "INE5401": Disciplina("Introdução à Computação", 2, {}),
    "INE5404": Disciplina("Programação Orientada a Objetos II", 6, {
        "INE5402"
    }),
    "INE5405": Disciplina("Probabilidade e Estatística", 5, {
        "MTM3100"
    }),
    "MTM3102": Disciplina("Cálculo 2", 4, {
        "MTM3100"
    }),
    "MTM5512": Disciplina("Geometria Analítica", 4, {}),
    "INE5406": Disciplina("Sistemas Digitais", 5, {
        "EEL5105"
    }),
    "INE5407": Disciplina("Ciência, Tecnologia e Sociedade", 3, {}),
    "INE5408": Disciplina("Estruturas de Dados", 6, {
        "INE5404"
    }),
    "INE5410": Disciplina("Programação Concorrente", 4, {
        "INE5404"
    }),
    "INE5409": Disciplina("Cálculo Numérico para Computação", 4, {
        "MTM3102", "MTM5512"
    }),
    "MTM5245": Disciplina("Álgebra Linear", 4, {
        "MTM5512"
    }),
    "INE5411": Disciplina("Organização de Computadores", 6, {
        "INE5406"
    }),
    "INE5417": Disciplina("Engenharia de Software I", 5, {
        "INE5408"
    }),
    "INE5413": Disciplina("Grafos", 4, {
        "INE5408", "INE5403"
    }),
    "INE5415": Disciplina("Teoria da Computação", 4, {
        "INE5408", "INE5403"
    }),
    "INE5416": Disciplina("Paradigmas de Programação", 5, {
        "INE5408"
    }),
    "INE5412": Disciplina("Sistemas Operacionais I", 4, {
        "INE5410", "INE5411"
    }),
    "INE5414": Disciplina("Redes de Computadores I", 4, {
        "INE5404"
    }),
    "INE5419": Disciplina("Engenharia de Software II", 4, {
        "INE5417"
    }),
    "INE5423": Disciplina("Banco de Dados I", 4, {
        "INE5408"
    }),
    "INE5421": Disciplina("Linguagens Formais e Compiladores", 4, {
        "INE5415"
    }),
    "INE5420": Disciplina("Computação Gráfica", 4, {
        "INE5408", "MTM3102", "MTM5245"
    }),
    "INE5418": Disciplina("Computação Distribuída", 4, {
        "INE5412", "INE5414"
    }),
    "INE5422": Disciplina("Redes de Computadores II", 4, {
        "INE5414"
    }),
    "INE5453": Disciplina("Introdução ao TCC", 1, {
        "INE5417"
    }),
    "INE5427": Disciplina("Planejamento e Gestão de Projetos", 4, {
        "INE5417"
    }),
    "INE5426": Disciplina("Construção de Compiladores", 4, {
        "INE5421"
    }),
    "INE5425": Disciplina("Modelagem e Simulação", 4, {
        "INE5405"
    }),
    "INE5430": Disciplina("Inteligência Artificial", 4, {
        "INE5405", "INE5413", "INE5416"
    }),
    "INE5424": Disciplina("Sistemas Operacionais II", 4, {
        "INE5412"
    }),
    "INE5433": Disciplina("Trabalho de Conclusão de Curso I (TCC)", 6, {
        "INE5453", "INE5427"
    }),
    "INE5432": Disciplina("Banco de Dados II", 4, {
        "INE5423"
    }),
    "INE5429": Disciplina("Segurança em Computação", 4, {
        "INE5403", "INE5414"
    }),
    "INE5431": Disciplina("Sistemas Multimídia", 4, {
        "INE5414"
    }),
    "INE5428": Disciplina("Informática e Sociedade", 4, {
        "INE5407"
    }),
    "INE5434": Disciplina("Trabalho de Conclusão de Curso II (TCC)", 9, {
        "INE5433"
    })
}
