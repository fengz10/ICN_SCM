#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 6461, 7018)


avg0= [0.12984119834535107, 0.02923629246499998, 0.034940607428428506, 0.086563541767430668, 0.052749753528142339, 0.16539182497639121, 0.091066036931846256, 0.026153045575686762]
avg1= [0.13138994901637588, 0.0312064189835226, 0.039402807302266141, 0.12890317053104222, 0.054524394149652974, 0.21078750885882899, 0.095836793936314418, 0.030939422057777853]




avgMax = max(avg0+avg1)
avg0 = np.array(avg0)/avgMax
avg1 = np.array(avg1)/avgMax

print 'Average cost reduce ratio=', (sum(avg1)-sum(avg0))/sum(avg1)

N = 8
width = 0.2       # the width of the bars
x = np.linspace(0, width*2*N + 0.2, N)  # the x locations for the groups

#x = np.arange(N)                # the x locations for the groups
#width = 0.35                      # the width of the bars

#patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')
#hatch of bars
plt.bar(x, avg0, width, color='white', hatch = '/', label='SCM-based algo',) #align='center'
plt.bar(x+width, avg1, width, color='black', hatch = '\\\\', label='Baseline algo', alpha=0.6) #align='center'
 
#plt.xlabel('AS number', fontsize=14)
plt.ylabel('Normalized link usage', fontsize=15)
plt.xticks(x+width, ('AS1221', 'AS1239', 'AS2914', 'AS3257', 'AS3356', 
                     'AS3967', 'AS6461', 'AS7018'), rotation=45, fontsize = 14)

plt.yticks(np.arange(0, 1.1, 0.2), ('0', '0.2', '0.4', '0.6', '0.8', '1.0'), fontsize = 14)
plt.ylim(0, 1.03)

# Adjusting xlim to display all AS
plt.xlim(0, width*2*N + 0.7)

#plt.subplots_adjust(bottom=0.15, left=0.08)
plt.tight_layout()
plt.legend(fontsize=14, loc='upper left')

plt.show()
