class professor:
    listaProfessores = []
    def __init__(self, nome, cpf, dataNascimento, endereco, telefone):
        self.nome = nome
        self. cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self. telefone = telefone
    
    def Cadastrar (self):
        
        self.nome = input("Digite o nome do professor: ").upper()
        self.cpf = input("Digite o CPF do professor: ")
        self.dataNascimento = input("Digite a data de nascimento do professor: ")
        self.endereco = input("Digite o endereço: ").upper()
        self.telefone = input("Digite o telefone: ")

    
    def listas(self):
        self.listaProfessores = []
        self.listaProfessores.append([self.nome, self.cpf, self.dataNascimento, self.endereco, self.telefone])
        return self.listaProfessores

    def editar(self):
        continua = True
        doc = input("Digite o CPF para consulta: ")

        while continua:
            if doc in self.cpf:
                print("+-----------------------------------------+")
                print("|   Digite os novos dados de contato      |")
                print("+-----------------------------------------+") 
                self.endereco = input("Digite o endereço: ").upper()
                self.telefone = input("Digite o telefone: ")
                print("+-----------------------------------+")
                print("|   Cadastro alterado com sucesso!  |")
                print("+-----------------------------------+")

                continua = False
            else:
                print("CPF não cadastrado")
                break
                


        
    

        


p = professor('Irineu',"045.548.658-98","05/04/1994","SP","994568475")

p.Cadastrar()
print('\n')
print('+-------------------+')
p.listas()
print(p.listas())
print('\n')
print('+-------------------+')
p.editar()
print(p.listas())