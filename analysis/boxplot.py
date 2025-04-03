import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def save_boxplots(df, output_dir):
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
    plt.savefig(os.path.join(output_dir, "boxplot1.png"))
    plt.close()


    sorted_grades = sorted(df['Grade'].dropna().unique())

    # Tworzymy boxplot z określoną kolejnością kategorii
    plt.figure(figsize=(10, 6))
    # sns.boxplot(x='Grade', y='Attendance (%)', data=df, palette='coolwarm', order=sorted_grades)
    plt.title('Boxplot of Grade vs Attendance (%)')
    plt.xlabel('Grade')
    plt.ylabel('Attendance (%)')
    sns.boxplot(x="Grade",y="Attendance (%)",data=df.sort_values(by="Grade", ascending=[True]), palette="crest")
    plt.savefig(os.path.join(output_dir, "boxplot2.png"))
    plt.close()




