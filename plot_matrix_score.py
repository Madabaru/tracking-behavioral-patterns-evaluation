# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BAR_WIDTH = 0.2
plt.style.use('ggplot')
plt.figure(figsize=(15, 8))

DATASET = "browsing"  # browsing
FILE_IN = f"data/{DATASET}_evaluation.csv"

# CHANGE AS REQUIRED:
APPROACH = "Sequence alignment-based Approach"
TITLE = f"{APPROACH}: Scoring Matrix vs. Scope vs. Strategy"

df = pd.read_csv(FILE_IN, delimiter=",")
subset_df = df[104:128]  # -2, -1
scoring_matrx_values = subset_df["scoring_matrix"].values
scope_values = subset_df["scope"].values
strategy_values = subset_df["strategy"].values
x = [(scoring_matrx_values[i], scope_values[i], strategy_values[i])
     for i in range(len(strategy_values))]

sample_size = subset_df["client_sample_size"].values[0]

top_1 = subset_df["top_1"].values
top_10 = subset_df["top_10"].values
top_10_percent = subset_df["top_10_percent"].values

top_1_std = subset_df["top_1_std"].values
top_10_std = subset_df["top_10_std"].values
top_10_percent_std = subset_df["top_10_percent_std"].values

ci_top_1 = 1.96 * (top_1_std / np.sqrt(sample_size))
ci_top_10 = 1.96 * (top_10_std / np.sqrt(sample_size))
ci_top_10_percent = 1.96 * (top_10_percent_std / np.sqrt(sample_size))

# The x position of bars
top_1_bar = np.arange(len(x))
top_10_bar = [i + BAR_WIDTH for i in top_1_bar]
top_10_percent_bar = [i + 2 * BAR_WIDTH for i in top_1_bar]

plt.bar(top_1_bar, top_1, width=BAR_WIDTH, color="#007FFF",
        yerr=ci_top_1, capsize=3, label="Top 1")
plt.bar(top_10_bar, top_10, width=BAR_WIDTH, color="#3333FF",
        yerr=ci_top_10, capsize=3, label="Top 10")
plt.bar(top_10_percent_bar, top_10_percent, width=BAR_WIDTH,
        color="#999999", yerr=ci_top_10_percent, capsize=3, label="Top 10%")

plt.xticks([r + BAR_WIDTH for r in range(len(top_1_bar))], x, rotation=90)
plt.legend(loc='upper right')
plt.title(TITLE)
plt.ylabel('Probability')
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.tight_layout()
plt.savefig(f"images/{DATASET}/{TITLE}.pdf", format="pdf")
