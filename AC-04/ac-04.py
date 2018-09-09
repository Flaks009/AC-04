class Pessoa:

    def __init__(self, nome, cpf, dataNascimento):

        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento



class Matricula(Pessoa):

    def __init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone, dataMatricula, status = False):

        Pessoa.__init__(self, nome, cpf, dataNascimento)
    
        self.RA = RA
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

        self.RF = RF

        self.salario = salario

        self.materiaMinistrada = materiaMinistrada

        self.dataContratacao = dataContratacao



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
print(x.RA)