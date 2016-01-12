#!/usr/bin/python
#coding:utf-8

import random
from Zipf import ZipfGenerator
from AddTreeTopology import GetPoPTopology
from ShortestPath import dijkstra
import numpy as np
import sys

##############################################################################
# Return the index of the maximal value of the double Dict structure
# E.g., doubleDict = {1:{2:5, 3:6}, 2:{1:3, 2:7}} will return (2,2)
# Input doubleDict
# Output (i,j) the key values of the maximal value of the doubleDict
#############################################################################
def GetIndexOfMax(doubleDict):
    if not doubleDict:
        return (-1, -1)
    i = j = -1
    currentMax = -1      # initial value
    for index in doubleDict:
        if not doubleDict[index]:
            continue
        
        jTemp = max(doubleDict[index], key = doubleDict[index].get)
        vMax = doubleDict[index][jTemp]
        
        if (vMax > currentMax):
            i = index
            j = jTemp
            currentMax = vMax
        
#        vMax = max(doubleDict[index].keys())
#        if (vMax > currentMax):
#            j = k for (k,v) in doubleDict[index].items() if v == vMax
#            i = index
#            currentMax = vMax
    return i, j
# Testing        
#dictTemp = {1:{2:3, 4:8}, 2:{2:2, 3:9}, 3:{1:2, 7:11}}
#print 'GetIndexOfMax(dictTemp)=', GetIndexOfMax(dictTemp)

##############################################################################
# The main simulation procedure
# Generate different distributions, and return the results of different 
# parameters
#
# Input: 
#        asn, the as number
#        cacheRatio, the percentage of replication from 0.0 to 1.0
#        delayLimit, the maximal delay
#        alph, zipf paremeter
#        algo == 0, our algorithm
#        algo == 1, baseline
#        The difference between the two algorithms mainly relies on the 
#        content-based routing strategy, algo 0 suppose all contents nearby
#        can be discovered by routing, on the other hand, algo 1 suppose
#        only contents in the way to the origin server can be found.
#
# Output: totalcost
###########################################################################
def main(asn = 1221, cacheRatio=0.1, delayLimit = 40, alpha = 0.7, algo = 0):
    
    assert asn in (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
    assert 0 <= cacheRatio <= 1
    assert 0 <= delayLimit <= 1000
    assert 0.1 <= alpha <= 2
    assert algo == 0 or algo == 1        
    
    PoP_graph, PoPsDict, ExternalAS_Dict, LeavesDict = GetPoPTopology(asn)

    # Generate content related parameters
    ID_MAX = 1000          # Content ID scope
    #alpha = 0.7             # Zipf parameter alpha
    
    # Generate content size
    sizeOfID = []
    for i in range(ID_MAX):        
        # Make sure the expected value is 2.2MB, so it times 0.55.
        # Since its original mean value equals to around 3.98
        # alpha = 1.3 according to reference
        sizeOfID.append(0.55*random.paretovariate(1.3))
              
    
    # Bandwidth capacity of every node
    BW_limit = 1.25e3      # 10Gbps as capacity, unit MB
    
    # Generate requests
    # Only leaf nodes send requests, and the number of their requests is
    # proportional to the size of the PoP
    # Key of LeavesDict is the id of the PoP, and the value is its leaves list
    # Key of ExternalAS_Dict is the id of the PoP, and the value is its 
    # external AS list, we can use the AS number as its population
    
    # Request related parameters
    RequestNum = int(1e4)   # Number of all requests

    # Record the request list of leaf nodes
    requestDict = {}    
    
    pop_Population = {}
    for pID in ExternalAS_Dict:
        pop_Population[pID] = len(ExternalAS_Dict[pID])
    
    requestDict = {}
    for pID in LeavesDict:
        # The totoal request number from this PoP (i.e., pID)
        #print 'pop_Population.values()=', pop_Population.values()
        popTem = RequestNum * pop_Population[pID]/sum(pop_Population.values())
        # The request number from every leaf node in this PoP
        vRequestNum = int(popTem/len(LeavesDict[pID]))
        
        # Generate requestLists for every leaf node
        for vID in LeavesDict[pID]:
            requestDict[vID] = [0] * ID_MAX
            zipfGen = ZipfGenerator(ID_MAX-1, alpha)
            for i in range(vRequestNum):    
                requestDict[vID][zipfGen.next()] += 1            
    #print 'requestDict=', requestDict
            
    # Record those contents already replicated in nodes
    cachedInNodes = {}
    # PoP nodes can cache content
    # Every node has the same storage, which equals to 5% of the total size
    cacheSize = ID_MAX * cacheRatio
    #print 'ExternalAS_Dict=', ExternalAS_Dict
    for id in ExternalAS_Dict:
        # Adding some most popular contents into the cached contents
        # We have not taken content size into consideration
        
        # Cache fraction of popular contents
        cachedInNodes[id] = set(range(int(cacheSize/10))) #1/5 are most popular        
        cachedInNodes[id] |= set(random.sample(range(int(cacheSize/10), \
        ID_MAX), int(cacheSize-cacheSize/10)))
 
    #print 'cachedInNodes=', cachedInNodes
        
        # Totoally random cache strategy
#        cachedInNodes[id] = set(random.sample(range(int(cacheSize)),\
#        int(cacheSize)))

        
    # Calculate those nodes within the delay limit
    # Generate the available node id list for every leaf node
    availNodesDict = {}
    for pID in LeavesDict:
        for vID in LeavesDict[pID]:            
            #least delay from vID to all the nodes in PoP_graph
            dist, pred = dijkstra(PoP_graph, vID)            
            
            # The only difference between algo 0 and algo 1 relies on the
            # availNodesDict. For algo 0, all nodes within the limit of delay
            # are available. Otherwise, only nodes on the path to the origin
            # contents are availabe for algo 1
            if algo == 0:
                availNodesDict[vID] = set([x for x in dist if dist[x] 
                <= delayLimit])
            elif algo == 1:
                # Generate a origin node randomly
                allNodes = PoP_graph.keys()                
                originNode = allNodes[int(len(allNodes)/2)]
                if originNode == vID:  # in case originNode is the start node
                    originNode = allNodes[int(len(allNodes)/2)-1]
                
                path = set([originNode, vID])
                while (pred[originNode] != vID):
                    temp = pred[originNode]
                    path.add(temp)
                    originNode = temp
                #print 'path=', path
                
                availNodesDict[vID] = set([x for x in path if dist[x] 
                <= delayLimit])              
                
            else:
                sys.stderr.write('Algo number error\n')
    #print 'availNodesDict=', availNodesDict
    
    # Exclude the requests that can be satisfied by cache
    for vID in availNodesDict:
        for id in availNodesDict[vID]:
            if (id in cachedInNodes):
                for cID in cachedInNodes[id]:
                    # cID is the content, which is cached in vID's available list
                    # Since cID can be obtained from cache, reset the requestDict
                    requestDict[vID][cID] = 0
            
    # Initialize the available bandwidth of every node  
    availBW = {}
    for id in PoP_graph:
        availBW[id] = BW_limit
    
    # Greedily store contents
    # Sort the content according to their bandwidth consumption
    bwConsumeDict = {}   # Record the bandwidth consumption of every leaf node
    for vID in requestDict:
        bwConsumeDict[vID] = np.array(requestDict[vID]) * np.array(sizeOfID)
    
    #print 'bwConsumeDict=', bwConsumeDict
    # bwConsumeDictVC will record the non-zero bandwidth consumption of leaves
    bwConsumeDictVC = {}
    for vID in bwConsumeDict:
        bwConsumeDictVC[vID] = {}
        for cID in range(len(bwConsumeDict[vID])):
            if bwConsumeDict[vID][cID] != 0:
                bwConsumeDictVC[vID][cID] = bwConsumeDict[vID][cID]
    #print 'bwConsumeDictVC=', bwConsumeDictVC
    # xInventroyDict records the content list of each node
    # xBandwidthDict records the bandwidth consumption of each node
    xInventroyDict = {} 
    xBandwidthDict = {}
    

    # The storage and bandwidth cost of all the nodes
    costOfStorageDict = {}
    costOfBWDict = {}
    for id in PoP_graph:
        # E.g., about $0.05/GB, since content size unit MB
        costOfStorageDict[id] = 0.01e-3 + 0.09e-3 * random.random()  
        #E.g., about $0.1/GB
        costOfBWDict[id] = costOfStorageDict[id]*2
    
    
    while(True):    
        vID, cID = GetIndexOfMax(bwConsumeDictVC)
        found = 0
        if vID == -1:
            break
        # Greedily storing requests from leaf node vID
        # Sort the cost of bandwidth of different nodes
        costBWAvail = {k:v for k,v in costOfBWDict.items()\
        if k in availNodesDict[vID]}        
        
        # Sort the cost of bandwidth, and record the node list
        nodeList = sorted(costBWAvail, key = costBWAvail.get)
        for node in nodeList:
            if availBW[node] < 1e-6:    # No available bandwidth
                continue
            # The unit of bwConsumeDictVC is in MB, and the unit of BW 
            # has also been changed to MB
            if (availBW[node] - bwConsumeDictVC[vID][cID] > 0):
                # Modify the available bandwidth
                bwTemp = bwConsumeDictVC[vID][cID]
                availBW[node] -= bwTemp               
                # Record the inventory results
                # Fixed bug here: 'if not node' was wrongly 'if not vID'
                if not node in xInventroyDict:                    
                    xInventroyDict[node] = set([cID])
                    xBandwidthDict[node] = bwTemp
                else:
                    xInventroyDict[node].add(cID)
                    xBandwidthDict[node] += bwTemp
                
                # bwConsumeDictVC only keeps unsatisfied requests
                del bwConsumeDictVC[vID][cID]
                # The process of vID and cID is finished
                found = 1                
                break
            else:                
                # If the size of the content is too large, it neends fragment
                bwTemp = availBW[node]
                bwConsumeDictVC[vID][cID] -= bwTemp
                
                if not node in xInventroyDict:                    
                    xInventroyDict[node] = set([cID])
                    xBandwidthDict[node] = bwTemp
                else:
                    xInventroyDict[node].add(cID)
                    xBandwidthDict[node] += bwTemp

        if found == 0:
            sys.stderr.write('Bandwidth is not enough\n')
            break
    # Calculate cost according to inventory strategies
    # xInventroyDict and xBandwidthDict values 
    totalCost = 0
    # node of xInventroyDict and xBandwidthDict are the same
    assert xInventroyDict.keys() == xBandwidthDict.keys()
    for node in xInventroyDict:
        for cID in xInventroyDict[node]:
            # All the contens stored in node
            totalCost += costOfStorageDict[node] * sizeOfID[cID]
        # Bandwidth cost
        totalCost += costOfBWDict[node] 
    
    return totalCost
##########################################################################
    
    






