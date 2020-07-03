import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
pd.options.display.max_rows = None
# pd.set_option('display.max_columns', None)
pd.options.display.max_columns = None
print(df)


print("-----------------------------------------------------")
df1=df[['Mileage','Price']]
bins =  np.arange(0,50000,10000)
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()
print(groups)
groups['Price'].plot.line()
plt.show()

import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

x = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']
print("-----------------------------------------------------")
print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
print(y)
print("-----------------------------------------------------")
# x = scale.fit_transform(x.as_matrix())

# print(y)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print (x)
print("est = ")
est = sm.OLS(y, x).fit()
print(est)

print("-------------SUMMARY---------------")
est.summary()
print(est.summary())
