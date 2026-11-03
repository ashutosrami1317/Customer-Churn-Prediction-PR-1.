"""Generate a profiling report with missing values, stats, correlations and warnings."""
from pathlib import Path
import pandas as pd

def generate_profile_report(df, output_file):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    missing = df.isna().sum().to_frame("Missing Values")
    missing["Missing %"] = (missing["Missing Values"] / len(df) * 100).round(2)
    stats = df.describe(include="all").T.fillna("")
    corr = df.select_dtypes(include="number").corr().round(3)

    warnings = []
    if df.duplicated().sum():
        warnings.append(f"{df.duplicated().sum()} duplicate rows detected.")
    for col in df.columns:
        pct = df[col].isna().mean() * 100
        if pct > 0:
            warnings.append(f"{col}: {pct:.2f}% missing values.")
    for col in df.select_dtypes(include="number").columns:
        if df[col].nunique(dropna=True) <= 1:
            warnings.append(f"{col}: constant or near-constant numeric column.")
    if "CustomerID" in df.columns and df["CustomerID"].duplicated().any():
        warnings.append("CustomerID is not unique.")

    warning_html = "".join(f"<li>{w}</li>" for w in warnings) or "<li>No major automated warnings detected.</li>"
    html = f"""
    <html><head><meta charset="utf-8"><title>Customer Data Profiling Report</title>
    <style>body{{font-family:Arial;margin:32px;color:#222}} table{{border-collapse:collapse;width:100%;margin-bottom:24px}}
    th,td{{border:1px solid #ddd;padding:7px;text-align:left;font-size:13px}} th{{background:#f2f2f2}}
    h1,h2{{color:#183153}} .note{{background:#eef5ff;padding:12px}}</style></head><body>
    <h1>Customer Data Profiling Report</h1>
    <p class="note">Generated automatically from the raw combined customer dataset.</p>
    <h2>Dataset overview</h2><p>Rows: {len(df)} | Columns: {len(df.columns)} | Duplicate rows: {df.duplicated().sum()}</p>
    <h2>Missing values</h2>{missing.to_html()}
    <h2>Descriptive statistics</h2>{stats.to_html()}
    <h2>Correlation matrix</h2>{corr.to_html()}
    <h2>Potential data quality warnings</h2><ul>{warning_html}</ul>
    </body></html>
    """
    output_file.write_text(html, encoding="utf-8")
    print(f"Profiling report saved: {output_file}")

if __name__ == "__main__":
    from data_acquisition import acquire_all_data
    raw = acquire_all_data()
    generate_profile_report(raw, "outputs/data_profiling_report.html")
