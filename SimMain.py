#!/usr/bin/python
import pickle

AS_care=(1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
# No information of AS1755 was found in the dataset, although AS1755 appeared in the paper














    str1 = './pickles/PoP_Topology_AS%d.dat'%asn
    f = open(str1, 'w')
    pickle.dump(PoP_graph, f)
    pickle.dump(PoPsDict, f)
    pickle.dump(ExternalAS_Dict, f)
    f.close()