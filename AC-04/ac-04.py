class Pessoa:

    def __init__(self, nome, cpf, dataNascimento):

        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento



class Matricula(Pessoa):

    def __init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status = False):

        Pessoa.__init__(self, nome, cpf, dataNascimento)
        self.RA = 0
        self.turma = turma
        self.end = end
        self.telefone = telefone
        self.dataMatricula = dataMatricula
        self.status = status

    def gera_RA(self):
        
        with open("ListaRA.txt", 'r') as ListaRA:

            line = ListaRA.readlines()

            ultimo = len(line)
            guia_RA = line[ultimo - 1]
            guia_RA = int(guia_RA)
            self.RA = guia_RA + 1

            ListaRA.close()

        with open("ListaRA.txt", 'a') as ListaRA:

            ListaRA.write(str('{}\n' .format(self.RA)))

            ListaRA.close()


class Aluno(Pessoa):

    def __init__ (self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status = False, notas = {}, faltas = 0):

        Matricula.__init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status=False)

        self.notas = {}

        self.faltas = faltas



class Professor(Pessoa):

    def __init__(self, nome, cpf, dataNascimento, RF, salario, materiaMinistrada, dataContratacao):

        Pessoa.__init__(self, nome, cpf, dataNascimento)

        self.RF = RF

        self.salario = salario

        self.materiaMinistrada = materiaMinistrada

        self.dataContratacao = dataContratacao

 #continua logo abaixo da class professor

    def gera_RF(self):
        
        with open("ListaRF.txt", 'r') as ListaRF:

            line = ListaRF.readlines()

            ultimo = len(line)
            guia_RF = line[ultimo - 1]
            guia_RF = int(guia_RF)
            self.RF = guia_RF + 1

            ListaRF.close()

        with open("ListaRF.txt", 'a') as ListaRF:

            ListaRF.write(str('{}\n' .format(self.RF)))

            ListaRF.close()

class Curso:

    def __init__(self, nomeCurso, turno, preco, cargaHoraria, materias = [], professores = []):

        self.nomeCurso = nomeCurso

        self.turno = turno

        self.preco = preco

        self.cargaHoraria = cargaHoraria

        self.materias = materias

        self.professores = professores

        

x = Matricula('Bruno', 44790119866, '18/10/1995', 'C', 'Rua Friedrich', 983673622, '09/09/2018', True)
x.gera_RA()
y = Professor('Peter', 12345678901, '15/08/1962', 0, 'xxxx,xx', 'Escalada', '11/12/1991')
y.gera_RF()
