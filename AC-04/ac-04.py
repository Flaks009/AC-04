class Pessoa:

    def __init__(self, nome, cpf, dataNascimento):

        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento



class Matricula(Pessoa):

    def __init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status = False):

        Pessoa.__init__(self, nome, cpf, dataNascimento)
        self.RA = self.gera_RA()
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
            self.RA = int (guia_RA) + 1
    
        
            ListaRA.close()

        with open("ListaRA.txt", 'a') as ListaRA:

            ListaRA.write(str('\n{}' .format(self.RA)))

            ListaRA.close()

        return self.RA
        
    def exibe_dados_matricula(self):

        print(self.RA, self.nome)


class Aluno(Pessoa):

    def __init__ (self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status = False, notas = {}, faltas = 0):

        Matricula.__init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status=False)

        self.notas = {}

        self.faltas = faltas



class Professor(Pessoa):

    def __init__(self, nome, cpf, dataNascimento, RF, salario, materiaMinistrada, dataContratacao):

        Pessoa.__init__(self, nome, cpf, dataNascimento)
        self.RF = self.gera_RF()
        self.salario = salario
        self.materiaMinistrada = materiaMinistrada
        self.dataContratacao = dataContratacao

    def gera_RF(self):
        
        with open("ListaRF.txt", 'r') as ListaRF:

            line = ListaRF.readlines()

            ultimo = len(line)
            guia_RF = line[ultimo - 1]
            self.RF = int (guia_RF) + 1
    
        
            ListaRF.close()

        with open("ListaRF.txt", 'a') as ListaRF:

            ListaRF.write(str('\n{}' .format(self.RF)))

            ListaRF.close()

        return self.RF

class Curso:

    def __init__(self, nomeCurso, turno, preco, cargaHoraria, materias = [], professores = []):

        self.nomeCurso = nomeCurso

        self.turno = turno

        self.preco = preco

        self.cargaHoraria = cargaHoraria

        self.materias = materias

        self.professores = professores

x = Matricula('Bruno', 44790119866, '18/10/1995', 'C', 'Rua Friedrich', 983673622, '09/09/2018', True)
print(x.RA)

y = Professor('Bruno', 123456, 0, '18/11/1056', 1200, 'Nada', '11/05/2018')
print(y.RF)