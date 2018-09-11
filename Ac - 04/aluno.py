class Aluno:
    def __init__(self, nome, cpf, dataNascimento, endereco, telefone, cadastrado = True):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.telefone = telefone
        self.cadastrado = True

    def cadastrarAluno(self):
        c = 0
        d = 0
        f = open('alunos.txt', '+a')
        print("Cadastre um aluno!")

        n = input("Digite o nome do(a) aluno(a): ")
        m = input("Digite o  RA  do(a) aluno(a): ")

        c = "Aluno(a): " + n + "\n"
        d = "RA......: " + m + "\n"
        f.write("--------------------------------------------\n")
        f.write(c)
        f.write(d)
        f.write("--------------------------------------------\n")

    def editarAluno(self):
        g = open('dados_alunos.txt', '+a')
        edi = str(input("Caso deseje alterar  os dados do aluno, digite SIM: "))

        if edi in ['sim', 's', 'S', 'SIM']:
            self.nome = str(input("Nome: "))
            self.cpf = str(input("CPF: "))
            self.dataNascimento = str(input("Data de Nascimento: "))
            self.endereco = str(input("Endereço: "))            
            self.telefone = str(input("Telefone: "))

            g.write("--------------------------------------------\n")
            g.write("Nome..............: {}\n" .format(self.nome))
            g.write("CPF...............: {}\n" .format(self.cpf))
            g.write("Data de Nascimento: {}\n" .format(self.dataNascimento))
            g.write("Endereço..........: {}\n" .format(self.endereco))
            g.write("Telefone..........: {}\n" .format(self.telefone))
            g.write("--------------------------------------------\n")

            
            print("Dados atualizados!")

        else:
            print("Dados não foram alterados!")    


    def desabilita(self):
        self.cadastrado = False
        #print(self.cadastrado)

    def habilitar(self):
        self.cadastrado = True
        #print(self.cadastrado)


y = Aluno("Renato", 37804343850, "09/12/1989", "rua Augusto Baer", 976334348)
y.cadastrarAluno()
y.editarAluno()
y.desabilita()
y.habilitar()
