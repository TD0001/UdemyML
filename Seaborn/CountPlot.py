import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")
pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
pd.options.display.max_rows = None

ax=sns.countplot(x='Mfr Name', data=df)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
print()
plt.show()