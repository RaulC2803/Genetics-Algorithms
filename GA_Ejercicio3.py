import random
import math
from copy import deepcopy

generacion1 = [[random.random()for x in range(10)]for x in range(3)]

class cromosoma:
    binario = ''
    decimal = 0
    
    def __init__(self,x):
        self.binario = x
        self.decimal = int(self.binario,2)
    
    def recaldec(self,b):
        self.binario = b
        self.decimal = int(self.binario,2)

    def func(self):
        f = abs((self.decimal-5)/(2 + math.sin(self.decimal)))
        return f
        

def generarCromosoma(g):
    generacion = []
    for i in range(len(g)):
        cromosomas = []
        binario = ''
        for j in range(len(g[0])):
            if g[i][j] < 0.5:
                binario += '0'
            else:
                binario += '1'

            if j == 4 or j == 9:
                cromosomas.append(cromosoma(binario))
                binario = ''
        generacion += cromosomas[:]
    return generacion

g = generarCromosoma(generacion1)


def imprimirCro(g):
    print("    Binario   Decimal")
    for i in range(len(g)):
        print("#" + str(i + 1) + "   "+ g[i].binario+ "       " + str(g[i].decimal))

print("\nPrimeros Individuos: \n")
imprimirCro(g)

def FuncionParejas(g2):
    comparados = []
    g = deepcopy(g2)
    for i in range(0,len(g2)-1):
        r1 = random.randint(0,len(g2)-1)
        r2 = i
        p = random.randint(1,4)
        while r1 in comparados or r2 == r1:
            r1 = random.randint(0,len(g2)-1)
        if r2 not in comparados:
            comparados.append(r1)
            comparados.append(r2)   
            n1 = g[r2].binario[p:]  
            n2 = g[r1].binario[p:]  
            g[r1].recaldec(g[r1].binario[:p] + n1)
            g[r2].recaldec(g[r2].binario[:p] + n2)
        else:
            while r2 in comparados or r2 == r1:
                r2 = random.randint(0,len(g2)-1)
            comparados.append(r1)
            comparados.append(r2)
            n1 = g[r2].binario[p:]
            n2 = g[r1].binario[p:]
            g[r1].recaldec(g[r1].binario[:p] + n1)
            g[r2].recaldec(g[r2].binario[:p] + n2)
        if len(comparados) == len(g2): break
    return g

g2 = FuncionParejas(g)

print("\nParejas: \n")
imprimirCro(g2)

def FuncionMutacion(g2):
    g = deepcopy(g2)
    for i in range(0,len(g2)):
        
        r2 = random.random()
        if 0.20 > r2:
            r1 = random.randint(0,4)
            s = ''
            for j in range(len(g2[0].binario)):
                if j == r1:
                    if g[i].binario[r1] == '1':  s += '0'
                    else: s += '1'
                else:
                    s += g[i].binario[j]
            g[i].recaldec(s)
            s = ''
    
    return g

g3 = FuncionMutacion(g)

print("\nMutacion: \n")
imprimirCro(g3)