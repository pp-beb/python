import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
np.random.seed(6)

population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000) 
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000) 
population_ages = np.concatenate((population_ages1, population_ages2))
minnesota_ages1 = stats.poisson. rvs(loc=18, mu=30, size=30) 
minnesota_ages2 = stats.poisson.rvs(loc=18, mu=10, size=20)
minnesota_ages = np.concatenate((minnesota_ages1, minnesota_ages2))

print( population_ages.mean() ) 
print( minnesota_ages.mean() )

a=population_ages.mean()
b=minnesota_ages.mean()
c=population_ages.mean()+1
d=population_ages.mean()+2
p=[a,b,c,d]
d=[1,2,3,4]
fig=plt.figure(figsize=(10,7))
plt.pie(p,labels=d)
plt.show()


barA=[10,20,30,10,20,10]
nameA=['a','b','c','d','e','f']
plt.bar(nameA,barA)
plt.title('wyawyawya')
plt.xlabel('names')
plt.ylabel('BAr')
plt.show

sigma=minnesota_ages.std()/math.sqrt(50)

stats.t.interval(0.95,
                df=49,
                loc=minnesota_ages.mean(),
                scale=sigma)


stats.t.cdf(x=-2.5742, df=49)*2

stats.t.ppf(q=0.975, df=49)

stats.t.ppf(q=0.025, df=49)

print(t1.pvalue)

t1 = stats.ttest_1samp(a = minnesota_ages , popmean = population_ages.mean())
print(t1)

stats.ttest_1samp(a=minnesota_ages, popmean = population_ages.mean())