from analysis import (
    load_data,
    calculate_statistics,
    save_boxplots,
    save_violinplots,
    save_errorbars,
    save_histograms,
    save_heatmaps,
    save_regressions,
    save_pca
)

if __name__ == "__main__":

    df = load_data("data/Students_Grading_Dataset.csv")
    
    stats = calculate_statistics(df)
    path_for_plots = "outputs/plots/"

    save_boxplots(df, path_for_plots)
    save_violinplots(df, path_for_plots)
    save_errorbars(df, path_for_plots)
    save_histograms(df, path_for_plots)
    save_heatmaps(df, path_for_plots)
    save_regressions(df, path_for_plots)
    save_pca(df, path_for_plots)
    
