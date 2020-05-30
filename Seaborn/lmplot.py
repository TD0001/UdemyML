import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")

pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
pd.options.display.max_rows = None
print(df)

sns.lmplot(x="Eng Displ", y="CombMPG", data=df)
plt.show()
# The "lmplot" is a scatterplot,
# but with a linear regression line computed and overlaid onto the data.