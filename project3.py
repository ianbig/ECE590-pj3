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
    while cur.rank != vertex.rank:
        retList.append(cur.rank)
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

    # import pdb; pdb.set_trace()
    for _ in range(len(adjList)):
        # print(f'=========={i} iterations=============')
        for vertex in adjList:
            for neigh in vertex.neigh:
                if vertex.dist != math.inf and neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank] + tol:
                    neigh.dist = vertex.dist + adjMat[vertex.rank][neigh.rank]
                    neigh.prev = vertex
                    pass
                #print(f' vertex: {vertex} dis: {vertex.dist} prev: {vertex.prev}')
                # print(f' neigh: {neigh} dis: {neigh.dist}, prev: {neigh.prev}')
                pass
            pass
        pass

    # import pdb; pdb.set_trace()
    retList = []
    # detect negative cycle
    for vertex in adjList:
        for neigh in vertex.neigh:
            if vertex.dist != math.inf and neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank] + tol:
                restoreCycle(neigh, retList)
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
