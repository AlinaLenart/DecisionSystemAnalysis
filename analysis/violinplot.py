import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def save_violinplots(df, output_dir):

    study_cats = pd.qcut(df['Study_Hours_per_Week'], q=4, labels=["light", "moderate", "high", "very high"])

    plt.figure(figsize=(8, 6))
    sns.violinplot(
        x=study_cats,
        y=df['Final_Score'],
        hue=study_cats,
        palette="crest", 
        legend=False,      
        inner="box"      # to dodaje kreski 
    )

    plt.title("Final Exam Score by Study Time Category")
    plt.xlabel("Study Hours per Week")
    plt.ylabel("Final Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "violinplot1.png"))
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.violinplot(x="Grade", y="Family_Income_Level", hue="Department", data=df, split=True, palette="crest", inner=None)

    plt.xlabel("Grade")
    plt.ylabel("Family Income Level")
    plt.title("Distribution of Family Income Level by Grade and Department")
    plt.legend(title="Department")

    plt.savefig(os.path.join(output_dir, "violinplot2.png"))
    plt.close()
