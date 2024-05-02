import hashlib
import math
import random as rd


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

        if t % 2 == 0:
            p = t+1
        else:
            p = t

        while True:
            if Util.miller_rabin(p, 40):
                break
            p += 2

        return p

    def miller_rabin(p: int, N: int):
        """
        Utiliza o algoritmo de Miller-Rabin com N interações para determinar se 
        um número p é primo ou não
        """
        
        c = p-1
        t = 0
        while c%2 == 0:
            t += 1
            c //= 2

        for _ in range(N):
            testemunho = rd.randint(1, p-1)
            r = pow(testemunho, c, p)
            
            for _ in range(t):
                aux = pow(r, 2, p)
                if (aux == 1) and not ( (r == 1) or (r == p-1) ):
                    return False
                
                r = aux

        if r != 1:
            return False
        return True







