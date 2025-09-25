# titanic_eda.py

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda(csv_in: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    plots_dir = os.path.join(out_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)

    print(f"\n=== EDA for {csv_in} ===")
    df = pd.read_csv(csv_in)
    print("Shape:", df.shape)

    # Save summaries
    with open(os.path.join(out_dir, "summary.txt"), "w") as f:
        f.write(f"INPUT: {csv_in}\n")
        f.write(f"SHAPE: {df.shape}\n\n")
        f.write("DTYPES:\n")
        f.write(str(df.dtypes) + "\n\n")
        f.write("MISSING VALUES:\n")
        f.write(str(df.isna().sum().sort_values(ascending=False)) + "\n\n")
        f.write("NUMERIC SUMMARY:\n")
        f.write(str(df.describe()) + "\n\n")
        try:
            f.write("CATEGORICAL SUMMARY:\n")
            f.write(str(df.describe(include='object')) + "\n\n")
        except Exception:
            pass

    # Choose numeric columns of interest
    num_cols = [c for c in ["Age", "Fare", "SibSp", "Parch"] if c in df.columns]
    if not num_cols:
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()[:4]

    # Histograms + Boxplots
    for col in num_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"{col} distribution")
        plt.tight_layout(); plt.savefig(os.path.join(plots_dir, f"{col}_hist.png")); plt.close()

        plt.figure(figsize=(6,4))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"{col} boxplot")
        plt.tight_layout(); plt.savefig(os.path.join(plots_dir, f"{col}_box.png")); plt.close()

    # Correlation heatmap
    num_df = df.select_dtypes(include=[np.number]).copy()
    # drop near-constant columns
    drop_cols = [c for c in num_df.columns if num_df[c].nunique(dropna=True) <= 1]
    num_df = num_df.drop(columns=drop_cols)
    if num_df.shape[1] >= 2:
        corr = num_df.corr(numeric_only=True)
        plt.figure(figsize=(8,6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation heatmap")
        plt.tight_layout(); plt.savefig(os.path.join(plots_dir, "correlation_heatmap.png")); plt.close()

    print("Saved EDA to:", out_dir)

if __name__ == "__main__":
    # Inputs: adjust paths if repo layout differs
    cleaned = "outputs/titanic_cleaned.csv"
    post_outliers = "outputs/titanic_cleaned_post_outliers.csv"

    # Fallback to raw if cleaned versions missing
    inputs = []
    if os.path.exists(cleaned): inputs.append((cleaned, "outputs/eda_cleaned"))
    if os.path.exists(post_outliers): inputs.append((post_outliers, "outputs/eda_post_outliers"))
    if not inputs:
        inputs = [("Titanic-Dataset.csv", "outputs/eda_raw")]

    for csv_in, out_dir in inputs:
        run_eda(csv_in, out_dir)
