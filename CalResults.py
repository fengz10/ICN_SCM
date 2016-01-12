#!/usr/bin/python
import sys
import numpy as np
from SimMain import main


##########################################################################
# Calculate the cost vs. cache ratio for every AS
#main(asn = 1221, cacheRatio=0.1, delayLimit = 3, alpha = 0.7, algo = 0)
def CalCostOfRatio(asn):
    AvgList0 = []   
    AvgList1 = []    
    for ratio in np.arange(0, 1.01, 0.05):
        totalCost0 = []
        totalCost1 = []
        for i in range(5):
            totalCost0.append(main(asn, ratio, 3, 0.7, 0))
            totalCost1.append(main(asn, ratio, 3, 0.7, 1))
        
        avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
        AvgList0.append(avgTemp0)
        AvgList1.append(avgTemp1)
        print 'Average totalCost0=', avgTemp0
        print 'Average totalCost1=', avgTemp1
    
    print 'cost%dAlgo0='%asn, AvgList0
    print 'cost%dAlgo1='%asn, AvgList1


##########################################################################
# Calculate the cost vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
def CalCostOfZipf(asn):
    AvgList0 = []   
    AvgList1 = []    
    for alpha in np.arange(0.6, 1.41, 0.05):
        totalCost0 = []
        totalCost1 = []
        for i in range(5):
            totalCost0.append(main(asn, 0.2, 3, alpha, 0))
            totalCost1.append(main(asn, 0.2, 3, alpha, 1))
        
        avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
        AvgList0.append(avgTemp0)
        AvgList1.append(avgTemp1)
        print 'Average totalCost0=', avgTemp0
        print 'Average totalCost1=', avgTemp1
    
    print 'cost%dAlgo0='%asn, AvgList0
    print 'cost%dAlgo1='%asn, AvgList1
########################################################################
    
##########################################################################
# Calculate the cost vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
def CalCostOfDelaySingle(asn):
    AvgList0 = []   
    AvgList1 = []
        
    for delay in np.arange(0.5, 20, 0.5):
        totalCost0 = []
        totalCost1 = []
        for i in range(10):
    #        totalCost0.append(main(asn, 0.2, delay, 0.7, 0))
            totalCost1.append(main(asn, 0.2, delay, 0.7, 1))
        
    #    avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
    #    AvgList0.append(avgTemp0)
        AvgList1.append(avgTemp1)
    #    print 'Average totalCost0=', avgTemp0
        print 'Average totalCost1=', avgTemp1
    
    #print 'cost%dAlgo0='%asn, AvgList0
    print 'cost%dAlgo1='%asn, AvgList1
########################################################################
    
    
##########################################################################
# Calculate the cost vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
def CalCostOfDelay(asn):
    AvgList0 = []   
    AvgList1 = []
    
    for delay in np.arange(0.5, 20, 0.5):
        totalCost0 = []
        totalCost1 = []
        for i in range(10):
            totalCost0.append(main(asn, 0.2, delay, 0.7, 0))
            totalCost1.append(main(asn, 0.2, delay, 0.7, 1))
        
        avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
        AvgList0.append(avgTemp0)
        AvgList1.append(avgTemp1)
        print 'Average totalCost0=', avgTemp0
        print 'Average totalCost1=', avgTemp1
    
    print 'cost%dAlgo0='%asn, AvgList0
    print 'cost%dAlgo1='%asn, AvgList1

##########################################################################

##########################################################################
# Calculate the cost for every AS
# The other papameters are main(asn, 0.2, 3, 0.7, 0))
#########################################################################
def CalCostOfAllASes():
    asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
    avg0 = []
    avg1 = []
    
    for asn in asnCare:
        totalCost0 = []
        totalCost1 = []
          
        for i in range(5):
            # Compare the cost of two algo uder certain circumstance
            # asn = 7018, ratio = 0.2, delay=3ms, alpha=0.7,
            totalCost0.append(main(asn, 0.2, 3, 0.7, 0))
            totalCost1.append(main(asn, 0.2, 3, 0.7, 1))    
            
        avg0.append(sum(totalCost0)/(len(totalCost0) + 0.0))
        avg1.append(sum(totalCost1)/(len(totalCost1) + 0.0))
    
    print 'avg0=', avg0
    print 'avg1=', avg1
######################################################################
    
asn = int(sys.argv[1])
op = int(sys.argv[2])

if op == 0:
    CalCostOfRatio(asn)
elif op == 1:
    CalCostOfZipf(asn)
elif op == 2:
    CalCostOfDelaySingle(asn)
elif op == 3:
    CalCostOfDelay(asn)
elif op == 4:
    CalCostOfAllASes()
else:
    sys.stderr.write('option value error!\n')
    
    