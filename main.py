"""End-to-end Customer Churn Data Preprocessing and Feature Engineering project."""
from pathlib import Path
from data_acquisition import acquire_all_data
from data_cleaning import explore_data, clean_data
from feature_engineering import engineer_features
from data_profiling import generate_profile_report
from eda import create_eda_plots

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "outputs"
OUTPUT.mkdir(exist_ok=True)

def main():
    print("=" * 65)
    print("CUSTOMER CHURN - DATA PREPROCESSING & FEATURE ENGINEERING")
    print("=" * 65)

    raw = acquire_all_data()
    raw.to_csv(OUTPUT / "raw_combined_customers.csv", index=False)

    print("\nSTEP 1: INITIAL DATA EXPLORATION")
    explore_data(raw)

    print("\nSTEP 2: DATA PROFILING REPORT")
    generate_profile_report(raw, OUTPUT / "data_profiling_report.html")

    print("\nSTEP 3: DATA CLEANING")
    cleaned = clean_data(raw)
    cleaned.to_csv(OUTPUT / "cleaned_customers.csv", index=False)
    print("Cleaned dataset shape:", cleaned.shape)
    print("Remaining missing values:", int(cleaned.isna().sum().sum()))

    print("\nSTEP 4: FEATURE ENGINEERING")
    engineered, ml_data = engineer_features(cleaned)
    engineered.to_csv(OUTPUT / "feature_engineered_customers.csv", index=False)
    ml_data.to_csv(OUTPUT / "ml_ready_dataset.csv", index=False)
    print("ML-ready dataset shape:", ml_data.shape)

    print("\nSTEP 5: EXPLORATORY DATA ANALYSIS")
    create_eda_plots(cleaned, OUTPUT / "eda_plots")
    print("EDA charts saved in outputs/eda_plots/")

    print("\nPROJECT COMPLETED. Check the outputs folder.")

if __name__ == "__main__":
    main()
