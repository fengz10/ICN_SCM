#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

ratio = np.arange(0, 1.01, 0.05)

# Data from AS 7018
# Other inputs are: main(7018, ratio, 3, 0.7, 0)

cost7018Algo0= [0.32816886868289885, 0.2208175601847247, 0.19251093813725606, 0.19213511824943674, 0.13080090885015863, 0.11537045883303, 0.09633102587606322, 0.07323609921126092, 0.09878431485204239, 0.05596993118756234, 0.049715428600860076, 0.03831044043548079, 0.06096882335052019, 0.028069296806645244, 0.022701113201547628, 0.021278104632073535, 0.013507052814121217, 0.026153265780405686, 0.0077527277733091485, 0.0031476608134015918, 0.0]
cost7018Algo1= [0.4642333921367071, 0.4639016472999131, 0.34012817677104124, 0.3340296081862053, 0.2969448732402059, 0.2461004974625, 0.2293186323481248, 0.24091214725010093, 0.19757595572768757, 0.1573243340317513, 0.18058477722058466, 0.12481420007040704, 0.10774395529769458, 0.09029783974164379, 0.09634065693940172, 0.08223281518431566, 0.09567750993009355, 0.04277884030146324, 0.028210440967304917, 0.017676653196543032, 0.004847344478943003]


max7018 = max(cost7018Algo0+ cost7018Algo1)
cost7018Algo0 = np.array(cost7018Algo0)/max7018
cost7018Algo1 = np.array(cost7018Algo1)/max7018


cost3356Algo0= [0.2783048731245389, 0.2872432864239341, 0.2230858096827762, 0.2056502418089665, 0.19798701702638456, 0.17357493305249336, 0.1469459407732046, 0.10761056872908284, 0.0997999691042518, 0.09213445289884156, 0.092158282436989, 0.0660532265325018, 0.06295908184506546, 0.048358314991151494, 0.04045873505958472, 0.0315771474462309, 0.02590217889984478, 0.01820272272729274, 0.012580744472094682, 0.007715350715371399, 0.0]
cost3356Algo1= [0.465620584858123, 0.40481693415398573, 0.3875690687641232, 0.43758852738211623, 0.3165725611715618, 0.3024823915734399, 0.26220346926993093, 0.2474230687700476, 0.24382857244792552, 0.24630388944790402, 0.1923745910236931, 0.1700306921862092, 0.16211949681867985, 0.16401967368367437, 0.1757433455069511, 0.10131859386229136, 0.11147997172614468, 0.0849289440996695, 0.0715091535328963, 0.06055701261597678, 0.02902765654616049]


max3356 = max(cost3356Algo0+ cost3356Algo1)
cost3356Algo0 = np.array(cost3356Algo0)/max3356
cost3356Algo1 = np.array(cost3356Algo1)/max3356

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

cost2914Algo0= [0.2985484020511996, 0.3678774231683738, 0.22471345430585563, 0.16939513694727085, 0.16470375883534655, 0.1873554643571797, 0.12180635895053124, 0.08917217445175339, 0.09418009720668301, 0.08602255944435719, 0.06227133969465918, 0.05742111452629443, 0.08499951928274836, 0.04435617393119315, 0.03557660115877804, 0.04948879687046496, 0.027409612835835533, 0.01611151133230808, 0.011949694759354836, 0.005433847749368355, 0.0]
cost2914Algo1= [0.4797497500434348, 0.36931227813986284, 0.3535122401694411, 0.3566576719805158, 0.38640821560707106, 0.716213466629919, 0.2935314839639993, 0.39111587647765933, 0.25428746739263486, 0.2130828579687878, 0.20757244130193064, 0.17380156664179708, 0.2115447151728378, 0.15569996960790217, 0.12753165995647436, 0.16329856974988097, 0.1115194699256139, 0.10639665060119938, 0.0932164906718553, 0.09090296502695513, 0.29667733078299985]


max2914 = max(cost2914Algo0+ cost2914Algo1)
cost2914Algo0 = np.array(cost2914Algo0)/max2914
cost2914Algo1 = np.array(cost2914Algo1)/max2914






# Comment
plt.plot(ratio, cost7018Algo0, "kD-", label="SCM-base AS7018", markersize = 8, linewidth=2)
plt.plot(ratio, cost7018Algo1, "ro--", label="Baseline AS7018", markersize = 8, linewidth=2)
plt.plot(ratio, cost3356Algo0, "b^-",label="SCM-base AS3356", markersize = 8, linewidth=2)
plt.plot(ratio, cost3356Algo1, "gv--",label="Baseline AS3356", markersize = 8, linewidth=2)

#plt.plot(ratio, cost2914Algo0, "g<-", label ="SCM-base AS2914", markersize = 8, linewidth=2)
#plt.plot(ratio, cost2914Algo1, "g>--", label ="Baseline AS2914", markersize = 8, linewidth=2)


plt.xticks(np.arange(0,1.1,0.1),('0', '0.1', '0.2', '0.3', '0.4', '0.5', \
'0.6', '0.7', '0.8', '0.9', '1.0'), fontsize = 14)
plt.yticks(np.arange(0, 1.1, 0.2), ('0', '0.2', '0.4', '0.6', '0.8', '1.0'), fontsize = 14)
plt.ylim([0, 1.03])
plt.xlabel('Replicate ratio (%)',fontsize = 14) 
plt.ylabel('Normalized cost',fontsize = 14) 

plt.legend(fontsize = 14)
#pylab.legend(loc='upper right')
plt.tight_layout()
plt.show()