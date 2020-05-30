import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]
print(df2.head())
sns.set(style="ticks", color_codes=True)
sns.pairplot(df2) #focus on Cylinders as the primary thing
plt.show()