"""Create machine-learning-ready features without using the target as an input."""
import pandas as pd

def engineer_features(df):
    data = df.copy()
    data["CustomerAgeGroup"] = pd.cut(
        data["Age"], bins=[17, 25, 35, 45, 55, 70],
        labels=["18-25", "26-35", "36-45", "46-55", "56-70"]
    )
    data["PurchaseFrequency"] = data["Purchases"] / data["TenureMonths"].clip(lower=1)
    data["AveragePurchaseValue"] = (
        data["PurchaseAmount"] / data["Purchases"].replace(0, 1)
    )
    data["IsInactive90Days"] = (data["LastPurchaseDays"] >= 90).astype(int)
    data["HighSupportNeed"] = (data["SupportCalls"] >= 4).astype(int)

    # One-hot encode categorical features. Keep Churn as the target.
    feature_data = data.drop(columns=["CustomerID", "SignupDate"], errors="ignore")
    feature_data = pd.get_dummies(
        feature_data,
        columns=["Gender", "Region", "ProductCategory", "CustomerAgeGroup"],
        drop_first=True,
        dtype=int
    )
    return data, feature_data

if __name__ == "__main__":
    print("Import engineer_features() from this module in main.py.")
