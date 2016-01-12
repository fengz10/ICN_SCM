#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


asnCare = (1221, 1239, 2914, 3257, 3356, 3967, 4755, 6461, 7018)

#Old dataset
#avg0= [0.18640828484844998, 0.1405643613161062, 0.1647024531249036, 0.1715571292628431, 0.14968693447002457, 0.21929679477229524, 0.12164534733773964, 0.21742658679680643, 0.16827650167483202]
#avg1= [0.23152380312234788, 0.27544035183229976, 0.40405428886890177, 0.296586222368432, 0.3384135270714669, 0.09308411370046468, 0.2548728840035476, 0.30543091690371293, 0.4072321859388519]

#Old dataset
#avg0= [0.2043616094037765, 0.1255403530344841, 0.13681177980848674, 0.19430396790589732, 0.1661422953603477, 0.0839934803522686, 0.3205533227209548, 0.3134546632470941, 0.12802794161241224]
#avg1= [0.30887418330354066, 0.6962762792242556, 0.5426890132644224, 0.3515167267945384, 0.3107184303086793, 0.13971966141410935, 0.3584185607303681, 0.4699036289625651, 0.28157481631835046]

avg0= [0.1941743445972864, 0.12422826200597799, 0.16995952491759017, 0.16672557521663647, 0.22021251445425075, 0.0708754104703567, 0.1327374602131554, 0.1737049400980204, 0.15522235112023047]
avg1= [0.30178489050225343, 0.26156975468144006, 0.33928885775803014, 0.41740201085482553, 0.3339680038470235, 0.11608300947767822, 0.2925469100860202, 0.3295929002230972, 0.3378434658826166]

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
plt.legend(fontsize=14, loc='upper middle')

plt.show()
