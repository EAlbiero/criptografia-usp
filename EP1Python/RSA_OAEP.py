
from Util import Util
import hashlib
import math


def main():

    N = 256
    nusp = int(input("Informe a mensagem (nº USP) que será utilizada: "))

    print(f"\n{20*'--'}\n")

    msg = Util.gera_entrada(nusp)
    q = Util.calcula_primo(int(4*msg, 2))
    r = Util.calcula_primo(q+2)
    
    print(f"Mensagem utilizada ({len(msg)} bits): {msg}\n")
    print(f"q: {q}")
    print(f"r: {r}")

    g = hashlib.sha3_256()
    h = hashlib.sha3_256()

    g.update( (r << 128).to_bytes(256) )
    x = (int(msg, 2) << 96) ^ (int(g.hexdigest(), 16) >> 128)

    h.update((x << 128).to_bytes(256))
    y = (int(h.hexdigest(), 16) >> 128) ^ r
    
    entrada_rsa = (x << 128) | y  

    






main()
