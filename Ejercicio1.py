import random
from copy import deepcopy

class Chromosome:
    decimal = []
    binary = []
    fit = 28
    prob = 0

    def __init__(self, decimal, binary):
        self.decimal = decimal
        self.binary = binary
        self.fitness()

    def getDecimal(self):
        return self.decimal

    def getBinary(self):
        return self.binary

    def setDecimal(self,decimal):
        self.decimal = decimal

    def setBinary(self, binary):
        self.binary = binary

    def getFit(self):
        return self.fit

    def getProbability(self):
        return self.prob

    def setProbability(self, prob):
        self.prob = prob

    def binary2Decimal(self):
        for i in range(len(self.binary)):
            self.decimal[i] = int(self.binary[i],2) 
        self.fitness()

    def fitness(self):
        number = 56
        for i in range(len(self.decimal)):
            for j in range(len(self.decimal)):
                if self.decimal[i] == self.decimal[j] and j != i:
                    number-=1
                if abs(i-j) == abs(self.decimal[i]-self.decimal[j]) and j != i:
                    number-= 1
        self.fit = round(number/2)


def showChromosomes(chromosomes):
    for i in chromosomes:
        print(i.getDecimal(), i.getBinary(), i.getFit(), i.getProbability(), end= ' ')
        print()

def Binary(n): 
    binary = "" 
    i = 0
    d = 0
    while n > 0 and i<=2: 
        s1 = str(int(n%2)) 
        binary = binary + s1 
        n /= 2
        i = i+1
        d = binary[::-1] 
    if d == 0:
        return '000'
    return d

def createChromosomes():
    n = 8
    chromosomes = []
    for i in range(4):
        decimal = []
        binary = []
        for j in range(n):
            r = random.randint(0,n-1) 
            decimal += [r]
            binary += [Binary(r)]
        chromosomes += [Chromosome(decimal,binary)]

    return chromosomes


def crossOver(chromo):
    chromosomes = deepcopy(chromo)
    cut_point = [random.randint(1,4) for x in range(2)]
    pair = [(0,1),(2,3)]
    count = 0
    for x,y in pair:
        cut = cut_point[count] 
        #Get the binary of each chromosome
        binary1 = chromosomes[x].getBinary()
        binary2 = chromosomes[y].getBinary()

        #swap the second part after the cut of each binary 
        aux = binary1[cut:] 
        binary1 = binary1[:cut] + binary2[cut:]
        binary2 = binary2[:cut] + aux
        chromosomes[x].setBinary(binary1)
        chromosomes[y].setBinary(binary2)
        chromosomes[x].binary2Decimal()
        chromosomes[y].binary2Decimal()

        count += 1

    return chromosomes

def mutation(chromo):
    chromosomes = deepcopy(chromo)

    for i in chromosomes:
        r_queen = random.randint(0,7)
        r_binary = random.randint(0,2)

        binary = i.getBinary()

        if binary[r_queen][r_binary] == '1':
            binary[r_queen] = binary[r_queen][:r_binary] + '0' + binary[r_queen][r_binary+1:]
        else:
            binary[r_queen] = binary[r_queen][:r_binary] + '1' + binary[r_queen][r_binary+1:]
        
        i.setBinary(binary)
        i.binary2Decimal()

    return chromosomes

def sort_probability(e):
    return e.getProbability()


def selection(chromo):
    chromosomes = deepcopy(chromo)
    total_prop = 0
    for i in chromosomes:
        total_prop += i.getFit()
        
    for i in range(len(chromosomes)):
        chromosomes[i].setProbability(round(chromosomes[i].getFit()/total_prop*100))
    
    chromosomes.sort(reverse=True, key=sort_probability)

    chromosomes.pop(len(chromosomes)-1)
    aux = deepcopy(chromosomes[0])
    chromosomes[0] = deepcopy(chromosomes[1])
    chromosomes[1]= deepcopy(aux)
    aux = deepcopy(chromosomes[2]) 
    chromosomes[2]  = deepcopy(chromosomes[0])
    chromosomes.append(aux)

    return chromosomes

def isGoal(chromo):
    chromosomes = deepcopy(chromo)
    goal = False
    for i in chromosomes:
        if i.getFit() == 28:
           goal = True 
           break

    return goal


if __name__ == "__main__":
    chromosomes = createChromosomes()
    count = 0 

    while count <= 100000:        
        if isGoal(chromosomes):
            break

        chromosomes = selection(chromosomes)
        chromosomes = crossOver(chromosomes)
        chromosomes = mutation(chromosomes)     
        showChromosomes(chromosomes)
        print()
        count += 1

    print("Total de generaciones: ", str(count-1))



        



