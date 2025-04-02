import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)

# Tworzymy alfabetyczną listę unikalnych ocen
sorted_grades = sorted(df['Grade'].dropna().unique())

# Tworzymy boxplot z określoną kolejnością kategorii
plt.figure(figsize=(10, 6))
sns.boxplot(x='Grade', y='Attendance (%)', data=df, palette='coolwarm', order=sorted_grades)
plt.title('Boxplot of Grade vs Attendance (%)')
plt.xlabel('Grade')
plt.ylabel('Attendance (%)')
plt.show()

sns.boxplot(x="Grade",y="Attendance (%)",data=df.sort_values(by="Grade", ascending=[True]), palette="crest")
plt.show()
