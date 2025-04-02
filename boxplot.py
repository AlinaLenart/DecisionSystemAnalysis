import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)

# Kolumny do pominięcia
excluded_cols = {"Student_ID", "First_Name", "Last_Name", "Email"}

# Wybieramy tylko kolumny numeryczne z wyłączeniem excluded_cols
numeric_cols = df.select_dtypes(include=["number"]).columns.difference(excluded_cols).tolist()

# Rysujemy boxplot dla cech numerycznych
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[numeric_cols])
plt.title("Outlier Detection in Numerical Features")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


