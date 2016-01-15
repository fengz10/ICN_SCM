#!/usr/bin/python

import pickle
##########################################################################
# Script to output the PoP information,
# Input No
# Outpu: the number of core routers, links, PoPs, and neighbouring ASes
##########################################################################
for asn in (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018): 
    
    with open('./pickles/PoP_Topology_AS%d.dat'%asn) as f:
        PoP_graph = pickle.load(f)
        PoPsDict = pickle.load(f)
        ExternalAS_Dict = pickle.load(f)
    print '################%d#######################'%asn
    print 'All routers number =', len(PoP_graph.keys())
    # links number
    
    if asn == 3967:
        print 'PoP_graph=', PoP_graph
        print 'PoPsDict=', PoPsDict
        print 'ExternalAS_Dict=', ExternalAS_Dict
    
    for i1 in PoP_graph:
        for i2 in PoP_graph[i1]:
            if not i1 in PoP_graph[i2]:
                print 'not asymmetry'
                break
    
    link = 0
    for i1 in PoP_graph:
        link += len(PoP_graph[i1])
    
    assert link%2 == 0
    print 'Link number = ', link/2
        
    
    temp = sum([len(i) for i in PoP_graph.values()])
    assert temp%2 == 0
    print 'Link number2 = ', temp/2
    
    print 'PoP number =', len(ExternalAS_Dict.keys())
    s = set([])
    for pop in ExternalAS_Dict.values():
        for id in pop:
            s.add(id)
            
    print 'Neighbor ASes number =', len(s)
    print 'Neighbor ASes: ', s
    
