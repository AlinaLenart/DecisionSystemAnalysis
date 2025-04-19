import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_regressions(df, output_dir):

    sns.set_style("whitegrid")

    plt.figure(figsize=(8, 6))
    sns.regplot(
        data=df,
        x="Attendance (%)",
        y="Total_Score",
        line_kws={'color': "red"},
        scatter_kws={"alpha": 0.6, "s": 30}
    )

    plt.title("Study Hours per Week vs Midterm Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Total_Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "regression.png"))
    plt.close()
