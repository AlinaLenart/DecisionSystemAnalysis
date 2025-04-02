import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# def save_violinplots(df, output_dir):

#     study_cats = pd.qcut(df['Study_Hours_per_Week'], q=4, labels=["light", "moderate", "high", "very high"])

#     # Rysowanie violin plotu z kreskami kwartylowymi
#     plt.figure(figsize=(8, 6))
#     sns.violinplot(
#         x=study_cats,
#         y=df['Final_Score'],
#         palette="Set1",       # lub 'Set2', 'pastel', etc.
#         inner="box"      # to dodaje kreski (25%, 50%, 75%)
#     )

#     plt.title("Final Exam Score by Study Time Category")
#     plt.xlabel("Study Hours per Week")
#     plt.ylabel("Final Score")
#     plt.tight_layout()
#     plt.savefig(os.path.join(output_dir, "violinplot.png"))
#     plt.close()

    


def save_violinplots(df, output_dir):

    plt.figure(figsize=(12, 6))
    sns.violinplot(x="Grade", y="Family_Income_Level", hue="Department", data=df, split=True, palette="coolwarm", inner=None)

    # Set labels and title
    plt.xlabel("Grade")
    plt.ylabel("Family Income Level")
    plt.title("Distribution of Family Income Level by Grade and Department")

    # Show plot
    plt.legend(title="Department")
    plt.savefig(os.path.join(output_dir, "violinplot.png"))
    plt.close()



    
