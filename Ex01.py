class triangulo:
    def __init__(self, perimetro = 0):
        self.Main()
        self.perimetro = perimetro

    def calcPerimetro(self):

        self.perimetro = self.LadoA + self.LadoB + self.LadoC

        print("Perímetro = {} " .format(self.perimetro))
        
    
    def getMaiorLado(self):
        
        maior = 0

        if self.LadoA > self.LadoB and self.LadoA > self.LadoC:
            maior = self.LadoA

        elif self.LadoB > self.LadoA and self.LadoB > self.LadoC:
            maior = self.LadoB
        
        else:
            maior = self.LadoC

        print ("O lado maior é: {} " .format(maior))

    def Main(self):

        self.LadoA = int(input("Insira o valor do Lado A: "))
        self.LadoB = int(input("Insira o valor do Lado B: "))
        self.LadoC = int(input("Insira o valor do Lado C: "))

    def getArea(self):
        
        semip = (self.perimetro / 2)
        area = ((semip*(semip-self.LadoA)*(semip*(semip-self.LadoB)*(semip*(semip-self.LadoC)))))**(1/2)

        print("Área do Triângulo = {}" . format(area))
        

