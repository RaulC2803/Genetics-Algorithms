import random
import math
from copy import deepcopy

tabla = [[random.random() for x in range(8)] for x in range(4)]

class Cromosoma:
    binario = ''
    decimal = 0
    resolve = 0

    def __init__(self, binario):
        self.binario =  binario

    def function(self,x):
        self.resolve = abs((x-5)/(2+math.sin(x)))
        self.resolve = round(self.resolve)
        return self.resolve
    

    def fitness(self,other):
        dif1 = abs(6-self.resolve)
        dif2 = abs(6-other.resolve)
        return dif1 <= dif2

    def __eq__(self, other):
        self.binario = other.binario
        self.decimal = other.decimal

    def comp(self, other):
        return self.decimal == other.decimal

    def bintoDecimal(self):
        self.decimal = int(self.binario,2)  

    def setBinario(self, binario):
        self.binario = binario

def showCromosomas(cromosomas):
    for x in cromosomas:
        print((x.binario, x.decimal, x.resolve),end=' ')
    print()


def generarCromosomas(tabla):
    row = len(tabla)
    col = 8
    cromosomas =[]
    for i in range(row):
        binario = [[] for x in range(2)]
        for j in range(col):
            if j < 4:
                if tabla[i][j] < 0.5:
                    binario[0].append(0)
                else:
                    binario[0].append(1)
            else:
                if tabla[i][j] < 0.5:
                    binario[1].append(0)
                else:
                    binario[1].append(1)
        cromosomas += binario[:]

    return cromosomas

def generarDecimales(cromo):
    cromosomas = []
    for i in cromo:
        s = ''
        for j in i:
            s += str(j)
        cromosoma = Cromosoma(s)
        cromosoma.decimal = int(s,2)
        cromosoma.function(cromosoma.decimal)
        cromosomas += [cromosoma]

    return cromosomas

def pairTournament():
    num = [4,5,6,7]
    pair = []
    for x in range(4):
        ran = num.pop(random.randint(0,len(num)-1))
        pair += [(x,ran)]
    return pair

def pairCrossover(cromo):
    cromosomas = deepcopy(cromo)
    pair = [] 
    used = []
    i = 0
    while i < len(cromosomas):
        for j in range(i+1, len(cromosomas)):
            if not cromosomas[i] == cromosomas[j] and i not in used and j not in used:
                used += [i, j]
                pair += [(i,j)]
                break
        i+= 1 

    return pair

def selection(pair,cromo):
    cromosomas = deepcopy(cromo)
    for x,y in pair:
        if cromosomas[x].fitness(cromosomas[y]):
            cromosomas[y] = deepcopy(cromosomas[x])
        else:
            cromosomas[x] = deepcopy(cromosomas[y])
    return cromosomas
        
def crossover(pair,cromo):
    cromosomas = deepcopy(cromo)
    cut_point = [random.randint(1,2) for x in range(4)]
    count = 0
    for x,y in pair:
        bin1 = deepcopy(cromosomas[x].binario[cut_point[count]:] )
        bin2 = deepcopy(cromosomas[y].binario[cut_point[count]:])
        aux1 = deepcopy(cromosomas[x])
        aux2 = deepcopy(cromosomas[y])
        aux1.binario = deepcopy(aux1.binario[:cut_point[count]] + bin2)
        aux2.binario = deepcopy(aux2.binario[:cut_point[count]] + bin1)
        aux1.bintoDecimal()
        aux2.bintoDecimal()
        aux1.resolve = aux1.function(aux1.decimal)
        aux2.resolve = aux2.function(aux2.decimal)
        cromosomas[x] = deepcopy(aux1)
        cromosomas[y] = deepcopy(aux2)
        count+=1

    return cromosomas

def mutation(cromo):
    cromosomas = deepcopy(cromo)
    for i in range(len(cromosomas)):
        r = random.randint(0,len(cromosomas[i].binario)-1)
        aux = deepcopy(cromosomas[i])
        list_bin = list(aux.binario)
        if aux.binario[r] == '1':
            list_bin[r] = '0'
        else:
            list_bin[r] = '1'
        j = ''
        aux.binario = j
        for j in list_bin:
           aux.binario += j 
        aux.bintoDecimal() 
        aux.resolve = aux.function(aux.decimal)
        cromosomas[i] = deepcopy(aux)

    return cromosomas


def goal(cromo):
    cromosomas = deepcopy(cromo)
    isGoal = False
    for x in cromosomas:
        if x.resolve == 6:
           isGoal = True
           break
    return isGoal

if __name__ ==  "__main__":

    count = 0
    cromo = generarCromosomas(tabla)
    cromosomas = generarDecimales(cromo)

    while True:

        showCromosomas(cromosomas)

        if goal(cromosomas):
            print('Numero de generaciones: ' + str(count))
            break
 
        pair = pairTournament()

        cromosomas = selection(pair,cromosomas)    
        
        pair = pairCrossover(cromosomas)
        
        cromosomas = crossover(pair,cromosomas[:])
            
        cromosomas = mutation(cromosomas[:])

        count+=1
 









