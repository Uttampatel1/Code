import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("SalaryGender.csv")
correlations = df.corr()
sns.heatmap(data = correlations,square = True, cmap = "bwr")

plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()
