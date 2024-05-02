
from Util import Util


def main():

    N = 256
    nusp = int(input("Informe a mensagem (nº USP) que será utilizada: "))

    msg = Util.gera_entrada(nusp)
    print(msg)

    q = Util.calcula_primo(int(4*msg))
    r = Util.calcula_primo(q+2)






main()
