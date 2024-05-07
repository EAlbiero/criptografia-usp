from Util import Util
import hashlib
import random as rd

def main():

    msg = int(input("Informe a mensagem (nº USP) que será utilizada: "))
    r_oaep = rd.randint(1, 2**128 - 1) # R usado no processo de padding/unpadding

    print(f"\n{20*'--'}\n")

    # Gerei primos de 256 bits ao invés de 128 como o enunciado pede porque sem isso
    # a volta do RSA não funcionava, pois X||Y tem 256 bits > n = q*r.
    # Seguindo o 'padrão' usado para G e H, os 128 bits faltantes foram preenchidos com 0
    q = Util.calcula_primo(((((((msg << 32) | msg) << 32) | msg) << 32) | msg)<<128)
    r = Util.calcula_primo(q+2)
    n = q*r
    
    print(f"Mensagem utilizada: {msg}\n")
    print(f"q: {q}")
    print(f"r: {r_oaep}")

    g = hashlib.sha3_256()
    h = hashlib.sha3_256()

    g.update( (r_oaep << 128).to_bytes(256) )
    x = (msg << 96) ^ (int(g.hexdigest(), 16) >> 128)

    h.update((x << 128).to_bytes(256))
    y = (int(h.hexdigest(), 16) >> 128) ^ r_oaep
    

    phi = (q-1)*(r-1)
    s = Util.calcula_chave_secreta(phi)
    p = Util.calcula_chave_publica(phi, s)

    print("\nChaves utilizadas para o algoritmo RSA:")
    print(f"Chave secreta: {s}")
    print(f"Chave pública: {p}")

    
    
    entrada_rsa = (x << 128) | y
    print("Entrada do algoritmo RSA (X||Y):", entrada_rsa)

    saida_rsa = pow(entrada_rsa, p, n)
    print(f"\nSaída do algoritmo RSA: {saida_rsa}")
    
    entrada_unpadding = pow(saida_rsa, s, n)

    x2 = entrada_unpadding >> 128
    y2 = (entrada_unpadding) ^ (x2 << 128)
    g2 = hashlib.sha3_256()
    h2 = hashlib.sha3_256()

    h2.update((x2 << 128).to_bytes(256))
    r_oaep2 = (int(h2.hexdigest(), 16) >> 128) ^ y2
    g2.update((r_oaep2 << 128).to_bytes(256))

    saida_unpadding = (x2 ^ (int(g2.hexdigest(), 16) >> 128)) >> 96
    print(f"Inversa do algoritmo RSA OAEP: {saida_unpadding}")


    ####################################################################
    # Itens 4 e 5, comparando a saída criptografada com bits modificados
    ####################################################################


    print(f"\n{20*'--'}\n")

    print("Usando o complemento do primeiro bit à esquerda:")

    # msg tem 32 bits, para conseguir 10000... basta tomar 2^31
    saida_complemento1 = Util.aplica_rsa_oaep(msg ^ 2**31, r_oaep)
    hamming1 = Util.hamming(saida_unpadding, saida_complemento1)

    print("Saída alterando o primeiro bit à esquerda:", saida_complemento1)
    print("Diferença comparado com a saída original:", hamming1)



    print(f"\n{20*'--'}\n")

    print("Usando o complemento dos dois primeiros bits à esquerda:")

    # msg tem 32 bits, para conseguir 11000... basta tomar 2^31 + 2^30
    saida_complemento2 = Util.aplica_rsa_oaep(msg ^ (2**31 + 2**30), r_oaep)
    hamming2 = Util.hamming(saida_unpadding, saida_complemento2)

    print("Saída alterando o primeiro bit à esquerda:", saida_complemento2)
    print("Diferença comparado com a saída original:", hamming2)

main()
