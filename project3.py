"""
Math 560
Project 3
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

def initGraph(adjList):
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
        pass
    return adjList


def restoreCycle(vertex, retList):
    retList.append(vertex.rank)
    cur = vertex.prev
    while (cur.rank != retList[0]):
        retList.append(cur.rank)
        '''
        if cur.prev != None and cur.prev.prev == cur:
            retList.clear()
            retList.append(cur.rank)
            retList.append(cur.prev.rank)
            retList.append(cur.rank)
            return
        '''
        cur = cur.prev
        pass

    retList.append(vertex.rank)
    retList.reverse()
"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    adjList = initGraph(adjList)
    adjList[0].dist = 0

    for i in range(0, len(adjList) - 1):
        for vertex in adjList:
            for neigh in vertex.neigh:
                if vertex.dist != math.inf and neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank]:
                    neigh.dist = vertex.dist + adjMat[vertex.rank][neigh.rank]
                    neigh.prev = vertex
                    pass
                pass
            pass
        pass

    # import pdb; pdb.set_trace()
    retList = []
    # detect negative cycle
    for vertex in adjList:
        for neigh in vertex.neigh:
            if vertex.dist != math.inf and neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank]:
                restoreCycle(vertex, retList)
                print(f'retList: {retList}')
                return retList
            pass
        pass
    pass
    return retList
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    # import pdb; pdb.set_trace()
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
