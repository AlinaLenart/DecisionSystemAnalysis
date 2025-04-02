import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Wczytanie danych
df = pd.read_csv("Students_Grading_Dataset.csv")

# Konwersja na uporządkowaną kategorię (ważne!)
edu_order = ["None", "High School", "Bachelor's", "Master's", "PhD"]
df["Parent_Education_Level"] = pd.Categorical(df["Parent_Education_Level"], categories=edu_order, ordered=True)

# Grupowanie
group_col = "Parent_Education_Level"
value_col = "Total_Score"

grouped = df.groupby(group_col, observed=True)[value_col].agg(['mean', 'count', 'std']).reset_index()
grouped['se'] = grouped['std'] / np.sqrt(grouped['count'])

# Wykres
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, height_ratios=[1, 1])

# Górny panel: średnia z SE
ax1.errorbar(
    x=grouped[group_col],
    y=grouped['mean'],
    yerr=grouped['se'],
    fmt='-o',
    capsize=5,
    color='tab:green',
    linewidth=2
)
ax1.set_title("Średni Total Score względem poziomu wykształcenia rodziców")
ax1.set_ylabel("Total Score")

# Dolny panel: rozrzut punktów
sns.stripplot(data=df, x=group_col, y=value_col, ax=ax2, jitter=0.25, alpha=0.6, color='tab:green', size=4)
ax2.set_title("Rozrzut wyników Total Score względem wykształcenia rodziców")
ax2.set_xlabel("Parent Education Level")
ax2.set_ylabel("Total Score")

plt.tight_layout()
plt.show()
