import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv("clgt.csv")
print(df)
print("------------------------------------------")
print(df.head(2))
print("-----------------------------------------")
print(df.tail(3))
print("----------------------------------------")
print(df.size) #rows*colums
print(df.shape) #
print(len(df)) #number of rows
print("----------------------------------------")
print(df['Brand'])
print("----------------------------------------")
print(df['Brand'][:2])#split and get 2 first
print("----------------------------------------")
print(df['Brand'][2:])#split and get 2 last
print("----------------------------------------")
print(df['Brand'].value_counts())
print("-----------------------------"
      "-----------")
# print(df[df['Brand']].sort_values())#sort the column
print(   (df['Brand'].value_counts()).plot(kind = 'line')     )
plt.show()