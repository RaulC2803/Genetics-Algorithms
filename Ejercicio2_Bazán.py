import random
import math
from copy import deepcopy

generacion1 = [[random.random()for x in range(8)]for x in range(4)]

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
    for i in range(4):
        cromosomas = []
        binario = ''
        for j in range(8):

            if g[i][j] < 0.5:
                binario += '0'
            else:
                binario += '1'

            if j == 3 or j == 7:
                cromosomas.append(cromosoma(binario))
                binario = ''
        generacion += cromosomas[:]
    return generacion

def mayor(x,y,g):
    ma = 0
    me = 0;
    if max(g[x].func(),g[y].func()) == g[x].func():
        ma = x;
        me = y;
    else: 
        ma = y
        me = x;
    return ma, me

def seleccion(g2):
    comparados = []
    g = deepcopy(g2)
    for i in range(0,7):

        r1 = random.randint(0,7)
        r2 = i
        while r1 in comparados or r2 == r1:
            r1 = random.randint(0,7)
        if r2 not in comparados:
            ma, me = mayor(r1,r2,g)
            comparados.append(r1)
            comparados.append(r2)
            g[me] = g[ma]
        else:
            while r2 in comparados or r2 == r1:
                r2 = random.randint(0,7)
            ma, me = mayor(r1,r2,g)
            comparados.append(r1)
            comparados.append(r2)
            g[me] = g[ma]
        if len(comparados) == 8: break
    
    return g

def crossover(g2):
    comparados = []
    g = deepcopy(g2)
    for i in range(0,7):
        r1 = random.randint(0,7)
        r2 = i
        p = random.randint(1,3)
        while r1 in comparados or r2 == r1:
            r1 = random.randint(0,7)
        if r2 not in comparados:
            comparados.append(r1)
            comparados.append(r2)   
            n1 = g[r2].binario[p:]  
            n2 = g[r1].binario[p:]  
            g[r1].recaldec(g[r1].binario[:p] + n1)
            g[r2].recaldec(g[r2].binario[:p] + n2)
        else:
            while r2 in comparados or r2 == r1:
                r2 = random.randint(0,7)
            comparados.append(r1)
            comparados.append(r2)
            n1 = g[r2].binario[p:]
            n2 = g[r1].binario[p:]
            g[r1].recaldec(g[r1].binario[:p] + n1)
            g[r2].recaldec(g[r2].binario[:p] + n2)
        if len(comparados) == 8: break
    return g

  

def mutacion(g2):
    g = deepcopy(g2)
    for i in range(0,7):
        r1 = random.randint(0,3)
        s = ''
        for j in range(4):
            if j == r1:
                if g[i].binario[r1] == '1':  s += '0'
                else: s += '1'
            else:
                s += g[i].binario[j]
        g[i].recaldec(s)
        s = ''
    
    return g

   
        
def MejorGen(g,m):
    mejor = g[0]
    dif = m - g[0].func()
    for i in g:
        if (m - i.func()) < dif: 
            mejor = i
            dif = m - i.func()
    return mejor
        
    



def Evaluacion(ng):
    contador = 0
    generaciones = []
    mejores = []
    generacion1 = [[random.random()for x in range(8)]for x in range(4)]
    ##PRIMERA GENERACION
    nueva = generarCromosoma(generacion1)
    generaciones.append(nueva)
    contador += 1
    mejores.append(MejorGen(generaciones[contador-1],6))
    
    
    
    while contador < ng:
        ##SELECCION
        generaciones.append(seleccion(generaciones[contador-1]))
        contador += 1
        mejores.append(MejorGen(generaciones[contador-1],6))
        if contador == ng: break
        ##CROSSOVER
        generaciones.append(crossover(generaciones[contador-1]))
        contador += 1
        mejores.append(MejorGen(generaciones[contador-1],6))
        if contador == ng: break
        ##MUTACION
        generaciones.append(mutacion((generaciones[contador-1])))
        contador += 1
        mejores.append(MejorGen(generaciones[contador-1],6))
        if contador == ng: break

    return generaciones, mejores

 

def Imprimir(g,m):
    count = 0
    for i in range(len(g)):
        print("La generacion #" + str(i+1) + " obtuvo los siguiente cromosomas")
        if count == 0:
            print("* Esta generacion se obtuvo de manera aleatoria \n")
        elif count == 1:
            print("* Esta generacion se obtuvo por el metodo de SELECCION \n")
        elif count == 2:
            print("* Esta generacion se obtuvo por el metodo de CROSSOVER \n")
        elif count == 3:
            print("* Esta generacion se obtuvo por el metodo de MUTACION \n")
            count = 0
        for j in range(len(g[i])):
            print("#" + str(j + 1) + "   "+ g[i][j].binario+ "       " + str(g[i][j].decimal))
        print("\nEL MEJOR DE ESTA GENERACION FUE EL CROMOSOMA " + str(m[i].binario)+ "\n")
        count +=1
    


g,m = Evaluacion(10)

Imprimir(g,m)
