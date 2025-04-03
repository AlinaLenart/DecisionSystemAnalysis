import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def save_errorbars(df, output_dir):
    # Kopiujemy kolumny do tymczasowego DataFrame
    temp_df = df[["Parent_Education_Level", "Total_Score"]].copy()

    # Konwersja na kategorię uporządkowaną tylko w temp_df
    edu_order = ["High School", "Bachelor's", "Master's", "PhD"]
    temp_df["Parent_Education_Level"] = pd.Categorical(
        temp_df["Parent_Education_Level"],
        categories=edu_order,
        ordered=True
    )

    # Grupowanie
    group_col = "Parent_Education_Level"
    value_col = "Total_Score"

    grouped = temp_df.groupby(group_col, observed=True)[value_col].agg(['mean', 'count', 'std']).reset_index()
    grouped['se'] = grouped['std'] / np.sqrt(grouped['count'])

    # Wykres
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, height_ratios=[1, 1])

    # Górny panel: średnia z SE
    ax1.errorbar(
        x=grouped[group_col],
        y=grouped['mean'],
        yerr=grouped['se'],
        fmt='-o',
        capsize=5,
        color='tab:green',
        linewidth=2
    )
    ax1.set_title("Average Total Score by Parent Education Level")
    ax1.set_ylabel("Total Score")

    # Dolny panel: rozrzut punktów
    sns.stripplot(
        data=temp_df,
        x=group_col,
        y=value_col,
        ax=ax2,
        jitter=0.25,
        alpha=0.6,
        color='tab:green',
        size=4
    )
    ax2.set_title("Distribution of Total Score by Parent Education Level")
    ax2.set_xlabel("Parent Education Level")
    ax2.set_ylabel("Total Score")

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "errorbar.png"))
    plt.close()
