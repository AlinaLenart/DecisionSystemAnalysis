import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)
# Zakładamy, że masz już wczytany DataFrame df
# I że cat_cols to lista kolumn kategorialnych, np.:
excluded = {"Student_ID", "First_Name", "Last_Name", "Email"}
cat_cols = df.select_dtypes(exclude=["number"]).columns.difference(excluded).tolist()

target_col = "Total_Score"  # <- zmień na swoją zmienną celu

# Parametry siatki
rows, cols = 2, 4
fig, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(14, 8))
i = 0

# Rysujemy boxploty w siatce
for row in range(rows):
    for col in range(cols):
        if i >= len(cat_cols):
            ax[row, col].axis("off")  # Wyłącz puste pola
            continue
        feature = cat_cols[i]
        sns.boxplot(data=df, x=feature, y=target_col, ax=ax[row, col])
        ax[row, col].set_title(f"{feature} vs {target_col}")
        ax[row, col].tick_params(axis="x", rotation=30)
        i += 1

plt.tight_layout()
plt.show()
