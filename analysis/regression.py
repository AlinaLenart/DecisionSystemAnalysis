import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_regressions(df, output_dir):

    target_col = 'Total_Score'

    id_fields = ['Student_ID', 'First_Name', "Last_Name", "Email"]

    trimmed_df = df.drop(columns=id_fields)

    # Categorical Columns
    cat_cols = trimmed_df.select_dtypes(include='object').columns

    # Categorical Columns
    num_cols = trimmed_df.select_dtypes(exclude="object").drop(columns=['Age', target_col]).columns

    # Sample to data due to because of much points
    sample_df = df.sample(n=int(len(df)*0.3), random_state=50)

    fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(16, 6))
    i=0


    for row in range(2):
        for col in range(5):
            feature = num_cols[i]
            sns.regplot(data=sample_df, x=feature, y=target_col, line_kws={'color': "red"}, ax=ax[row, col])
            i+=1
            
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "regression.png"))
    plt.close()

