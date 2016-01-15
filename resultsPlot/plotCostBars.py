#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)

#Old dataset

#avg0= [0.1941743445972864, 0.12422826200597799, 0.16995952491759017, 0.16672557521663647, 0.22021251445425075, 0.0708754104703567, 0.1327374602131554, 0.1737049400980204, 0.15522235112023047]
#avg1= [0.30178489050225343, 0.26156975468144006, 0.33928885775803014, 0.41740201085482553, 0.3339680038470235, 0.11608300947767822, 0.2925469100860202, 0.3295929002230972, 0.3378434658826166]

avg0= [0.20083810976347535, 0.15051533768381747, 0.16107180208916966, 0.17599008263506238, 0.24744509317873636, 0.13326010199613963, 0.3107858201377537, 0.17700982107138738, 0.12576235873738525]
avg1= [0.3331894118213721, 0.3088949091659557, 0.3326342808198167, 0.41377464864883384, 0.47264318044402, 0.4529982450263247, 0.4426186823248706, 0.3305423791242398, 0.43790289721603026]


avgMax = max(avg0+avg1)
avg0 = np.array(avg0)/avgMax
avg1 = np.array(avg1)/avgMax

print 'Average cost reduce ratio=', (sum(avg1)-sum(avg0))/sum(avg1)

N = 9
width = 0.2       # the width of the bars
x = np.linspace(0, width*2*N + 0.2, N)  # the x locations for the groups

#x = np.arange(N)                # the x locations for the groups
#width = 0.35                      # the width of the bars

#patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')
#hatch of bars
plt.bar(x, avg0, width, color='white', hatch = '/', label='SCM-based algo',) #align='center'
plt.bar(x+width, avg1, width, color='black', hatch = '\\\\', label='Baseline algo', alpha=0.6) #align='center'
 
#plt.xlabel('AS number', fontsize=14)
plt.ylabel('Normalized cost', fontsize=15)
plt.xticks(x+width, ('AS1221', 'AS1239', 'AS2914', 'AS3257', 'AS3356', 
                     'AS3967', 'AS4755', 'AS6461', 'AS7018'), rotation=45, fontsize = 14)

plt.yticks(np.arange(0, 1.1, 0.2), ('0', '0.2', '0.4', '0.6', '0.8', '1.0'), fontsize = 14)
plt.ylim(0, 1.03)

# Adjusting xlim to display all AS
plt.xlim(0, width*2*N + 0.7)

#plt.subplots_adjust(bottom=0.15, left=0.08)
plt.tight_layout()
plt.legend(fontsize=14, loc='upper left')

plt.show()
