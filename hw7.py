import math
import heapq
import random
import numpy

# INPUT
test_list = [10, 8, 7, 6, 5]

# partition takes a list of integers and performs KK number partitioning algorithm

def karmarkar_karp(l):
    n = len(l)
    K = sum(l)

    # init heap, but since heappop only pops the min value, we will multiply each input value by -1
    heap = []
    for item in l:
        heapq.heappush(heap, item * -1)
    heapq.heapify(heap)

    while len(heap) > 1:
        i = heapq.heappop(heap)
        j = heapq.heappop(heap)
        heapq.heappush(heap, abs(i - j) * -1)
    # the result should be the residue. Switch negative sign back.
    return heapq.heappop(heap) * -1

def randSet():
    test_list = []
    rand = []
    for i in range(0,100):
        rand.append(random.randint(1,pow(10,12)))
    return rand

def generatePosOrNeg():
    val = random.randint(1, 2)
    if (val == 1):
        return 1
    else:
        return -1

def repeated_random(k):
    best_res_set = []
    for on_list in range(0,50):
        l = randSet()
        best_so_far = 999999999999999
        for j in range(0,k):
            
            for i in range(0,100):
                l[i] = generatePosOrNeg()*l[i]
            residue = abs(sum(l))
            if residue < best_so_far:
                best_so_far = residue
        best_res_set.append(best_so_far)
        print(best_res_set)
    return best_res_set


def residue(sol,l):
    return abs(sum([a*b for a,b in zip(sol, l)]))

def gradient_descent1(k):
    best_res_set = []
    for on_list in range(0,50):
        l = randSet()
        best_so_far = 999999999999999
        for j in range(0,k):
            
            for i in range(0,100):
                x = random.randint(0,99)
                y = random.randint(0,99)
                l[x] = l[x] * -1
                l[y] = l[y] * random.choice([1,-1])
            residue = abs(sum(l))
            #print(residue)
            if residue < best_so_far:
                #print(residue, '<', best_so_far)
                best_so_far = residue
                
        best_res_set.append(best_so_far)
    return best_res_set


def temp(i):
    return pow(10,10)*pow(0.8,(i/300.0))




def simulated_annealing(k):

    best_res_set = []
    for on_list in range(0,50):
        l = randSet()
        best_so_far = 999999999999999
        for j in range(0,k):
            residue1 = abs(sum(l))
            x = random.randint(0,99)
            y = random.randint(0,99)
            l[x] = l[x] * -1
            l[y] = l[y] * random.choice([1,-1])
            residue2 = abs(sum(l))
            p = numpy.exp(-( residue1 - residue2  ) / temp(j)   )
            randFloat = random.uniform(0,1)
            if residue2 < best_so_far or (randFloat < p and residue2 > best_so_far):
                best_so_far = residue2
            
            
                
        best_res_set.append(best_so_far)
    return best_res_set




    
    '''
    n = len(l)
    randListGen = lambda n: [random.choice([-1,1]) for x in range(0,n)]
    solution1 = randListGen(n)
    residue1 = residue(solution1,l)
    for x in range(0,25000):
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        solution2 = solution1
        solution2[i] = solution2[i] * -1
        solution2[j] = solution2[j] * random.choice([1,-1])
        residue2 = residue(solution2,l)

        #Probability of choosing a wrong move:
        print(residue(solution2,l) - residue(solution1,l))
        p = math.exp(-( residue(solution2,l) - residue(solution1,l)  ) / temp(x)   )
        print(p)



        if residue2 < residue1:
            solution1 = solution2
            residue1 = residue(solution1,l)
    return solution1

'''
def testKK():
    rand = randSets()
    test = []
    for i in range(0,len(rand)):
        test.append(karmarkar_karp(rand[i]))
        return test

def testCases():
    rand = randSets()
    rrResult = []
    gdResult = []
    saResult = []
    for i in range(0,len(rand)):

        rrResult.append(repeated_random(rand[i],5))
        #print('rr done at ',i)
        #gdResult.append(gradient_descent(rand[i],250))
        #print('gd done at ',i)
        #saResult.append(simulated_annealing(rand[i],5))
















