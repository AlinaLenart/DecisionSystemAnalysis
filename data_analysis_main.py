from analysis.loader import load_data
from analysis.stats import calculate_statistics
from analysis.boxplot import save_boxplots
from analysis.violinplot import save_violinplots
from analysis.errorbar import save_errorbars
from analysis.histogram import save_histograms
from analysis.heatmap import save_heatmaps
from analysis.regression import save_regressions


if __name__ == "__main__":
    df = load_data("data/Students_Grading_Dataset.csv")
    
    stats = calculate_statistics(df)

    save_boxplots(df, "outputs/plots/")
    save_violinplots(df, "outputs/plots/")
    save_errorbars(df, "outputs/plots/")
    save_histograms(df, "outputs/plots/")
    save_heatmaps(df, "outputs/plots/")
    save_regressions(df,"outputs/plots/")
    
