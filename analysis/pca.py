import seaborn as sns
import os
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def save_pca(df, output_dir):

    excluded_cols = {"Student_ID", "First_Name", "Last_Name", "Email"}
    numeric_cols = df.select_dtypes(include=["number"]).columns.difference(excluded_cols).tolist()

    df_clean = df[numeric_cols].dropna()
    attendance_vals = df_clean["Attendance (%)"].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_clean[numeric_cols])
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    cmap = plt.cm.viridis
    norm = Normalize(vmin=attendance_vals.min(), vmax=attendance_vals.max())

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("whitegrid")

    scatter = ax.scatter(
        X_pca[:, 0], X_pca[:, 1],
        c=attendance_vals,
        cmap=cmap,
        norm=norm,
        s=70,
        alpha=0.85
    )

    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("Attendance (%)")

    ax.set_title("PCA – Colored by Attendance (%)", fontsize=14)
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "PCA.png"), dpi=300)
    plt.close()



