#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

delay = np.arange(0.5, 20, 0.5)

cost7018 = [0.7664153908065725, 0.41073266980166556, 0.22278195417283095, 0.2044575963185114, 0.13465349640271282, 0.11062262679580011, 0.09114014278375193, 0.09241834128439025, 0.0670275104854754, 0.065910174812325, 0.0544052646756372, 0.056057098316345644, 0.03940756305472455, 0.049139990097829864, 0.028363315809568457, 0.0344610202536546, 0.020924215493701707, 0.018963933246541283, 0.016122313185256396, 0.01236818754030108, 0.01209086188102093, 0.010110721716645158, 0.010377497702638594, 0.006829135598455821, 0.006835797212650395, 0.006474380394995276, 0.005966456888338469, 0.0065580184315153335, 0.005016924427648721, 0.005231351278472678, 0.008365666961430946, 0.0039008409399591986, 0.004157050703707425, 0.0026868143948580447, 0.003165629939836914, 0.0027936616666761347, 0.002482959988509118, 0.0036939648573884377, 0.002835760131598515]

cost7018 = np.array(cost7018)/max(cost7018)


# Discard since too many noisy data
#cost7018Algo0= [0.5134822665107843, 0.5721263787238307, 0.2635121506535606, 0.14079399730005993, 0.14376483838605741, 0.08591328267645423, 0.10206785346369703, 0.059521485785092525, 0.05948084818944274, 0.08157161863226209, 0.06931549761937074, 0.04603452505799543, 0.032050690471246604, 0.035433318338689596, 0.038101750633351625, 0.027378060610547806, 0.024302204615899665, 0.030521593309242128, 0.015920219378835063, 0.01916797974907178, 0.02165300206775971, 0.00850473831100898, 0.00968864821673108, 0.009520473107272174, 0.007731100274221526, 0.013393841077819787, 0.011525837093954525, 0.006582553480869898, 0.0051984211518518115, 0.004189843307956792, 0.003243321299963072, 0.0025487367079304445, 0.0028284303667211706, 0.0027079479866239094, 0.002838715388506403, 0.0032526301505182227, 0.0052010827658911605, 0.0023064758563894516, 0.0018816554134232734]
#cost7018Algo1= [0.5273880685604764, 0.5271603711452721, 0.3824471352158841, 0.2853724016235656, 0.30047249414985044, 0.2682148921217091, 0.2053350348625909, 0.21977343855833711, 0.2448386977155315, 0.16796221457542146, 2.304147447943576, 0.21830433215231645, 0.3552888750544094, 0.1788764191565578, 0.3847693646702023, 1.7131787152870295, 0.2687020518739203, 0.2262564223194352, 0.24076188985700867, 0.27126064027829433, 0.14970776203040545, 0.1804730378672832, 0.270442191971851, 0.16358402420337176, 0.19272817127455935, 0.393114856568319, 0.1819975474846727, 0.7253976111498258, 0.1279407652265394, 0.2118588667821203, 0.1683548038124034, 0.15057677588133112, 0.19954075035976324, 0.1677631868080839, 0.13842483429801686, 0.16055158651958573, 0.11631713210919152, 0.25818031400357, 0.1210165105491008]

#Normalizing
#max7018 = max(cost7018Algo0+ cost7018Algo1)
#cost7018Algo0 = np.array(cost7018Algo0)/max7018
#cost7018Algo1 = np.array(cost7018Algo1)/max7018


cost3356 = [0.7026994703628718, 0.38214288751939374, 0.2557046163632778, 0.23089642285364823, 0.19952981781725893, 0.13759899212579063, 0.1650295134667201, 0.12167669049083493, 0.07789095717703252, 0.13486090507810736, 0.10032071210687579, 0.08704097655700557, 0.05849463874039314, 0.056943184328637056, 0.04423512311753861, 0.03449399358009193, 0.03220950581124847, 0.03666459801229956, 0.027670874521330012, 0.02678631544031617, 0.01957857403348754, 0.02507244236786451, 0.021906783283438556, 0.020799888701115578, 0.020311936091420665, 0.017674650354893497, 0.02273470379585775, 0.016932956791285668, 0.04275924609360684, 0.016760722464627547, 0.01651207837622192, 0.010812877676969769, 0.014906936779289314, 0.014244073922405823, 0.014455163134192253, 0.015598536332258023, 0.010766716080318752, 0.018771633421377467, 0.010696091940450807]

#Normalizing
cost3356 = np.array(cost3356)/max(cost3356)


# Discard since too many noisy data
#cost3356Algo0= [0.696076838967598, 0.41175365702668715, 0.21727762858113184, 0.27059207513401373, 0.21861831700399384, 0.1552818221841558, 0.08747087371696251, 0.10310237824300772, 0.1124306101764447, 0.05565457365066836, 0.09633070320970298, 0.08421132243038261, 0.05472801722338655, 0.06727138588936117, 0.041052754983267645, 0.034159996818273225, 0.02088649400680509, 0.037917321484332314, 0.9090152792769669, 0.025231938672961075, 0.015234851544170853, 0.019513496148042264, 0.02392445519713128, 0.023198946884638957, 0.01663644273529124, 0.0516128465304601, 0.013487447274689139, 0.013363797404981314, 0.01285572698003299, 0.018386347022948793, 0.061610915583761534, 0.011219178166135265, 0.016907596281782292, 0.010177724374545198, 0.03018538389425513, 0.035328423832944315, 0.019169017084469206, 0.020440464429330698, 0.009365507767877021]
#cost3356Algo1= [0.8066030179003812, 0.631665035549781, 0.3254998254924471, 0.234622003831605, 0.17662196762743282, 0.29540470076267383, 0.24286846023034828, 0.30051701700496725, 0.22236171976051708, 0.257170461822257, 0.42837402886200865, 0.3146440072566563, 0.3293428009603855, 0.2660205367401322, 0.33233088768489377, 0.2696619102616101, 0.22014134846146063, 0.7751845620627493, 0.24511739036844102, 0.2997475055750163, 0.23866980270157634, 0.28359017483402, 0.2665253050681607, 0.7549643990814593, 0.3790666002161969, 0.23600681766499443, 0.21105177867306832, 0.2887999946225078, 0.2822090355475393, 0.2898723700784262, 0.36374664329942497, 0.22869641067288063, 0.29009536681078785, 0.28609345291986793, 0.315559661169713, 0.2646379301856123, 0.4094208277986023, 0.7744806080742447, 0.4504331151789082]
#
#max3356 = max(cost3356Algo0+ cost3356Algo1)
#cost3356Algo0 = np.array(cost3356Algo0)/max3356
#cost3356Algo1 = np.array(cost3356Algo1)/max3356




cost3257 = [0.7052830812566205, 0.4285316334574885, 0.3538718920895866, 0.17974696473248097, 0.21787081425778904, 0.18911987783447298, 0.11656153285481255, 0.12497581602558525, 0.22768544492680362, 0.10268660775645881, 0.10389981513845008, 0.12234416998190334, 0.08441543271972443, 0.21701883567437208, 0.27919577283837926, 0.08412104538364214, 0.10100222117046316, 0.0793842730018901, 0.08240940935839128, 0.08821348892451898, 0.07202867239395955, 0.07900953168969535, 0.07862614401934018, 0.07437895947654796, 0.05411949016418357, 0.09664538837325891, 0.055193066296632474, 0.07781451940787967, 0.0651108783629606, 0.0745474067804017, 0.054122035640983925, 0.0756668782609422, 0.039959087302333454, 0.04546845434899593, 0.048505066012789894, 0.0424736193638936, 0.04552942289671989, 0.04291405259846503, 0.048604943614149874]

#Normalizing
cost3257 = [x/0.70528308 for x in cost3257]
#AS 3257 data has more noise

cost2914 = [0.6364233383440936, 0.45853297117346675, 0.2118401903786991, 0.15489467988292843, 0.1599052068698862, 0.1820596411295267, 0.11563374078178108, 0.09672713664328056, 0.10559867230660396, 0.08306998254657745, 0.05530869758909186, 0.0754864889514455, 0.05562774248551081, 0.05632099606699552, 0.06956819163646055, 0.037764504773381835, 0.03528533598207921, 0.032901871175245685, 0.029779824725612573, 0.024878701744210106, 0.03268188217324459, 0.020130078419298026, 0.020510078137462296, 0.021252242268444847, 0.021280461636943675, 0.017278079636860663, 0.017588144911242172, 0.01598090222191087, 0.01611452738301004, 0.013732915203164492, 0.018319645118041412, 0.015772724578065764, 0.013364567147410467, 0.01605863966212307, 0.012031134861428715, 0.013336470403618591, 0.01764619802824739, 0.037866093263763986, 0.011804884102705162]

#Normalizing
cost2914 = [x/0.636423338 for x in cost2914]

cost3967 = [0.24520000160252858, 0.17203697496601683, 0.0973276024986132, 0.05733238809400466, 0.08193441867103368, 0.05965516482489316, 0.050531525574675884, 0.05273644173727905, 0.05765445375858974, 0.06525306851162746, 0.041523680232983876, 0.0503256852522854, 0.04084559675097527, 0.05586159117793106, 0.061755415467706444, 0.06909815796150451, 0.033999792099463855, 0.04033225847557329, 0.04360035938277994, 0.042058132535096104, 0.031420581790361675, 0.050786317040129855, 0.04735974177781225, 0.04299795182174747, 0.04135705527412389, 0.04730469907416771, 0.04141365054978589, 0.05012510290726822, 0.04090360869409241, 0.04502780102198478, 0.05476012792013929, 0.05975670720345414, 0.055943713843474255, 0.04453478647646741, 0.0491550031411038, 0.04036659371325072, 0.04986505518124799, 0.03877786607334059, 0.0420738861877379]

#Normalizing
cost3967 = [x/0.2452 for x in cost3967]

cost6461 = [0.5653535645528656, 0.5526958539943179, 0.2597675767730624, 0.26231433812725835, 0.23069092435143007, 0.16934163960697138, 0.15358959320370583, 0.12554101691806432, 0.1040197440361879, 0.28195524927220134, 0.16608301050226132, 0.11213262068273236, 0.16117224940451721, 0.09321894828038835, 0.06031889810243228, 0.0735436623308868, 0.08484134030252546, 0.062183602450932504, 0.06577223309074212, 0.06640740867203117, 0.05933754222661034, 0.04959184975321877, 0.06414786757763243, 0.06165270959869784, 0.0492200244646821, 0.05702015827033692, 0.059732320735324085, 0.053764727735153325, 0.04100294105404232, 0.04496958134708533, 0.04179890960348029, 0.04243890281272045, 0.04417191299179435, 0.04597539811412549, 2.18659622891491, 0.05124122838186738, 0.041493265510537815, 0.11240834583640018, 0.045761879741262064]

#Normalizing
cost6461 = [x/0.5653535 for x in cost6461]

# Comment
plt.plot(delay, cost7018, "kD-", label="SCM-base AS7018", markersize = 8, linewidth=2)
#plt.plot(delay, cost7018Algo1, "kD--", label="AS 7018", markersize = 8, linewidth=2)
plt.plot(delay, cost3356, "b^-",label="SCM-base AS 3356", markersize = 8, linewidth=2)
#plt.plot(delay, cost3356Algo1, "b^--",label="AS 3356", markersize = 8, linewidth=2)
plt.plot(delay, cost3967, "rs-", label ="SCM-base AS 3967", markersize = 8, linewidth=2)
plt.plot(delay, cost2914, "go-", label ="SCM-base AS 2914", markersize = 8, linewidth=2)
#plt.plot(delay, cost6461, "g*-", label ="AS 6461", markersize = 8, linewidth=2)


plt.xticks(range(0,21,5),('0', '5', '10', '15', '20'), fontsize = 14)
plt.yticks(np.arange(0, 1.1, 0.2), ('0', '0.2', '0.4', '0.6', '0.8', '1.0'), fontsize = 14)
plt.ylim([0, 1.03])
plt.xlabel('Delay (ms)',fontsize = 14) 
plt.ylabel('Normalized cost',fontsize = 14) 

plt.legend(fontsize = 14)
#pylab.legend(loc='upper right')
plt.tight_layout()
plt.show()