
def carro(fim, tanque_cheio, qtd_paradas, paradas):
    paradas.append(fim)
    tanque = tanque_cheio
    percorrer = 0
    contador = 0
    for i in range(len(paradas) - 1):
        if i > 0: percorrer = paradas[i + 1] - paradas[i]
        
        else: percorrer = paradas[i]
    
        if tanque - percorrer <= 0:
            tanque = tanque_cheio
            contador += 1

        if percorrer > tanque_cheio: return -1
        
        else: tanque -= percorrer
      
    return contador


fim = int(input())
tanque_cheio = int(input())
qtd_paradas = int(input())
paradas = list(map(int, input().split()))
print(carro(fim, tanque_cheio, qtd_paradas, paradas))