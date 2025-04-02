import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_regressions(df, output_dir):
    target_col = 'Total_Score'

    num_cols = [
        'Attendance (%)', 'Midterm_Score', 'Final_Score',
        'Assignments_Avg', 'Quizzes_Avg', 'Participation_Score',
        'Projects_Score', 'Study_Hours_per_Week',
        'Stress_Level (1-10)', 'Sleep_Hours_per_Night'
    ]

    sample_df = df.sample(n=int(len(df)*0.3), random_state=50)

    fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(16, 6))
    i = 0

    for row in range(2):
        for col in range(5):
            feature = num_cols[i]
            sns.regplot(data=sample_df, x=feature, y=target_col, line_kws={'color': "red"}, ax=ax[row, col])
            ax[row, col].set_title(feature)
            i += 1

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "regression.png"))
    plt.close()

