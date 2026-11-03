# 🚀 Customer Churn Prediction
## 📊 Data Preprocessing, Feature Engineering & Exploratory Data Analysis

**👨‍💻 Project Author:** Rami Ashutosh  
**📌 Project Type:** Data Analytics / Machine Learning Preparation  
**🛠️ Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, SQLite and REST API  
**📁 Dataset:** Synthetic customer purchase-behaviour data

---

## 🎯 1. Project Overview

This project demonstrates an end-to-end data preparation workflow for a consumer-insights company. It collects customer purchase-behaviour data from multiple sources, combines it, checks data quality, cleans inconsistent values, creates useful features, performs Exploratory Data Analysis (EDA), and generates an automated data profiling report.

> ⚠️ **Important:** All included customer records are synthetic and intended for educational practice only.

## 🏢 2. Business Problem

The company wants to understand customer behaviour and prepare data for a future **Customer Churn Prediction** model.

- 🔴 `Churn = 1`: Customer churned.
- 🟢 `Churn = 0`: Customer did not churn.

This project prepares the data; it does not train or validate a production-ready prediction model.

## 🎯 3. Project Objectives

- 📥 Import data from CSV, JSON, SQL and REST API sources.
- 🔗 Combine records from multiple sources.
- 🔍 Explore data using Pandas.
- 🧹 Identify missing values and duplicate records.
- 🔄 Correct data types and inconsistent category values.
- 🩹 Handle missing values using imputation.
- 📊 Perform univariate, bivariate and multivariate analysis.
- 📈 Create visualizations and correlation analysis.
- 📝 Generate an automated data profiling report.
- ⚙️ Perform feature engineering for future machine learning.

## 🛠️ 4. Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🐼 Pandas | Data loading, manipulation and cleaning |
| 🔢 NumPy | Numerical operations and arrays/tensors |
| 📊 Matplotlib | Data visualization |
| 🎨 Seaborn | Statistical charts and EDA |
| 🗄️ SQLite | SQL database source |
| 🌐 Requests | REST API data collection |
| ⚡ Flask | Optional local demo API server |

## 📂 5. Project Folder Structure

```text
Customer_Churn_Data_Preprocessing_Project/
│
├── 📁 data/
│   ├── customers_csv.csv
│   ├── customers_json.json
│   ├── customers.db
│   ├── api_customers.json
│   └── README_DATA.txt
│
├── 📁 outputs/
│   ├── data_profiling_report.html
│   └── 📁 eda_plots/
│
├── data_acquisition.py
├── data_cleaning.py
├── feature_engineering.py
├── eda.py
├── data_profiling.py
├── api_server.py
├── main.py
├── data_dictionary.csv
├── requirements.txt
└── README.md
```

## 📊 6. Dataset Information

| Data Source | File / Location | Approx. Records |
|---|---|---:|
| 📄 CSV | `data/customers_csv.csv` | 400 |
| 🧾 JSON | `data/customers_json.json` | 250 |
| 🗄️ SQLite | `data/customers.db`, table `customers` | 200 |
| 🌐 API sample | `data/api_customers.json` | 150 |
| **📌 Total source records** | | **1,000** |

The combined data also includes intentionally introduced duplicate rows and data-quality issues for cleaning practice.

### 🧾 Main Dataset Columns

| Column | Description |
|---|---|
| 🆔 CustomerID | Customer identifier |
| 🎂 Age | Customer age |
| 👤 Gender | Customer gender category |
| 💰 Income | Estimated income |
| 🛒 Purchases | Number of purchases |
| 💵 PurchaseAmount | Purchase amount measure |
| 🕒 LastPurchaseDays | Days since last purchase |
| ☎️ SupportCalls | Number of support calls |
| 📅 TenureMonths | Customer tenure in months |
| ⭐ SatisfactionScore | Satisfaction rating from 1 to 5 |
| 🌍 Region | Customer region |
| 🏷️ ProductCategory | Product category |
| 🗓️ SignupDate | Customer signup date |
| 🎯 Churn | Target variable (0 or 1) |

See `data_dictionary.csv` for the complete column reference.

## ✅ 7. Tasks Covered

### 📘 Part A — Fundamentals
- What is Data Analysis?
- Data Science project workflow.
- Framing a customer churn machine-learning problem.
- Tensor fundamentals using NumPy arrays.

### 📥 Part B — Data Acquisition
- Load CSV using `pd.read_csv()`.
- Parse JSON using `pd.read_json()`.
- Read SQL records using SQLite and Pandas.
- Fetch API data using Requests.
- Combine datasets using `pd.concat()`.

### 🧹 Part C — Data Understanding & Cleaning
- Explore data using `head()`, `info()` and `describe()`.
- Check missing values using `isna()`.
- Detect duplicates using `duplicated()`.
- Convert columns to suitable data types.
- Normalize inconsistent category values.
- Impute missing numerical and categorical values.
- Remove duplicate records.

### 📊 Part D — Exploratory Data Analysis (EDA)

**📌 Univariate Analysis**
- Age distribution.
- Income distribution.
- Purchases distribution.

**🔗 Bivariate Analysis**
- Gender vs Purchases.
- Income vs Churn.

**🌐 Multivariate Analysis**
- Correlation heatmap.
- Pair plot of numerical features.

### 📝 Part E — Data Profiling

The automated report summarizes:
- 🔎 Missing values and missing percentages.
- 📊 Descriptive statistics.
- 🔗 Numerical correlations.
- ♻️ Duplicate records.
- ⚠️ Potential data-quality warnings.

## ⚙️ 8. Feature Engineering

| Feature | Description |
|---|---|
| 🎂 CustomerAgeGroup | Groups customers by age range |
| 🛒 PurchaseFrequency | Purchases divided by customer tenure |
| 💵 AveragePurchaseValue | Purchase amount divided by purchases |
| 💤 IsInactive90Days | Indicates inactivity for at least 90 days |
| ☎️ HighSupportNeed | Indicates four or more support calls |

Categorical variables are one-hot encoded in the ML-ready dataset.

## 💻 9. Installation

1. 📥 Download and extract the project ZIP.
2. 📂 Open the project folder in VS Code or Command Prompt.
3. Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

4. 📦 Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ 10. How to Run the Project

Run the complete workflow from the project folder:

```bash
python main.py
```

The script:
1. 📥 Loads CSV, JSON, SQL and API sample data.
2. 🔗 Combines all source datasets.
3. 🔍 Performs initial exploration.
4. 📝 Generates the profiling report.
5. 🧹 Cleans the data.
6. ⚙️ Creates engineered features.
7. 💾 Exports the ML-ready dataset.
8. 📈 Generates EDA charts.

### 🌐 Optional: Run the Local REST API

In a first terminal:

```bash
python api_server.py
```

Keep it running. Open a second terminal in the project folder and run:

```bash
python main.py
```

The local endpoint is:

```text
http://127.0.0.1:5000/api/customers
```

If the API server is unavailable, the project automatically uses the bundled `api_customers.json` file.

## 📦 11. Expected Output Files

After running `main.py`, check the `outputs/` folder:

| Output File | Description |
|---|---|
| `raw_combined_customers.csv` | Combined data before cleaning |
| `data_profiling_report.html` | Automated data-quality report |
| `cleaned_customers.csv` | Cleaned customer dataset |
| `feature_engineered_customers.csv` | Dataset with engineered features |
| `ml_ready_dataset.csv` | Encoded dataset prepared for future ML |
| `eda_plots/` | Saved EDA visualizations |

🌐 Open `data_profiling_report.html` in a web browser.

## 🎓 12. Learning Outcomes

Through this project, I practiced:

- 📂 Working with multiple data formats and sources.
- 🔗 Loading and merging datasets.
- 🐼 Using Pandas and NumPy.
- 🔢 Understanding tensors and array dimensions.
- 🧹 Identifying and fixing data-quality issues.
- 📊 Performing exploratory data analysis.
- 📈 Creating visualizations.
- 📝 Generating automated profiling reports.
- ⚙️ Engineering features for machine-learning preparation.
- 🧩 Organizing Python code into reusable modules.

## 🚀 13. Limitations & Future Improvements

- ⚠️ The dataset is synthetic and should not be used for real business decisions.
- ⚠️ Churn labels are illustrative, not verified business outcomes.
- 🤖 A future version can train Logistic Regression, Decision Tree and Random Forest models.
- 📏 Future work can include train/test splitting, class-imbalance analysis, model evaluation and explainability.
- 🔐 A production project should use validated real-world data and secure API credentials.

## 🏁 14. Conclusion

This project demonstrates a structured workflow for acquiring, understanding, cleaning, profiling and transforming customer data. The final prepared dataset provides a foundation for a future Customer Churn Prediction model.

---

### 👨‍💻 Created By: Rami Ashutos
**🚀 Project:** Customer Churn Prediction — Data Preprocessing & Feature Engineering

⭐ *Thank you for visiting this project!*
