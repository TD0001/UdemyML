import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")
pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
pd.options.display.max_rows = None

df2 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.set()
sns.heatmap(df2)
plt.show()