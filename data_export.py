import pandas as pd
import numpy as np

path_import = "Students_Grading_Dataset.csv"

df = pd.read_csv(path_import)  

excluded_cols = {"Student_ID", "First_Name", "Last_Name", "Email"}

# numeric_cols = [col for col in df.select_dtypes(include=[np.number]).columns if col not in excluded_cols]
# categorical_cols = [col for col in df.select_dtypes(exclude=[np.number]).columns if col not in excluded_cols]


numeric_cols = df.select_dtypes(include=[np.number]).columns.difference(excluded_cols).tolist()
categorical_cols = df.select_dtypes(exclude=[np.number]).columns.difference(excluded_cols).tolist()


numeric_stats = []
categorical_stats = []

for col in numeric_cols:
    col_data = df[col]
    stats = {
        "Feature": col,
        "Average": col_data.mean(),
        "Median": col_data.median(),
        "Min": col_data.min(),
        "Max": col_data.max(),
        "Std": col_data.std(),
        "5th percentile": col_data.quantile(0.05),
        "95th percentile": col_data.quantile(0.95),
        "Missing": col_data.isna().sum()
    }
    numeric_stats.append(stats)

for col in categorical_cols:
    col_data = df[col]
    value_counts = col_data.value_counts(dropna=False, normalize=True)
    class_props = "; ".join([f"{k}: {round(v*100, 2)}%" for k, v in value_counts.items()])
    stats = {
        "Feature": col,
        "Number of unique classes": col_data.nunique(dropna=True),
        "Missing": col_data.isna().sum(),
        "Class proportion": class_props
    }
    categorical_stats.append(stats)


stats_num_df = pd.DataFrame(numeric_stats)
stats_cat_df = pd.DataFrame(categorical_stats)


stats_num_df.to_csv("numeric_stats.csv", index=False)
stats_cat_df.to_csv("categorical_stats.csv", index=False)