#!/usr/bin/python
##########################################################################
# AddTreeToGraph will add a tree to the accessPoint of the graph
# Input: graph        a classic dict structure of graph
#        accessPoint  the id of the node where the tree will be added to
#        degree       the degree of the tree, 2 for binary trees
#        level        the level of the tree
#
# Output: the new graph is in the input graph structure
###########################################################################
#import copy
def AddTreeToGraph(graph, accessPoint, degree, level):
    assert accessPoint in graph
    assert degree > 0 and level > 0
    assert type(graph) == type({})   
    
    # After experiment, simply call the copy function of build-in, will not 
    # copy the inner list structure of the graph dict, it wil still change out
    # of this funciton
    # graphNew = copy.deepcopy(graph)
    # Comment the above line to improve efficiency
    
    idNode = max(graph.keys())
    # New nodes id start from idNode + 1
    aboveLevelNodes = []
    for i in range(level):
        thisLevelNodes = []
        if i == 0:
            thisLevelNodes.append(idNode+1)
            graph[accessPoint][idNode+1] = 1
            graph[idNode+1] = {}
            graph[idNode+1][accessPoint] = 1
            aboveLevelNodes = thisLevelNodes
            levelStartID = idNode+2
        else:
            for j in range(len(aboveLevelNodes)):
                for k in range(degree):
                    # This level start from id value of levelStartID
                    # and this node is the k th child of parent node j
                    graph[aboveLevelNodes[j]][levelStartID + j*degree + k] = 1
                    graph[levelStartID + j*degree + k] = {}
                    graph[levelStartID + j*degree + k][aboveLevelNodes[j]] = 1               
                    thisLevelNodes.append(levelStartID + j*degree + k)
            
            # After creating i th level nodes
            levelStartID = levelStartID + len(aboveLevelNodes)*degree
            aboveLevelNodes = thisLevelNodes
            
##############################################################################    

        
    
    
    
    
    
    
    
    
        
