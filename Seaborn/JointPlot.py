import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("FuelEfficiency.csv")

pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
pd.options.display.max_rows = None
print(df)

sns.jointplot(x="Eng Displ", y="CombMPG", data=df)
plt.show()
# Seaborn also offers a "jointplot",
# which combines a scatterplot with histograms on both axes.
# This lets you visualize both the individual data points and
# the distribution across both dimensions at the same time.