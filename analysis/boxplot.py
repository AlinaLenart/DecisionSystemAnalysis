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
    plt.savefig(os.path.join(output_dir, "boxplot.png"))
    plt.close()

    pass


# def save_boxplots(df, output_dir):
#     excluded = {"Student_ID", "First_Name", "Last_Name", "Email"}
#     cat_cols = df.select_dtypes(exclude=["number"]).columns.difference(excluded).tolist()

#     target_col = "Total_Score"  # <- zmień na swoją zmienną celu

#     # Parametry siatki
#     rows, cols = 2, 4
#     fig, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(14, 8))
#     i = 0

#     # Rysujemy boxploty w siatce
#     for row in range(rows):
#         for col in range(cols):
#             if i >= len(cat_cols):
#                 ax[row, col].axis("off")  # Wyłącz puste pola
#                 continue
#             feature = cat_cols[i]
#             sns.boxplot(data=df, x=feature, y=target_col, ax=ax[row, col])
#             ax[row, col].set_title(f"{feature} vs {target_col}")
#             ax[row, col].tick_params(axis="x", rotation=30)
#             i += 1

#     plt.tight_layout()
#     plt.show()

#     pass


# def save_boxplots(df, output_dir):
#     sorted_grades = sorted(df['Grade'].dropna().unique())

#     # Tworzymy boxplot z określoną kolejnością kategorii
#     plt.figure(figsize=(10, 6))
#     # sns.boxplot(x='Grade', y='Attendance (%)', data=df, palette='coolwarm', order=sorted_grades)
#     plt.title('Boxplot of Grade vs Attendance (%)')
#     plt.xlabel('Grade')
#     plt.ylabel('Attendance (%)')
#     sns.boxplot(x="Grade",y="Attendance (%)",data=df.sort_values(by="Grade", ascending=[True]), palette="crest")
#     plt.show()

#     pass


