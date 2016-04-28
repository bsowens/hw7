import math
import heapq
import random

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




def repeated_random(l,k):
    n = len(l)
    best_residue = pow(10,14)*2
    for i in range(0,k):
        for j in range(0,n):
            l[j] = random.choice([1, -1])*l[j]
        residue = abs(sum(l))
        if residue < best_residue:
            best_residue = residue
    return best_residue


def residue(sol,l):
    return abs(sum([a*b for a,b in zip(sol, l)]))

def gradient_descent(l,k):
    n = len(l)
    randListGen = lambda n: [random.choice([-1,1]) for x in range(0,n)]
    solution1 = [random.choice([-1,1]) for x in range(0,n)]
    residue1 = residue(solution1,l)
    for x in range(0,k):
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        solution2 = solution1

        solution2[i] = solution2[i] * -1

        solution2[j] = solution2[j] * random.choice([1,-1])
        residue2 = residue(solution2,l)
        if residue2 < residue1:
            solution1 = solution2
            residue1 = residue(solution1,l)
    return solution1

def temp(i):
    return pow(10,10)*pow(0.8,(i/300))



#Function for weighted random pick from https://www.safaribooksonline.com/library/view/python-cookbook-2nd/0596007973/ch04s22.html

def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item

def simulated_annealing(l,k):
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

def randSets():
    test_list = []
    rand = []
    for i in range(0,50):
        for i in range(0,100):
            rand.append(random.randint(1,pow(10,12)))
        test_list.append(rand)
    return test_list


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

        rrResult.append(repeated_random(rand[i],250))
        #print('rr done at ',i)
        #gdResult.append(gradient_descent(rand[i],250))
        #print('gd done at ',i)
        #saResult.append(simulated_annealing(rand[i],5))
    return rrResult
















