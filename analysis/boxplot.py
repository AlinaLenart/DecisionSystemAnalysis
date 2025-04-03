import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def save_boxplots(df, output_dir):

    excluded_cols = {"Student_ID", "First_Name", "Last_Name", "Email"}
    numeric_cols = df.select_dtypes(include=["number"]).columns.difference(excluded_cols).tolist()

    plt.figure(figsize=(10, 5))
    sns.set_style("whitegrid")
    sns.boxplot(data=df[numeric_cols], palette="rainbow")
    plt.title("Outlier Detection in Numerical Features")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "boxplot1.png"))
    plt.close()

    sorted_grades = sorted(df['Grade'].dropna().unique())
    df['Grade'] = pd.Categorical(df['Grade'], categories=sorted_grades, ordered=True)

    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.boxplot(
        x="Grade",
        y="Attendance (%)",
        hue="Grade",  
        data=df.sort_values(by="Grade"),
        palette="crest"
    )

    plt.title("Boxplot of Attendance (%) by Grade")
    plt.xlabel("Grade")
    plt.ylabel("Attendance (%)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "boxplot2.png"))
    plt.close()
