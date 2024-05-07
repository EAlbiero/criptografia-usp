import hashlib
import math
import random as rd


class Util():

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
            if Util.miller_rabin(p, 10):
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

    def calcula_chave_secreta(phi: int):
        """
        Calcula uma chave secreta s para o algoritmo RSA tal que
        mdc(s, phi) = 1
        """

        # Calculei s 'sorteando' possíveis valores até achar mdc(s, phi) = 1. Pensei
        # em procurar os números em ordem crescente para tentar melhorar a eficiência,
        # mas achei que usando randint poderia tirar alguma possível tendência no valor
        # da chave
        while True:
            # Checamos apenas os números ímpares  
            s = 2*rd.randint(1, phi//2) - 1
            if math.gcd(phi, s) == 1:
                return s
            
    def calcula_chave_publica(phi: int, s: int):
        """
        Calcula uma chave pública p para o algoritmo RSA tal que
        s*p = 1mod(phi)
        """
        return pow(s, -1, phi)

    def aplica_rsa_oaep(msg: int, r_oaep: int):
        """
        Aplica o algoritmo RSA OAEP para a mensagem msg usando como seed r_oaep. Devolve
        a saída do algoritmo.
        """

        # Gerei primos de 256 bits ao invés de 128 como o enunciado pede porque sem isso
        # a volta do RSA não funcionava, pois X||Y tem 256 bits > n = q*r.
        # Seguindo o 'padrão' usado para G e H, os 128 bits faltantes foram preenchidos com 0
        q = Util.calcula_primo(((((((msg << 32) | msg) << 32) | msg) << 32) | msg)<<128)
        r = Util.calcula_primo(q+2)
        n = q*r
        g = hashlib.sha3_256()
        h = hashlib.sha3_256()

        g.update( (r_oaep << 128).to_bytes(256) )
        x = (msg << 96) ^ (int(g.hexdigest(), 16) >> 128)

        h.update((x << 128).to_bytes(256))
        y = (int(h.hexdigest(), 16) >> 128) ^ r_oaep
        

        phi = (q-1)*(r-1)
        s = Util.calcula_chave_secreta(phi)
        p = Util.calcula_chave_publica(phi, s)

        
        entrada_rsa = (x << 128) | y

        return pow(entrada_rsa, p, n)
    


