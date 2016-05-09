#!/usr/bin/python
import sys
import numpy as np
from SimMain import main


##########################################################################
# Calculate the cost and link usage vs. cache ratio for every AS
#main(asn = 1221, cacheRatio=0.1, delayLimit = 3, alpha = 0.7, algo = 0)
def CalResultOfRatio(asn):
    AvgCostList0 = []   
    AvgCostList1 = []

    AvgLinkUsageList0 = []   
    AvgLinkUsageList1 = []
    
    for ratio in np.arange(0, 1.01, 0.05):
        totalCost0 = []
        totalCost1 = []

        totalLinkUsage0 = []
        totalLinkUsage1 = []
        
        for i in range(10):
            costTemp0, usageTemp0 = main(asn, ratio, 3, 0.7, 0)
            costTemp1, usageTemp1 = main(asn, ratio, 3, 0.7, 1)

            totalCost0.append(costTemp0)
            totalCost1.append(costTemp1)

            totalLinkUsage0.append(usageTemp0)
            totalLinkUsage1.append(usageTemp1)
        
        avgCostTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgCostTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)

        avgUsageTemp0 = sum(totalLinkUsage0)/(len(totalLinkUsage0) + 0.0)
        avgUsageTemp1 = sum(totalLinkUsage1)/(len(totalLinkUsage1) + 0.0)
        
        AvgCostList0.append(avgCostTemp0)
        AvgCostList1.append(avgCostTemp1)
        
        AvgLinkUsageList0.append(avgUsageTemp0)   
        AvgLinkUsageList1.append(avgUsageTemp1)
        
        
        print 'Average totalCost0=', avgCostTemp0
        print 'Average totalCost1=', avgCostTemp0
        
        print 'Average totalUsage0=', avgUsageTemp0
        print 'Average totalUsage1=', avgUsageTemp1
    
    print 'cost%dAlgo0='%asn, AvgCostList0
    print 'cost%dAlgo1='%asn, AvgCostList1

    print 'linkUsage%dAlgo0='%asn, AvgLinkUsageList0
    print 'linkUsage%dAlgo1='%asn, AvgLinkUsageList1
    
##########################################################################
# Replaced by the previous function
# Calculate the cost vs. cache ratio for every AS
#main(asn = 1221, cacheRatio=0.1, delayLimit = 3, alpha = 0.7, algo = 0)
#def CalCostOfRatio(asn):
#    AvgList0 = []   
#    AvgList1 = []    
#    for ratio in np.arange(0, 1.01, 0.05):
#        totalCost0 = []
#        totalCost1 = []
#        for i in range(10):
#            # main()[0] means only returning the cost,
#            # [1] is the value of link usage
#            totalCost0.append(main(asn, ratio, 3, 0.7, 0)[0])
#            totalCost1.append(main(asn, ratio, 3, 0.7, 1)[0])
#        
#        avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
#        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
#        AvgList0.append(avgTemp0)
#        AvgList1.append(avgTemp1)
#        print 'Average totalCost0=', avgTemp0
#        print 'Average totalCost1=', avgTemp1
#    
#    print 'cost%dAlgo0='%asn, AvgList0
#    print 'cost%dAlgo1='%asn, AvgList1

##########################################################################
# Calculate the cost and link usage vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
def CalResultOfZipf(asn):
    AvgCostList0 = []   
    AvgCostList1 = []
    
    AvgLinkUsageList0 = []   
    AvgLinkUsageList1 = []
    
    for alpha in np.arange(0.6, 1.41, 0.05):
        totalCost0 = []
        totalCost1 = []
        
        totalLinkUsage0 = []
        totalLinkUsage1 = []
        
        
        for i in range(10):
            costTemp0, usageTemp0 = main(asn, 0.2, 3, alpha, 0)
            costTemp1, usageTemp1 = main(asn, 0.2, 3, alpha, 1)

            totalCost0.append(costTemp0)
            totalCost1.append(costTemp1)

            totalLinkUsage0.append(usageTemp0)
            totalLinkUsage1.append(usageTemp1)

        
        avgCostTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
        avgCostTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)

        avgUsageTemp0 = sum(totalLinkUsage0)/(len(totalLinkUsage0) + 0.0)
        avgUsageTemp1 = sum(totalLinkUsage1)/(len(totalLinkUsage1) + 0.0)
        
        AvgCostList0.append(avgCostTemp0)
        AvgCostList1.append(avgCostTemp1)
        
        AvgLinkUsageList0.append(avgUsageTemp0)   
        AvgLinkUsageList1.append(avgUsageTemp1)
        
        
        print 'Average totalCost0=', avgCostTemp0
        print 'Average totalCost1=', avgCostTemp0
        
        print 'Average totalUsage0=', avgUsageTemp0
        print 'Average totalUsage1=', avgUsageTemp1
    
    print 'cost%dAlgo0='%asn, AvgCostList0
    print 'cost%dAlgo1='%asn, AvgCostList1

    print 'linkUsage%dAlgo0='%asn, AvgLinkUsageList0
    print 'linkUsage%dAlgo1='%asn, AvgLinkUsageList1
     
       
########################################################################
    

##########################################################################
# Replaced by the previous function
# Calculate the cost vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
#def CalCostOfZipf(asn):
#    AvgList0 = []   
#    AvgList1 = []    
#    for alpha in np.arange(0.6, 1.41, 0.05):
#        totalCost0 = []
#        totalCost1 = []
#        for i in range(10):
#            totalCost0.append(main(asn, 0.2, 3, alpha, 0)[0])
#            totalCost1.append(main(asn, 0.2, 3, alpha, 1)[0])
#        
#        avgTemp0 = sum(totalCost0)/(len(totalCost0) + 0.0)
#        avgTemp1 = sum(totalCost1)/(len(totalCost1) + 0.0)
#        AvgList0.append(avgTemp0)
#        AvgList1.append(avgTemp1)
#        print 'Average totalCost0=', avgTemp0
#        print 'Average totalCost1=', avgTemp1
#    
#    print 'cost%dAlgo0='%asn, AvgList0
#    print 'cost%dAlgo1='%asn, AvgList1
########################################################################
    
##########################################################################
# Calculate the cost vs. zipf alpha for every AS
#main(asn = 1221, cacheRatio=0.2, delayLimit = 3, alpha, algo = 0)
def CalCostOfDelaySingle(asn):
#    AvgList0 = []   
    AvgList1 = []
        
    for delay in np.arange(0.5, 20, 0.5):
#        totalCost0 = []
        totalCost1 = []
        for i in range(10):
    #        totalCost0.append(main(asn, 0.2, delay, 0.7, 0))
            totalCost1.append(main(asn, 0.2, delay, 0.7, 1)[0])
        
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
            totalCost0.append(main(asn, 0.2, delay, 0.7, 0)[0])
            totalCost1.append(main(asn, 0.2, delay, 0.7, 1)[0])
        
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
def CalResultOfAllASes():
    asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
    avgCost0 = []
    avgCost1 = []
    
    avgLinkUsage0 = []
    avgLinkUsage1 = []
    
    for asn in asnCare:
        totalCost0 = []
        totalCost1 = []
          
        totalLinkUsage0 = []
        totalLinkUsage1 = []
        
        for i in range(10):
            # Compare the cost of two algo uder certain circumstance
            # asn = 7018, ratio = 0.2, delay=3ms, alpha=0.7,
            costTemp0, linkUsageTemp0 = main(asn, 0.2, 3, 0.7, 0)
            costTemp1, linkUsageTemp1 = main(asn, 0.2, 3, 0.7, 1)
            
            totalCost0.append(costTemp0)
            totalCost1.append(costTemp1)
            
            totalLinkUsage0.append(linkUsageTemp0)
            totalLinkUsage1.append(linkUsageTemp1)
            
        avgCost0.append(sum(totalCost0)/(len(totalCost0) + 0.0))
        avgCost1.append(sum(totalCost1)/(len(totalCost1) + 0.0))
        
        avgLinkUsage0.append(sum(totalLinkUsage0)/(len(totalLinkUsage0) + 0.0))
        avgLinkUsage1.append(sum(totalLinkUsage1)/(len(totalLinkUsage1) + 0.0))
        
        
    
    print 'avgCost0=', avgCost0
    print 'avgCost1=', avgCost0
    print 'avgLinkUsage0=', avgLinkUsage0
    print 'avgLinkUsage1=', avgLinkUsage1
    
######################################################################
    
##########################################################################
# Replaced by the previous function
# Calculate the cost for every AS
# The other papameters are main(asn, 0.2, 3, 0.7, 0))
#########################################################################
#def CalCostOfAllASes():
#    asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)
#    avg0 = []
#    avg1 = []
#    
#    for asn in asnCare:
#        totalCost0 = []
#        totalCost1 = []
#          
#        for i in range(10):
#            # Compare the cost of two algo uder certain circumstance
#            # asn = 7018, ratio = 0.2, delay=3ms, alpha=0.7,
#            totalCost0.append(main(asn, 0.2, 3, 0.7, 0)[0])
#            totalCost1.append(main(asn, 0.2, 3, 0.7, 1)[0])    
#            
#        avg0.append(sum(totalCost0)/(len(totalCost0) + 0.0))
#        avg1.append(sum(totalCost1)/(len(totalCost1) + 0.0))
#    
#    print 'avg0=', avg0
#    print 'avg1=', avg1
######################################################################


asn = int(sys.argv[1])
op = int(sys.argv[2])

if op == 0:
    CalResultOfRatio(asn)
elif op == 1:
    CalResultOfZipf(asn)
elif op == 2:
    CalCostOfDelaySingle(asn)
elif op == 3:
    CalCostOfDelay(asn)
elif op == 4:
    CalResultOfAllASes()
else:
    sys.stderr.write('option value error!\n')
    
    
