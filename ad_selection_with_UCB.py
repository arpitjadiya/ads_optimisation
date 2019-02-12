# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:44:18 2018

@author: arpit
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:44:18 2018

@author: arpit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
dataset = pd.read_csv('Ads_CTR_Optimisation.csv').values

N=10000
d=10
ads_selected = []
number_of_selections=[0]*d
sums_of_rewards=[0]*d
totalreward=0
for n in range(N):
    max_upper_bound = 0
    ad=0
    for i in range(d):
        if(number_of_selections[i] > 0):
            average_reward = sums_of_rewards[i]/number_of_selections[i]
            delta_i = math.sqrt(3/2* math.log(n+1)/number_of_selections[i])
            upper_bound = average_reward+delta_i
        else:
            upper_bound=1e399
        if(max_upper_bound<upper_bound):
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward=dataset[n,ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    totalreward = totalreward +reward           
        
plt.hist(ads_selected)
plt.xlabel('ad')
plt.ylabel('number of selections')
plt.title('optimized ads')
    
