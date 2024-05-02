import hashlib
import math
import random


class Util():

    def gera_entrada(m: int):
        """
        Recebe um int m como entrada e devolve uma string correspondente a
        concatenação de cada dígito na base 2, sendo utilizados 4 bits por 
        dígito.

        Exemplo: gera_entrada(15) ---> '00010101'
        """

        m = str(m)
        msg_final = format(int(m[0]), '04b')
        for i in m[1:]:
            novos_bits = format(int(i), '04b')
            msg_final  += novos_bits

        return msg_final

    def calcula_primo(t: int):
        """
        Calcula e devolve o menor número primo maior ou igual do que t utilizando
        o algoritmo Miller-Rabin.
        """
        return 0

    def miller_rabin(p: int):
        """
        Utiliza o algoritmo de Miller-Rabin com, 
        """
        return 0







