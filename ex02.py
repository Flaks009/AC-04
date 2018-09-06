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
        
        

class Aluno(Pessoa):
    def __init__ (self, nome, cpf, dataNascimento, RA, turma, end, telefone, notas = {}, faltas = 0):
        Matricula.__init__(self, nome, cpf, dataNascimento, RA, turma, end, telefone)
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