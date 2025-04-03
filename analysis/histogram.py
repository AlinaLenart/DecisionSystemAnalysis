import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def save_histograms(df, output_dir):
    sns.set_style("whitegrid")

    grade_order = sorted(df["Grade"].dropna().unique()) 
    df["Grade"] = pd.Categorical(df["Grade"], categories=grade_order, ordered=True)

    g = sns.displot(
        data=df,
        x="Final_Score",
        hue="Gender",
        col="Grade",
        col_wrap=2,             
        stat="percent",
        bins=20,
        multiple="stack",
        palette="mako",
        alpha=0.6,
        height=4,
        aspect=1.2
    )

    g.set_axis_labels("Final Score", "Percentage of Students")
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle("Final Score Distribution by Grade and Gender", fontsize=16)
    g.savefig(os.path.join(output_dir, "hist2.png"))
    plt.close()

    sleep_hours_rounded = df["Sleep_Hours_per_Night"].round()

    counts = df.groupby([sleep_hours_rounded, df["Department"]]).size().unstack(fill_value=0)
    percent = counts.div(counts.sum(axis=0), axis=1) * 100

    colors = sns.color_palette("crest", n_colors=percent.shape[1])

    percent.plot(kind="bar", figsize=(12, 6), color=colors)

    plt.title("Relative Sleep Hours Distribution by Department")
    plt.xlabel("Sleep Hours per Night")
    plt.ylabel("Percentage of Students")
    plt.legend(title="Department")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "hist3.png"))
    plt.close()



