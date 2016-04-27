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

def min_finder(l):
    min_val = min(l)
    min_idx = l.index(min_val)
    return min_idx

def repeated_random(l,k):
    n = len(l)
    solutions = []
    residues = []
    randBinList = lambda n: [random.choice([-1,1]) for b in range(0,n)]
    for i in range(0,k):
        solution = randBinList(n)
        solutions += [solution]
        residue = abs(sum([a*b for a,b in zip(solution, l)]))
        residues += [residue]
    min_res = min_finder(residues)   
    return solutions[min_res]
    
    


def gradient_descent(k):
    pass



def simulated_annealing(k):
    pass







    
    











