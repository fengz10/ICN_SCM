#!/usr/bin/python
import pickle
from Zipf import ZipfGenerator
from AddTreeTopology import AddTreeToGraph

AS_care=(1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
# No information of AS1755 was found in the dataset, although AS1755
# appeared in the paper

PoP_Topology = {}
for asn in AS_care:
    f = open('./pickles/PoP_Topology_AS%d.dat'%asn)
    PoP_graph = pickle.load(f)
    PoPsDict = pickle.load(f)
    ExternalAS_Dict = pickle.load(f)
    f.close()    

    # Add a binary tree (3-level) to every PoP where it has external links      
    for popID in ExternalAS_Dict:
        if not popID in PoP_graph:
            # Some PoPs are not in the graph structure, since they only
            # appeared in the external links
            #print 'popID = ', popID
            continue
        AddTreeToGraph(PoP_graph, popID, 2, 3)
    
    # Record the PoP topology information into the PoP_Topology dict
    PoP_Topology[asn] = [PoP_graph, PoPsDict, ExternalAS_Dict]
    
    print '####################################'
    print 'asn=', asn
    print 'ExternalAS_Dict.keys()=', ExternalAS_Dict.keys() 
    print 'PoP_graph.keys()=', PoP_graph.keys()









zipfGen = ZipfGenerator(1000, 0.7)
print zipfGen.next()

