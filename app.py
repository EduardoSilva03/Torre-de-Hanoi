def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

if __name__=='__main__':
    n = int(input("Digite o número de discos: "))
    origem = input("Digite a torre de origem (A, B ou C): ").upper()
    destino = input("Digite a torre de destino (A, B ou C): ").upper()
    auxiliar = input("Digite a torre auxiliar (A, B ou C): ").upper()
    
    if origem == destino or origem == auxiliar or destino == auxiliar:
        print("Erro: As torres de origem, destino e auxiliar devem ser distintas.")
    else:
        torre_hanoi(n, origem, destino, auxiliar)