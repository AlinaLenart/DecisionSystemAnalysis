import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def save_heatmaps(df, output_dir):

    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr()
    plt.figure(figsize=(12, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".3f", linewidths=0.5)
    plt.title("The Correlation ")
    plt.savefig(os.path.join(output_dir, "heatmap1.png"))
    plt.close()

    score_dict = {
        "Participation_Score": 0.05,
        "Assignments_Avg": 0.05,
        "Quizzes_Avg": 0.1,
        "Projects_Score": 0.15,
        "Midterm_Score": 0.25,
        "Final_Score": 0.4
    }

    # Obliczenie tymczasowego Total_Score
    aggregate = np.zeros(len(df))
    for col, weight in score_dict.items():
        aggregate += df[col].values * weight

    # Tymczasowy DataFrame do korelacji
    aggregate_cols = list(score_dict.keys())
    temp_df = df[aggregate_cols].copy()
    temp_df["Calculated_Total_Score"] = aggregate

    # Korelacja z przeliczoną wartością
    corr = temp_df.corr().abs()

    # Wizualizacja
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, cmap='YlGnBu', annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Correlation with Recalculated Total Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "heatmap2.png"))
    plt.close()
