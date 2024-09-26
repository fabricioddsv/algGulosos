#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Mediana de dois arrays
def mediana(a: list, b: list, initA: int=None, endA: int=None, initB: int=None, endB: int=None) -> int:
    if initA is None:
        initA = initB = 0
        endA = endB = len(a)
    meioA = int((initA + endA) / 2)
    meioB = int((initB + endB) / 2)
    
    if a[meioA] == b[meioB]: return a[meioA]
    
    if endA - initA == 1: return int((a[initA] + b[initB]) / 2)
    
    elif endA - initA == 2:
        r = [max(a[initA], b[initB]), min(a[initA + 1],
        b[initA + 1])]
        return int(sum(r) / 2)
    
    elif a[meioA] < b[meioB]: return mediana(a, b, meioA + 1, endA, initB, meioB)
    
    else: return mediana(a, b, initA, meioA, meioB + 1, endB)
    
tamArr = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(mediana(A, B))


###Achar o menor elemento faltante de um array.
def menor(a: list, init: int=None, fim: int=None) -> int:
    if init == None or fim == None:
        init = 0
        fim = len(a)
    
    meio = int((fim + init) / 2)
    
    if fim - init == 1: return meio if a[meio] != meio else meio + 1
    
    if a[meio] == meio:
        init = meio
    else: fim = meio
        
    return menor(a, init, fim)

A = list(map(int, input().split()))
print(menor(A))


###Encontre o teto e o piso de um número em um array ordenado de inteiros.
def encontrar(a: list, k: int, init: int=None, fim: int=None) -> dict:
    if init is None:
        init = 0
        fim = len(a)
    meio = int((init + fim) / 2)
    
    if a[meio] == k: return {"teto": a[meio], "piso": a[meio]}
    
    elif fim - init == 1:
        if a[init] < k: return {"teto": -1, "piso": a[init]}
        else: return {"teto": a[init], "piso": -1}

    elif a[meio] < k and fim - init > meio + 1:
        if a[meio + 1] > k: return {"teto": a[meio + 1], "piso": a[meio]}
    
    elif a[meio - 1] < k and a[meio] > k: return {"teto": a[meio], "piso": a[meio - 1]}
    
    if a[meio] > k: fim = meio
        
    else:
        init = meio
        return encontrar(a, k, init, fim)
def p(a: list) -> None:
    tam = 11
    for i in range(tam):
        r= encontrar(a, i)
        print(f"k = {i} --> teto = {r['teto']}, piso = {r['piso']}")
      
a = list(map(int, input().split()))
p(a)


# In[ ]:





# In[ ]:




