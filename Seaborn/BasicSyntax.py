# Seaborn is a visualization library that sits on top of matplotlib,
# making it nicer to look at
#
# and adding some extra capabilities too.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")

gear_counts = df['# Gears'].value_counts()

sns.set()
gear_counts.plot(kind='bar')
plt.show()
print(df)
print("---------------------------------------")
print(df.head())
