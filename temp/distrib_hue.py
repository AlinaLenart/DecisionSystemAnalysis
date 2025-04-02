import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
df = pd.read_csv("Students_Grading_Dataset.csv")

plt.figure(figsize=(10, 6))
sns.catplot(x='Department', hue='Gender', col='Grade', data=df, kind='count', height=5, aspect=1.5, alpha=0.45)
plt.title('Department -wise Gender Distribution by Grade')
plt.show()
