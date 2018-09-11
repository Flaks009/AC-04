class disciplina:
    def __init__(self, nome, cargaHoraria, percentualPratico, percentualTeorico, professor):
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.percentualPratico = percentualPratico
        self.percentualTeorico = percentualTeorico
        self.professor = professor

        auxDisciplinas = []
        nomeDB = {}
        cargaHorariaDB = {}
        percPraticoDB = {}
        percTeoricoDB = {}
        professorDB = {}

        with open("disciplinas.txt") as f:
            aux = f.read().splitlines()
            f.close()

        for item in aux:
            auxDisciplinas = item.split(";")
            nomeDB[auxDisciplinas[0]] = auxDisciplinas[0]
            cargaHorariaDB[auxDisciplinas[0]] = auxDisciplinas[1]
            percPraticoDB[auxDisciplinas[0]] = auxDisciplinas[2]
            percTeoricoDB[auxDisciplinas[0]] = auxDisciplinas[3]
            professorDB[auxDisciplinas[0]] = auxDisciplinas[4]

        if self.nome in nomeDB:
            print("Disciplina já cadastrada!\n")
        else:        
            DB = open("disciplinas.txt", "a")

            nomeDB[self.nome] = self.nome
            cargaHorariaDB[self.nome] = self.cargaHoraria
            percPraticoDB[self.nome] = self.percentualPratico
            percTeoricoDB[self.nome] = self.percentualTeorico
            professorDB[self.nome] = self.professor

            for j in nomeDB:
                DB.write(nomeDB[j] + ';' + cargaHorariaDB[j] + ';' + percPraticoDB[j] + ';' + percTeoricoDB[j] + ';' + professorDB[j] + '\n')

            DB.close()

            print("Disciplina cadastrada com sucesso!\n")
