import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("mtcars.csv")
mtcars=mtcars.rename(columns={'unnamed:0' : 'model'})
mtcars.index=mtcars.model
del mtcars["model"]
mtcars.head()
mtcars.mean(axis=0)
norm_data=pd.DataFrame(np.random.normal(size=100000))

norm_data.plot(kind="density",
               figsize=(10,10));

plt.vlines(norm_data.mean(),
           ymin=0,
           ymax=0.4,
           linewidth=5.0);

plt.vlines(norm_data.medain(),
           ymin=0,
           ymax=0.4,
           linewidth=2.0,
           color="red");


