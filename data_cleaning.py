"""Data understanding and cleaning functions."""
import pandas as pd

NUMERIC_COLUMNS = [
    "Age", "Income", "Purchases", "PurchaseAmount", "LastPurchaseDays",
    "SupportCalls", "TenureMonths", "SatisfactionScore", "Churn"
]

def explore_data(df):
    print("\n--- HEAD ---")
    print(df.head())
    print("\n--- INFO ---")
    df.info()
    print("\n--- DESCRIPTIVE STATISTICS ---")
    print(df.describe(include="all").T)
    print("\n--- MISSING VALUES ---")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

def clean_data(df):
    data = df.copy()
    data = data.drop_duplicates()

    # Normalize text values
    for col in ["Gender", "Region", "ProductCategory"]:
        data[col] = data[col].astype("string").str.strip().str.title()
        data[col] = data[col].replace({"<NA>": pd.NA, "Nan": pd.NA, "None": pd.NA})

    # Convert numeric columns safely
    for col in NUMERIC_COLUMNS:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["SignupDate"] = pd.to_datetime(data["SignupDate"], errors="coerce")

    # Impute numeric missing values with median
    for col in NUMERIC_COLUMNS:
        if data[col].isna().any():
            if col == "Churn":
                data[col] = data[col].fillna(data[col].mode().iloc[0])
            else:
                data[col] = data[col].fillna(data[col].median())

    # Impute categorical missing values with mode
    for col in ["Gender", "Region", "ProductCategory"]:
        if data[col].isna().any():
            data[col] = data[col].fillna(data[col].mode().iloc[0])

    # Remove invalid target rows if any and enforce integer target
    data = data[data["Churn"].isin([0, 1])].copy()
    data["Churn"] = data["Churn"].astype(int)
    data["CustomerID"] = pd.to_numeric(data["CustomerID"], errors="coerce")
    data = data.dropna(subset=["CustomerID"])
    data["CustomerID"] = data["CustomerID"].astype(int)

    # Remove irrelevant identifiers only from feature set later, not from master data
    return data.reset_index(drop=True)

if __name__ == "__main__":
    from data_acquisition import acquire_all_data
    raw = acquire_all_data()
    explore_data(raw)
    cleaned = clean_data(raw)
    cleaned.to_csv("outputs/cleaned_customers.csv", index=False)
    print("Cleaned shape:", cleaned.shape)
