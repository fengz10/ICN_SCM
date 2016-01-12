#!/usr/bin/python
import pickle

##########################################################################
# AddTreeToGraph will add a tree to the accessPoint of the graph
# Input: graph        a classic dict structure of graph
#        accessPoint  the id of the node where the tree will be added to
#        degree       the degree of the tree, 2 for binary trees
#        level        the level of the tree
#
# Output: the new graph is in the input graph structure
#         key=-1 in graph record the leaves nodes
#         Note to delete the key after getting the leaves nodes
###########################################################################
#import copy
def AddTreeToGraph(graph, accessPoint, degree, level):
    assert accessPoint in graph, 'node %d is not in the graph'%accessPoint
    assert degree > 0 and level > 0, 'input error'
    assert type(graph) == type({}), 'graph type error'   
    
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
            # The default delay value is 0.5ms
            graph[accessPoint][idNode+1] = 0.5
            graph[idNode+1] = {}
            graph[idNode+1][accessPoint] = 0.5
            aboveLevelNodes = thisLevelNodes
            levelStartID = idNode+2
        else:
            for j in range(len(aboveLevelNodes)):
                for k in range(degree):
                    # This level start from id value of levelStartID
                    # and this node is the k th child of parent node j
                    # The default delay value is 0.5ms
                    graph[aboveLevelNodes[j]][levelStartID + j*degree + k]=0.5
                    graph[levelStartID + j*degree + k] = {}
                    graph[levelStartID + j*degree + k][aboveLevelNodes[j]]=0.5               
                    thisLevelNodes.append(levelStartID + j*degree + k)
            
            # After creating i th level nodes
            levelStartID = levelStartID + len(aboveLevelNodes)*degree
            aboveLevelNodes = thisLevelNodes
            
    # using graph[-1] to record leaves nodes and its PoP index
    if -1 not in graph:        
        graph[-1] = {accessPoint:aboveLevelNodes}
    else:
        graph[-1][accessPoint] = aboveLevelNodes
##############################################################################
        
def GetPoPTopology(asn):
    assert asn in (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018), \
    'AS %d is not in the asnCare list'%asn 
    
    with open('./pickles/PoP_Topology_AS%d.dat'%asn) as f:
        PoP_graph = pickle.load(f)
        PoPsDict = pickle.load(f)
        ExternalAS_Dict = pickle.load(f)

    # Add a binary tree (3-level) to every PoP where it has external links      
    for popID in ExternalAS_Dict:
        if not popID in PoP_graph:
            # Some PoPs are not in the graph structure, since they only
            # appeared in the external links
            #print 'popID = ', popID
            continue
        AddTreeToGraph(PoP_graph, popID, 2, 3)

    # Suppose every AS has at least one PoP have external links, so it has
    # added a tree in that PoP. So it has the -1 key
    assert -1 in PoP_graph
    LeavesDict = PoP_graph[-1]
    # Remember to delete -1 from graph after copying it out
    # Otherwise, -1 may be iterated in the following loops
    del PoP_graph[-1]
    
#    # Testing
#    if asn == 1221:
#        AddTreeToGraph(PoP_graph, 20, 2, 3)
#        AddTreeToGraph(PoP_graph, 21, 2, 3)
#        print 'PoP_graph[1221]=', PoP_graph
#        print 'PoP_graph[-1]=', PoP_graph[-1]
    
    # Record the PoP topology information into the PoP_Topology dict
    # Using set to judge if the element of one list is all in another list
    assert set(LeavesDict.keys()) <= set(ExternalAS_Dict.keys())
    
    return PoP_graph, PoPsDict, ExternalAS_Dict, LeavesDict  
    
########################################################################
#print GetPoPTopology(1221)

        
    
    
    
    
    
    
    
    
        
