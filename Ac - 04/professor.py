class professor:
    listaProfessores = []
    def __init__(self, nome, cpf, dataNascimento, endereco, telefone, status = 'Ativo'):
        self.nome = nome
        self. cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self. telefone = telefone
        self.status = 'Ativo'
    
    def Cadastrar (self):
        
        self.nome = input("Digite o nome do professor: ").upper()
        self.cpf = input("Digite o CPF do professor: ")
        self.dataNascimento = input("Digite a data de nascimento do professor: ")
        self.endereco = input("Digite o endereço: ").upper()
        self.telefone = input("Digite o telefone: ")

    
    def listas(self):
        self.listaProfessores = []
        self.listaProfessores.append([self.nome, self.cpf, self.dataNascimento, self.endereco, self.telefone])
        
        with open ('professores.txt', 'a+') as Prof:
            Prof.write("--------------------------------------------\n")
            Prof.write("Nome do professor: {}\n" .format(self.nome))
            Prof.write("CPF: {}\n" .format(self.cpf))
            Prof.write("Data de nascimento: {}\n" .format(self.dataNascimento))
            Prof.write("Endereço: {}\n" .format(self.endereco))
            Prof.write("Telefone: {}\n" .format(self.telefone))
            Prof.write("--------------------------------------------\n")


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
                return doc
            
            with open ('professores.txt', 'a+') as Prof:
                Prof.write("--------------------------------------------\n")
                Prof.write("Nome do professor: {}\n" .format(self.nome))
                Prof.write("CPF: {}\n" .format(self.cpf))
                Prof.write("Data de nascimento: {}\n" .format(self.dataNascimento))
                Prof.write("Endereço: {}\n" .format(self.endereco))
                Prof.write("Telefone: {}\n" .format(self.telefone))
                Prof.write("--------------------------------------------\n")
        
    def cancela_cad(self):
        loc_cpf1 = input("Buscar CPF para cancelar o cadastro: ")
        if loc_cpf1 in self.cpf:
            self.status = 'Cancelado'
            print('Status do cadastro: ', self.status)
        else:
            print("CPF não cadastrado!")
        

    def ativa_cad(self):
        loc_cpf2 = input("Buscar CPF para ativar o cadastro: ")
        if loc_cpf2 in self.cpf:
            self.status = 'Ativo'
            print('Status do cadastro: ', self.status)
        else:
            print("CPF não cadastrado!")

     

p = professor('Irineu',"045.548.658-98","05/04/1994","SP","994568475")

p.Cadastrar()
print('\n')
print("+-----------------------------------+")
p.listas()
print('\n')
p.editar()
print("+-----------------------------------+")
p.cancela_cad()
print("+-----------------------------------+")
p.ativa_cad()
