#!/usr/bin/python
import os
from ReadEdges import ReadEdges
from ShortestPath import dijkstra
import pickle

as_edege = os.listdir('./Rocketfuel/maps-n-paths/')
AS_topology = {}
asnCare=(1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
# No information of AS1755 was found in the dataset, although AS1755 
# appeared in the paper

for edge in as_edege:
    if edge.find(':') == -1:
        continue
    [asn1, asn2] = map(int, edge.split(':'))
    if asn1 != asn2:
        if asn1 in AS_topology:
            AS_topology[asn1][asn2] = 1            
        else:            
            AS_topology[asn1] = {}
            AS_topology[asn1][asn2] = 1

print len(AS_topology)

# Testing whether the PoP-level topology data is symmetry
# for i in AS_topology:
#     for asn in AS_topology[i]:
#         if not i in AS_topology[asn]:
#             print 'not symmetry'
# print 'symmetry'
# Only AS 4600 and AS 3582 have no internal topology data


for asn in asnCare:
    # Read internal PoP link of the AS      
    edgesInternal=ReadEdges('./Rocketfuel/maps-n-paths/%d:%d/edges.lat'\
    %(asn,asn))
    
    # PoPNames record the location name of the PoP
    PoPNames = []
    for edge in edgesInternal:
        PoPNames += [edge[0], edge[1]]

    
    # Create a dict to map index to PoP Location name, and name to index
    # It can lookup name and index at the same time
    i = 0
    PoPsDict = {}    
    for name in set(PoPNames):
        PoPsDict[name] = i
        PoPsDict[i] = name
        i += 1
    del i


    # Record external link of the AS
    edgesExternal = {}
    for asnTem in AS_topology[asn]:
        str = './Rocketfuel/maps-n-paths/%d:%d/edges.lat'%(asn,asnTem)
        edgesExternal[asnTem] = ReadEdges(str)
       
                
    #        if not edge[0] in PoPsN2I:
    #            print str
    #            print 'edge %s is not in the dict'%edge[0]
    #        if not edge[1] in PoPsN2I:
    #            print str
    #            print 'edge %s is not in the dict'%edge[1]
    #    print 'All edges are in the dict'
    
    

    
    # Mapping PoP names to indexes    
    edgesInternal = [(PoPsDict[n1], PoPsDict[n2], delay) for (n1, n2, delay)\
    in edgesInternal]
    # Mapping PoP name to indexes fo external links
    for asnTem in edgesExternal:
        # Most external links connect the routers in the same PoP location, 
        # and we exclude those not in the same PoP location
        edgesExternal[asnTem] = [(PoPsDict[n1], PoPsDict[n2], delay)\
        for (n1, n2, delay) in edgesExternal[asnTem] if n1 == n2 and \
        n1 in PoPsDict]
        print 'edgesExternal[%d]='%asnTem, edgesExternal[asnTem]
        
    # Record the internal topology into the standard graph structure
    PoP_graph = {}
    for edge in edgesInternal:
        if edge[0] not in PoP_graph:
            PoP_graph[edge[0]] = {}
        if edge[1] not in PoP_graph:
            PoP_graph[edge[1]] = {}
        
        PoP_graph[edge[0]][edge[1]] = edge[2]
        PoP_graph[edge[1]][edge[0]] = edge[2]
        
    #################################################
    if asn == 1221:
        print 'testing###################################'
        print PoP_graph
        
    # Record the external topology
    # The PoP index as the key, and the neighboring ASN list as its value
    ExternalAS_Dict = {}
    for asnTem in edgesExternal:
        for (i, j, delay) in edgesExternal[asnTem]:
            if not i in ExternalAS_Dict:
                ExternalAS_Dict[i] = []    
            ExternalAS_Dict[i].append(asnTem)         
#        ExternalAS_Dict[asnTem] = [i for (i, j) in edgesExternal[asnTem]]
        
    print 'PoP_graph[%d]='%asn, PoP_graph
    # Testing whether the PoP graph is a connected graph by dijkstra
    # Evidence shows that all the nodes are reachable
    dist, pred = dijkstra(PoP_graph, PoP_graph.keys()[0])
    print 'dist=', dist
    print 'values=', dist.values()
    print 'max dist=', max(dist.values())
    assert max(dist.values()) < 1000
    print 'ExternalAS_Dict=', ExternalAS_Dict
    print '#######################End of AS%d######################'%asn
    
    # Record the results into pickle files    
    str1 = './pickles/PoP_Topology_AS%d.dat'%asn
    f = open(str1, 'w')
    pickle.dump(PoP_graph, f)
    pickle.dump(PoPsDict, f)
    pickle.dump(ExternalAS_Dict, f)
    f.close()
    
    
    

        
        
        
