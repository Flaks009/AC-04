class curso:
    listaCursos = []
    def __init__(self, nome, periodo, cod_curso = 0, disciplinas = [], status = False):
        self.nome = nome
        self.periodo = periodo
        self.cod_curso = len(self.listaCursos) + 1
        self.disciplinas = {}
        self.status = False
        

    def cadastraCurso(self):
            
        self.listaCursos.append([self.nome, self.cod_curso, self.periodo, self.disciplinas])
        self.status = True
            

        with open('cursos.txt', 'a+') as Cursos:

            Cursos.write("--------------------------------------------\n")
            Cursos.write("Nome do curso: {}\n" .format(self.nome))
            Cursos.write("Código do curso: {}\n" .format(self.cod_curso))
            Cursos.write("Período: {}\n" .format(self.periodo))
            Cursos.write("Disciplinas: {}\n" .format(self.disciplinas))
            Cursos.write("--------------------------------------------\n")

                
            Cursos.close()
        
    def exibeCurso(self):

        cod_busca = int(input("Código do curso:"))          

        if cod_busca == 0:
            print(self.listaCursos)
        
        else:
            print(self.listaCursos[cod_busca])

    def desativaCurso(self):
        pass



ADS = curso("ADS", "Manhã")
ADS.cadastraCurso()
Ingles = curso("Ingles", "Noite")
Ingles.cadastraCurso()
SI = curso("SI", "Manhã")
SI.cadastraCurso()
Banco = curso("Banco", "Noite")
Banco.cadastraCurso()

ADS.exibeCurso()
