from disco import Disco
import sys

disco = Disco()

class Torre:

    def __init__(self):
        self.torre_a = []
        self.torre_b = []
        self.torre_c = []

    def init(self):
        for i in range(0, int(disco.n_discos)):
            self.torre_a.append(int(disco.n_discos) - i)
        
        return True


    def printTorre(self, arrayTorre, torre):
        print('{:>{}}'.format("\nTorre ", (disco.n_discos)) + torre)
        for n in reversed(arrayTorre):
            pino = ""
            for i in range(n):
                pino += "#"
            print('{:>{}}'.format(pino, disco.n_discos) + '{:<{}}'.format(pino, disco.n_discos))




    def verificarMovimento(self, str):
        strView = ""
        if str == "a" or str == "A":
            strView = "B ou C"
        elif (str == "b" or str == "B"):
            strView = "A ou C"
        elif (str == "c" or str == "C"):
            strView = "A ou B"
        return strView


    def movimentar(self, torre, operacao, valorMove):
        
        movimento = ""

        if (torre == "a" or torre == "A") and operacao == 1:
            if self.validaAlocacao(self.torre_a, operacao, valorMove):
                movimento = self.torre_a.pop()

        elif (torre == "b" or torre == "B") and operacao == 1:
            if self.validaAlocacao(self.torre_b, operacao, valorMove):
                movimento = self.torre_b.pop()

        elif (torre == "c" or torre == "C") and operacao == 1:
            if self.validaAlocacao(self.torre_c, operacao, valorMove):
                movimento = self.torre_c.pop()

        elif (torre == "a" or torre == "A") and operacao == 2:
            if self.validaAlocacao(self.torre_a, operacao, valorMove):
                self.torre_a.append(valorMove)
                movimento = valorMove

        elif (torre == "b" or torre == "B") and operacao == 2:
            if self.validaAlocacao(self.torre_b, operacao, valorMove):
                self.torre_b.append(valorMove)
                movimento = valorMove
        elif (torre == "c" or "torre" == "C") and operacao == 2:
            if self.validaAlocacao(self.torre_c, operacao, valorMove):
                self.torre_c.append(valorMove)
                movimento = valorMove
        return movimento


    def inputValue(self):
        saida = ""
        movSaida = ""
        entrada = ""
        movEntrada = ""
        disco.ctrl = False
        reset = False
        novaPartida = False

        while saida == "":

            if movSaida == "" and disco.ctrl != False:
                print("A Torre informada esta errada, por favor informe uma torre valida.")
                disco.ctrl = False
            else:
                print("\nPara resetar a jogada digite [ reset ] ")
                print("Para iniciar novamente a partida digite [ iniciar ] ")
                print("Para imprimir o resultado anterior digite [ print ]\n")
                saida = input("Informe a Torre de Saida: ")

                if saida == "reset":
                    reset = True
                elif saida == "print":
                    self.printResult()
                    reset = True
                elif saida == "iniciar":
                    novaPartida = True
                else:
                    movSaida = self.verificarMovimento(saida)
                    disco.ctrl = True

            if not reset and not novaPartida:
                saida = self.movimentar(saida, 1, "")

        disco.ctrl = False

        while entrada == "" and (not reset and not novaPartida):

            if movEntrada == "" and disco.ctrl != False:
                print("A Torre informada esta errada, por favor informe uma torre valida.")
                disco.ctrl = False
            else:
                entrada = input("Informe a Torre de Entrada " + movSaida + ": ")

                if entrada == "reset":
                    self.iniciar(self)
                    reset = True
                    
                elif entrada == "print":
                    self.printResult()
                    reset = True

                elif entrada == "iniciar":
                    self.iniciar(self)
                    novaPartida = True
                    
                else:
                    movEntrada = self.verificarMovimento(entrada)

                    if movSaida == movEntrada:
                        print("Essa joganda no e valida. Você deve muda sua jogada.")
                        disco.ctrl = False
                    else:
                        disco.ctrl = True

            if disco.ctrl:
                entrada = self.movimentar(entrada, 2, saida)
            else:
                entrada = ""

        if reset:
            self.inputValue()
        elif novaPartida:
            self.iniciar()


    def validaAlocacao(self, torre, operacao, valorMove):
        length = torre.__len__()

        if length == 0 and operacao == 1:
            print("Esta torre esta vazia. Você deve muda sua jogada.")
            return False
        elif length > 0 and operacao == 2:
            if valorMove < torre[length - 1]:
                return True
            else:
                print("Os ultimo disco que esta na torre è menor que o disco [", valorMove, "]. Você deve muda sua jogada.")
                return False
        else:
            return True


    def validaResultado(self):
        vencedor = False

        if int(self.torre_a.__len__()) == 0 and int(self.torre_b.__len__()) == 0 and int(self.torre_c.__len__()) == int(self.n_discos):
            vencedor = True
        elif int(self.torre_a.__len__()) == 0 and int(self.torre_b.__len__()) == int(self.n_discos) and int(self.torre_c.__len__()) == 0:
            vencedor = True

        return vencedor


    def fimJogo(self):
        print("PARABÉNS, VOCÊ GANHOU...\nAgora o que voce acha de aumentar o desafio.\n")

        if input("Para uma nova partida digite [ iniciar ]: ") == "iniciar":
            self.iniciar()
        else:
            print("Que pena, entao ate a proxima... bye bye\n")
            sys.exit(0)


    def move(self):
        resultado = False

        while not resultado:
            self.inputValue()
            self.movimentos += 1
            self.printResult()
            resultado = self.validaResultado()
        else:
            self.fimJogo()


    def printResult(self):
        print("\n")
        print("Torre A: ", self.torre_a)
        print("Torre B: ", self.torre_b)
        print("Torre C: ", self.torre_c)
        print("Movimentos: ", self.movimentos)

        self.printTorre(self.torre_a, "A")
        self.printTorre(self.torre_b, "B")
        self.printTorre(self.torre_c, "C")
        print("\n")


    def iniciar(self):

        self.n_discos = 0
        self.iniciar_jogo = False
        self.movimentos = 0
        self.torre_a = []
        self.torre_b = []
        self.torre_c = []

        disco.quantDisco()
        self.init()

        print("\n     PRONTO VAMOS INCIAR O JOGO \n")
        self.printResult()
        self.move()
