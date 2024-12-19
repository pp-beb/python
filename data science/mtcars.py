import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

altcars = pd.read_csv("mtcars.csv")
mean=altcars['mpg'].mean()
count=len(altcars['mpg'])
median=altcars['mpg'].median()
mode=altcars['mpg'].mode()
values=[mean,count,median]
categories=["Mean","Datacount","Median"]
plt.bar(categories,values)
plt.title('Bar chart')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()

