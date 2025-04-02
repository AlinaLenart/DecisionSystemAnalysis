import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)


plt.figure(figsize=(12, 6))
sns.violinplot(x="Grade", y="Family_Income_Level", hue="Department", data=df, split=True, palette="coolwarm", inner=None)

# Set labels and title
plt.xlabel("Grade")
plt.ylabel("Family Income Level")
plt.title("Distribution of Family Income Level by Grade and Department")

# Show plot
plt.legend(title="Department")
plt.show()


