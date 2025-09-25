Input

	Preferred: outputs/titanic_cleaned_post_outliers.csv.
	Also supported: outputs/titanic_cleaned.csv or Titanic-Dataset.csv.
Key scripts:

	titanic_eda.py — EDA for a single dataset.
	titanic_eda_compare.py — Runs EDA on both cleaned and post‑outliers datasets and saves results side‑by‑side.
Outputs folders:

	outputs/eda_plots/ (single‑run)
	outputs/eda_cleaned/ and outputs/eda_post_outliers/ (comparison‑run)
	outputs/eda_summary.txt or outputs/*/summary.txt (text stats)
	
#How to run

Install packages:

	pip install pandas numpy seaborn matplotlib
Single dataset EDA:

	python titanic_eda.py
	Saves plots to outputs/eda_plots/ and a text summary to outputs/eda_summary.txt.
Compare cleaned vs post‑outliers:

	Ensure both CSVs exist in outputs/.
	python titanic_eda_compare.py
Saves:

	outputs/eda_cleaned/plots and outputs/eda_cleaned/summary.txt
	outputs/eda_post_outliers/plots and outputs/eda_post_outliers/summary.txt
	
What the code does
Summary statistics:

	Writes shape, dtypes, missing values, numeric describe(), and categorical describe().
Distributions:

	Histograms with KDE for Age, Fare, SibSp, Parch (or best numeric columns).
Outliers:

	Boxplots for the same numeric features to visualize spread and extremes.
Relationships:

	Correlation heatmap for numeric features.
	Sampled pairplot (in single‑run script) for quick relationship scanning.
	
Files produced
Plots (PNG):

	_hist.png — histogram + KDE.
	_box.png — boxplot for outliers.
	correlation_heatmap.png — annotated correlations.
	pairplot_sampled.png — optional pairwise view.
Text summary:

	outputs/eda_summary.txt (single‑run) or outputs/*/summary.txt (comparison‑run).
	
Key observations (example)
•	Age:

	Centered around young–middle adulthood; a few higher extremes.
•	Fare:

	Strong right skew; clear outliers in cleaned dataset; tighter spread post‑outliers.
•	SibSp/Parch:

	Most values near 0–1; many passengers traveled alone or with a small group.
•	Correlations:

	Fare relates to class‑linked variables; encoded Sex (from Task 1) often relates to Survived in modeling.
		
Include both datasets in EDA
•	Use titanic_eda_compare.py to run identical EDA on:

	outputs/titanic_cleaned.csv → outputs/eda_cleaned/
	outputs/titanic_cleaned_post_outliers.csv → outputs/eda_post_outliers/
Compare histograms, boxplots, and heatmaps across both folders and summarize differences.

Repo structure (suggested)
•	README.md

•	titanic_eda.py

•	titanic_eda_compare.py

•	outputs/

	titanic_cleaned.csv
	titanic_cleaned_post_outliers.csv
	eda_plots/ or
	eda_cleaned/plots + summary.txt
	eda_post_outliers/plots + summary.txt

Notes
	•	No randomness required for stats/plots; pairplot sampling uses a fixed seed for consistency.
