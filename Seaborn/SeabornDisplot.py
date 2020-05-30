import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")

print(df)
print("---------------------------------------")
print(df.head())
print("---------")
print(df.tail())
sns.set()
sns.distplot(df['HwyMPG'])
plt.show()

