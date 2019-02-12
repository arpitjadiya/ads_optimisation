# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:55:15 2018

@author: arpit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


dataset = pd.read_csv('Ads_CTR_Optimisation.csv').values

N=10000
d=10
ads_selected=[]
total_reward = 0
for i in range(N):
    ad=random.randrange(d)
    ads_selected.append(ad)
    reward=dataset[i,ad]
    total_reward+=reward
    


plt.hist(ads_selected)
plt.xlabel('ad selected')
plt.ylabel('number of times it was selected')
plt.title('histogram of ads_selection')
plt.show()
