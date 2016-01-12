#!/usr/bin/python
import re

###############Reading edges from the topology dataset#############
# Input: str, the edge file name
# Output: edgeLoc1, edgeLoc2, delay
#         The location string of the edge
####################################################################
def ReadEdges(str):    
    
    edgeLoc1 = []
    edgeLoc2 = []
    delay = []
    
    # With statement will close file if exceptions occur
    with open(str) as f:     
        lines = f.readlines()    
    
    for line in lines:
        # Using regular expression to split PoP location names
        line = re.split(':|->', line)
        # Eleminate the space after each location
        edgeLoc1.append(line[1].strip())
        edgeLoc2.append(re.split('\d+', line[3])[0].strip())
        # delay in milliseconds
        delayTemp = float(re.split(' ', line[3])[-1])
        # There is a false data in 3356:3356, and the dalay is 100000ms 
        if delayTemp < 0 or delayTemp > 100:
#            f = open('error.txt', 'a')
#            f.writelines([str] + line)
#            f.close()            
            # Let delay be the average value, and be 10 if no old values
            delayTemp = sum(delay)/(len(delay) + 0.0) if delay else 10            
        
        delay.append(delayTemp)    

    return zip(edgeLoc1, edgeLoc2, delay)
        

    
    
    
    