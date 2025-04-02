import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
df = pd.read_csv("Students_Grading_Dataset.csv")

# Univariate analysis of Numeric variables
numeric_cols = df.select_dtypes(exclude="object").columns

nrows = 4
ncols = 3
i = 0
# use the default style
plt.style.use("default")

fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 12))

for row in range(nrows):
    for col in range(ncols):
        dist = df[numeric_cols[i]]
        sns.histplot(dist, kde=True, alpha=.4, ax=ax[row, col])
        ax[row, col].axvline(dist.mean(), color="r", linestyle='dashed', label=f"Mean: {int(dist.mean())}")
        ax[row, col].axvline(dist.median(), color="black", linestyle='-.', label=f"Median: {int(dist.median())}")
        ax[row, col].legend()
        i+=1

plt.tight_layout()
plt.show()
