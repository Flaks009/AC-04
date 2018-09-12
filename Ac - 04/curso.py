class curso:
    listaCurso = {}
    cursosCadastrados = []

    def __init__(self, nome, periodo, disciplinas = [], status = "Desativado"):

        self.nome = nome + "*"

        self.periodo = periodo

        self.disciplinas = disciplinas

        self.status = "Desativado"

        self.listaCurso[self.nome] = {"Nome":self.nome, "Periodo":self.periodo, "Disciplina":self.disciplinas, "Status":self.status}

    def cadastraCurso(self):

        if self.listaCurso[self.nome]["Nome"] == "Desativado":
            self.listaCurso[self.nome]["Status"] = "Ativado"
        
        self.cursosCadastrados.append(self.nome)
        self.listaCurso[self.nome]["Status"] = "Ativado"
        
        with open('cursos.txt', 'a+') as Cursos:

            Cursos.write(self.nome + ";" + self.periodo + ";")

            Cursos.close()

        

    def Cursos(self):

        with open('cursos.txt', 'r') as Cursos:

            for item in Cursos:
                item = item.splitlines()
                for item in item:
                    item2 = item.split(";")
                    if '*' in item2:
                        self.cursosCadastrados.append(item2)
        Cursos.close()

        return self.cursosCadastrados

    def exibeCursos(self):

        for curso in self.cursosCadastrados:
            print("*"*20)
            print("Nome: {}" .format(self.listaCurso[curso]["Nome"]))
            print("Periodo: {}" .format(self.listaCurso[curso]["Periodo"]))
            print("Disciplinas {}" .format(self.listaCurso[curso]["Disciplina"]))
            print("Status {}" .format(self.listaCurso[curso]["Status"]))
            print("*"*20)


    def alteraStatus(self):
        if self.listaCurso[self.nome]["Status"] == "Ativado":
            self.listaCurso[self.nome]["Status"] = "Desativado"

        elif self.listaCurso[self.nome]["Status"] == "Desativado":
            self.listaCurso[self.nome]["Status"] = "Ativado"


ADS = curso("ADS", "Manha",["Logica", "Programacao"])
ADS.cadastraCurso()
Banco = curso("Banco", "Noite", ["Banco de dados", "Linguagem SQL"])
Banco.cadastraCurso()
SI = curso("SI", "Tarde", ["Modelagem", "Gestao"])
SI.cadastraCurso()
Banco.alteraStatus()
SI.exibeCursos()

