import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_regressions(df, output_dir):

    sns.set_style("whitegrid")

    plt.figure(figsize=(8, 6))
    sns.regplot(
        data=df,
        x="Study_Hours_per_Week",
        y="Midterm_Score",
        line_kws={'color': "red"},
        scatter_kws={"alpha": 0.6, "s": 30}
    )

    plt.title("Study Hours per Week vs Midterm Score")
    plt.xlabel("Study Hours per Week")
    plt.ylabel("Midterm Exam Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "regression.png"))
    plt.close()
