import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)

# Podział na 4 grupy według czasu nauki
study_cats = pd.qcut(df['Study_Hours_per_Week'], q=4, labels=["light", "moderate", "high", "very high"])

# Rysowanie violin plotu z kreskami kwartylowymi
plt.figure(figsize=(8, 6))
sns.violinplot(
    x=study_cats,
    y=df['Final_Score'],
    palette="Set1",       # lub 'Set2', 'pastel', etc.
    inner="box"      # to dodaje kreski (25%, 50%, 75%)
)

plt.title("Final Exam Score by Study Time Category")
plt.xlabel("Study Hours per Week")
plt.ylabel("Final Score")
plt.tight_layout()
plt.show()
