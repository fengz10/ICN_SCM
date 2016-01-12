#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

alpha = np.arange(0.6, 1.41, 0.05)

# Data from AS 7018

cost7018Algo0= [0.12051582744930762, 0.11680350313899748, 0.17274661546597944, 0.11378920637101424, 0.11109699871737504, 0.10542205421651518, 0.10350595818151391, 0.104131278995897, 0.07564572521700227, 0.08277083792435946, 0.06621432585417708, 0.055506674810766335, 0.05107156155128434, 0.03798561292042276, 0.032734977992961135, 0.038109150578393064, 0.02928238178543464]
cost7018Algo1= [0.38917259053782033, 0.292324986240057, 0.30671590108221036, 0.3002265624385025, 0.25467976248097524, 0.231949995384147, 0.2105889056686806, 0.19618585692113627, 0.16380233012215184, 0.21298467049033537, 0.14505599550260254, 0.13128497155061597, 0.1105193381102733, 0.1112477499134017, 0.09928948635273128, 0.07497745840830874, 0.08755067016443348]



max7018 = max(cost7018Algo0+ cost7018Algo1)
cost7018Algo0 = np.array(cost7018Algo0)/max7018
cost7018Algo1 = np.array(cost7018Algo1)/max7018


cost3356Algo0= [0.18273804458204693, 0.2017229168783265, 0.1597223261486454, 0.186871896459707, 0.13482577804752585, 0.14856751811805127, 0.1468669859830833, 0.10179600465592653, 0.13142124510806868, 0.09305728697349816, 0.07100590477936028, 0.08013254139368808, 0.05787108600527309, 0.05757024653984268, 0.04841736737369256, 0.06458783827057038, 0.03922614767252497]
cost3356Algo1= [0.36539245731944725, 0.3975109531196989, 0.3352062157065948, 0.29792023344095525, 0.3012409246472575, 0.25620615508047706, 0.2429658488568775, 0.23878783107276233, 0.2420295914569037, 0.24070051221814692, 0.17071661531500965, 0.16881784005255598, 0.12955536700168085, 0.12324852082972278, 0.1259310888437521, 0.08433431304300851, 0.07746855310588066]


max3356 = max(cost3356Algo0+ cost3356Algo1)
cost3356Algo0 = np.array(cost3356Algo0)/max3356
cost3356Algo1 = np.array(cost3356Algo1)/max3356




#
#max2914 = max(cost2914Algo0+ cost2914Algo1)
#cost2914Algo0 = np.array(cost2914Algo0)/max2914
#cost2914Algo1 = np.array(cost2914Algo1)/max2914


#########################Calculate reduced ratio############################
avg7018Alg0 = sum(cost7018Algo0)/len(cost7018Algo0)
avg7018Alg1 = sum(cost7018Algo1)/len(cost7018Algo1)
print 'cost reduced ratio of 7018'
print 'reduced ration = ', (avg7018Alg1 - avg7018Alg0)/avg7018Alg1

avg3356Alg0 = sum(cost3356Algo0)/len(cost3356Algo0)
avg3356Alg1 = sum(cost3356Algo1)/len(cost3356Algo1)
print 'cost reduced ratio of 3356'
print 'reduced ration = ', (avg3356Alg1 - avg3356Alg0)/avg3356Alg1

#######################################################################




# Comment
plt.plot(alpha, cost7018Algo0, "kD-", label="SCM-base AS7018", markersize = 8, linewidth=2)
plt.plot(alpha, cost7018Algo1, "ro--", label="Baseline AS7018", markersize = 8, linewidth=2)
plt.plot(alpha, cost3356Algo0, "b^-",label="SCM-base AS3356", markersize = 8, linewidth=2)
plt.plot(alpha, cost3356Algo1, "gv--",label="Baseline AS3356", markersize = 8, linewidth=2)

#plt.plot(ratio, cost2914Algo0, "g<-", label ="SCM-base AS2914", markersize = 8, linewidth=2)
#plt.plot(ratio, cost2914Algo1, "g>--", label ="Baseline AS2914", markersize = 8, linewidth=2)


plt.xticks(np.arange(0.6, 1.41, 0.1),('0.6', '0.7', '0.8', '0.9', '1.0', '1.1', \
'1.2', '1.3', '1.4'), fontsize = 14)
plt.yticks(np.arange(0, 1.1, 0.2), ('0', '0.2', '0.4', '0.6', '0.8', '1.0'), fontsize = 14)
plt.ylim(0, 1.05)
plt.xlim(0.6, 1.41)
plt.xlabel(r'$\alpha$ of Zipf',fontsize = 14) 
plt.ylabel('Normalized cost',fontsize = 14) 

plt.legend(fontsize = 14)
#pylab.legend(loc='upper right')
plt.tight_layout()
plt.show()