class Disco:
    
    def __init__(self):
        self.n_discos = 0
        self.iniciar_jogo = False
        self.movimentos = 0
        self.ctrl = False


    def quantDisco(self):
        self.iniciar_jogo
        self.n_discos
        self.n_discos = 0
        while (self.iniciar_jogo == False):

            self.ctrl = input("\nInforme qual a quantidade de disco: ")

            for i in range(100):
                if self.ctrl == i.__str__():
                    self.n_discos = self.ctrl

            if self.n_discos != "" and int(self.n_discos) >= 3:
                self.iniciar_jogo = True
            else:
                print("|------>   A quantidade minima de disco para iniciar o jogo deve ser >= 3 disco.")


        