# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:56:26 2016

@author: fzhen
"""
import re
###############Reading edges from the topology dataset#############
# Input: str, the edge file name
# Output: edgeLoc1, edgeLoc2
#         The location string of the edge
####################################################################
def ReadEdges(str):
    f = open(str)
    if not f:
        exit
        
    edgeLoc = []
    edgeLoc1 = []
    edgeLoc2 = []
    lines = f.readlines()
    f.close()
    
    for line in lines:
        line = re.split(':|->', line)
        edgeLoc1.append(line[1])
        edgeLoc2.append(re.split('\d+', line[3])[0])
    
    # Eleminate the space after each location
    edgeLoc1 = [loc.strip() for loc in edgeLoc1]
    edgeLoc2 = [loc.strip() for loc in edgeLoc2]
    edgeLoc = zip(edgeLoc1, edgeLoc2)
    return edgeLoc
        

    
    
    
    