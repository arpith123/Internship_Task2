Task 2 — Exploratory Data Analysis (Titanic)
Objective: Perform EDA on the Titanic dataset to understand distributions, outliers, and feature relationships, then summarize insights with visuals and stats.
Project setup
	•	Input
	•	Preferred: outputs/titanic_cleaned_post_outliers.csv (from Task 1).
	•	Also supported: outputs/titanic_cleaned.csv or Titanic-Dataset.csv.
	•	Key scripts:
	•	titanic_eda.py — EDA for a single dataset.
	•	titanic_eda_compare.py — Runs EDA on both cleaned and post‑outliers datasets and saves results side-by-side.
	•	Outputs:
	•	outputs/eda_plots/ (single-run) or
	•	outputs/eda_cleaned/plots and outputs/eda_post_outliers/plots (comparison-run)
	•	outputs/eda_summary.txt or outputs/*/summary.txt (text stats)
How to run
	•	Install packages:
	•	pip install pandas numpy seaborn matplotlib
	•	Single dataset EDA:
	•	python titanic_eda.py
	•	Saves plots to outputs/eda_plots/ and a text summary to outputs/eda_summary.txt.
	•	Compare cleaned vs post‑outliers:
	•	Ensure both CSVs exist in outputs/.
	•	python titanic_eda_compare.py
	•	Saves:
	•	outputs/eda_cleaned/plots and outputs/eda_cleaned/summary.txt
	•	outputs/eda_post_outliers/plots and outputs/eda_post_outliers/summary.txt
What the code does
	•	Summary statistics:
	•	Prints and writes shape, dtypes, missing values, numeric describe(), and categorical describe().
	•	Distributions:
	•	Histograms with KDE for Age, Fare, SibSp, Parch (or best-available numeric columns).
	•	Outliers:
	•	Boxplots for the same numeric features to visualize spread and extremes.
	•	Relationships:
	•	Correlation heatmap for numeric features.
	•	Sampled pairplot (when using the single-run script) for quick relationship scanning.
Files produced
	•	Plots (PNG):
	•	_hist.png — histogram + KDE for each numeric feature.
	•	_box.png — boxplot for outlier visualization.
	•	correlation_heatmap.png — annotated correlations.
	•	pairplot_sampled.png — optional overview of numeric relationships.
	•	Text summary:
	•	eda_summary.txt (single-run) or summary.txt inside each per-dataset folder.
Key observations (example notes to adapt)
	•	Age:
	•	Centered around young to middle adulthood with moderate spread.
	•	Boxplot shows a few higher-age extremes; post‑outliers version caps extremes by prior preprocessing choices.
	•	Fare:
	•	Strong right skew with long tail.
	•	Boxplots show clear outliers in the cleaned dataset; post‑outliers distribution is tighter with fewer extreme values.
	•	SibSp and Parch:
	•	Most values are 0–1, indicating many passengers traveled alone or with a small group.
	•	Correlations:
	•	Fare tends to correlate with class-related variables when present.
	•	If using encoded datasets (from Task 1), note how these relate to Survived in downstream modeling plans.
	•	Pairwise patterns:
	•	Fare vs Age often shows clustering due to class and ticket price differences.
	•	Most other numeric pairs overlap, suggesting engineered features or categorical encodings matter.
How to include both datasets in EDA
	•	Use titanic_eda_compare.py to run the identical EDA routine on:
	•	outputs/titanic_cleaned.csv → outputs/eda_cleaned/
	•	outputs/titanic_cleaned_post_outliers.csv → outputs/eda_post_outliers/
	•	Compare histograms, boxplots, and heatmaps across the two folders; in README, add a brief “Outlier sensitivity” section summarizing differences in spread and visible extremes, plus any implications for modeling.
Interview-style answers
	•	Purpose of EDA:
	•	Understand data quality, distributions, relationships, and anomalies before modeling.
	•	How boxplots help:
	•	Show median, quartiles, and potential outliers via whiskers, making spread and extremes immediately clear.
	•	What is correlation and why useful:
	•	Correlation measures linear relationships between numeric features, helping detect signals and flag multicollinearity risks.
	•	Detecting skewness:
	•	Compare mean vs median and inspect histogram/KDE; a long tail indicates skew.
	•	Multicollinearity:
	•	When features are highly correlated, coefficients in linear models become unstable; diagnose via correlation heatmap (and VIF if modeling).
	•	Tools used:
	•	Pandas (stats), Seaborn/Matplotlib (plots); optionally add Plotly for interactivity if needed.
	•	Example of EDA catching an issue:
	•	Fare’s heavy right skew and outliers guided robust imputation in Task 1 and motivated showing a post‑outliers variant for sensitive algorithms.
	•	Role of visualization in ML:
	•	Visuals surface data issues early, communicate insights quickly, and inform preprocessing and feature engineering choices.
Repo structure (suggested)
	•	README.md
	•	Titanic-Dataset.csv (or link in README)
	•	titanic_eda.py
	•	titanic_eda_compare.py
	•	outputs/
	•	titanic_cleaned.csv
	•	titanic_cleaned_post_outliers.csv
	•	eda_plots/ or
	•	eda_cleaned/plots + summary.txt
	•	eda_post_outliers/plots + summary.txt
Reproducibility notes
	•	No randomness is required for stats/plots; pairplot may sample up to 300 rows for speed but the seed is fixed for consistency.
	•	If running on the raw CSV, some plots may skip columns with too many missing values—prefer the cleaned outputs from Task 1 for the most consistent visuals.
Next steps (optional)
	•	Add a short modeling notebook comparing baseline models on cleaned vs post‑outliers data.
	•	Evaluate metrics (accuracy, F1) and show whether outlier handling changes outcomes for sensitive algorithms.
	•	Document findings briefly and link them back to EDA insights.
