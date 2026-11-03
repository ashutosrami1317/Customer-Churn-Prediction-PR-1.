"""Univariate, bivariate and multivariate exploratory analysis."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

def create_eda_plots(df, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="deep")

    # Univariate analysis
    for col in ["Age", "Income", "Purchases"]:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, color="steelblue")
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.savefig(output_dir / f"univariate_{col.lower()}.png", dpi=140)
        plt.close()

    # Bivariate analysis
    plt.figure(figsize=(7, 5))
    sns.barplot(data=df, x="Gender", y="Purchases", errorbar=None, color="steelblue")
    plt.title("Average Purchases by Gender")
    plt.tight_layout()
    plt.savefig(output_dir / "gender_vs_purchases.png", dpi=140)
    plt.close()

    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="Churn", y="Income", color="steelblue")
    plt.title("Income Distribution by Churn")
    plt.tight_layout()
    plt.savefig(output_dir / "income_vs_churn.png", dpi=140)
    plt.close()

    # Multivariate analysis
    numeric = df.select_dtypes(include="number")
    plt.figure(figsize=(10, 7))
    sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Numerical Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_dir / "correlation_heatmap.png", dpi=140)
    plt.close()

    pair_cols = ["Age", "Income", "Purchases", "PurchaseAmount", "Churn"]
    pair = sns.pairplot(df[pair_cols].sample(min(250, len(df)), random_state=42),
                        hue="Churn", diag_kind="hist", palette="deep")
    pair.fig.suptitle("Pair Plot of Customer Features", y=1.02)
    pair.savefig(output_dir / "pairplot.png", dpi=140)
    plt.close("all")
