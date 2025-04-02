import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def save_histograms(df, output_dir):

    numeric_cols = df.select_dtypes(exclude="object").columns

    nrows = 4
    ncols = 3
    i = 0
    # use the default style
    plt.style.use("default")

    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 12))

    for row in range(nrows):
        for col in range(ncols):
            dist = df[numeric_cols[i]]
            sns.histplot(dist, kde=True, alpha=.4, ax=ax[row, col])
            if pd.api.types.is_numeric_dtype(dist):
                ax[row, col].axvline(dist.mean(), color="r", linestyle='dashed', label=f"Mean: {int(dist.mean())}")
                ax[row, col].axvline(dist.median(), color="black", linestyle='-.', label=f"Median: {int(dist.median())}")
                ax[row, col].legend()
            i+=1

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "hist1.png"))
    plt.close()
    

    plt.figure(figsize=(10, 6))
    sns.catplot(x='Department', hue='Gender', col='Grade', data=df, kind='count', height=5, aspect=1.5, alpha=0.45)
    plt.title('Department -wise Gender Distribution by Grade')
    plt.savefig(os.path.join(output_dir, "hist2.png"))
    plt.close()