# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BAR_WIDTH = 0.2
plt.style.use('ggplot')

DATASET = "browsing"  # browsing
FILE_IN = f"data/{DATASET}_evaluation.csv"

# CHANGE AS REQUIRED:
APPROACH = "Sequence alignment-based Approach"  # Sequence alignment
TITLE = f"{APPROACH}: Typical vs. K Observed Traces"

plt.style.use('ggplot')
df = pd.read_csv(FILE_IN, delimiter=",")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True, figsize=(8, 5))
fig.suptitle(TITLE, fontsize=14)
ax1.patch.set_facecolor('#e0e0e0')
ax2.patch.set_facecolor('#e0e0e0')
ax3.patch.set_facecolor('#e0e0e0')
ax4.patch.set_facecolor('#e0e0e0')

subset_df = df[66:74]  # -2, -1
typical_values = subset_df["typical"].values  # CHANGE HERE

k_values = subset_df["trace_sample_size"].values
x = ["Typical", "Not Typical", "Typical", "Not Typical",
     "Typical", "Not Typical", "Typical", "Not Typical"]

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
top_1_bar = np.arange(2)
top_10_bar = [i + BAR_WIDTH for i in top_1_bar]
top_10_percent_bar = [i + 2 * BAR_WIDTH for i in top_1_bar]

ax1.bar(top_1_bar, top_1[0:2], width=BAR_WIDTH, color="#3f51b5",
        yerr=ci_top_1[0:2], capsize=3, label="Top 1")
ax1.bar(top_10_bar, top_10[0:2], width=BAR_WIDTH, color="#f44336",
        yerr=ci_top_10[0:2], capsize=3, label="Top 10")
ax1.bar(top_10_percent_bar, top_10_percent[0:2], width=BAR_WIDTH,
        color="#9e9e9e", yerr=ci_top_10_percent[0:2], capsize=3, label="Top 10%")
ax1.set_xticks([0.2, 1.2])
ax1.set_xticklabels(["Typical", "Not Typical"])
ax1.set_title("K = 5", fontsize=12)
ax1.set(ylabel='Probability')

ax2.bar(top_1_bar, top_1[2:4], width=BAR_WIDTH, color="#3f51b5",
        yerr=ci_top_1[2:4], capsize=3, label="Top 1")
ax2.bar(top_10_bar, top_10[2:4], width=BAR_WIDTH, color="#f44336",
        yerr=ci_top_10[2:4], capsize=3, label="Top 10")
ax2.bar(top_10_percent_bar, top_10_percent[2:4], width=BAR_WIDTH,
        color="#9e9e9e", yerr=ci_top_10_percent[2:4], capsize=3, label="Top 10%")
ax2.set_xticks([0.2, 1.2])
ax2.set_xticklabels(["Typical", "Not Typical"])
ax2.set_title("K = 10", fontsize=12)

ax3.bar(top_1_bar, top_1[4:6], width=BAR_WIDTH, color="#3f51b5",
        yerr=ci_top_1[4:6], capsize=3, label="Top 1")
ax3.bar(top_10_bar, top_10[4:6], width=BAR_WIDTH, color="#f44336",
        yerr=ci_top_10[4:6], capsize=3, label="Top 10")
ax3.bar(top_10_percent_bar, top_10_percent[4:6], width=BAR_WIDTH,
        color="#9e9e9e", yerr=ci_top_10_percent[4:6], capsize=3, label="Top 10%")
ax3.set_xticks([0.2, 1.2])
ax3.set_xticklabels(["Typical", "Not Typical"])
ax3.set_title("K = 25", fontsize=12)
ax3.set(ylabel='Probability')

ax4.bar(top_1_bar, top_1[6:8], width=BAR_WIDTH, color="#3f51b5",
        yerr=ci_top_1[6:8], capsize=3, label="Top 1")
ax4.bar(top_10_bar, top_10[6:8], width=BAR_WIDTH, color="#f44336",
        yerr=ci_top_10[6:8], capsize=3, label="Top 10")
ax4.bar(top_10_percent_bar, top_10_percent[6:8], width=BAR_WIDTH,
        color="#9e9e9e", yerr=ci_top_10_percent[6:8], capsize=3, label="Top 10%")
ax4.set_xticks([0.2, 1.2])
ax4.set_xticklabels(["Typical", "Not Typical"])
ax4.set_title("K = 50", fontsize=12)

plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.tight_layout()

ax4.legend(loc='center')
plt.savefig(f"images/{DATASET}/{TITLE}.pdf", format="pdf")
