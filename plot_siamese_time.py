# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BAR_WIDTH = 0.2
plt.style.use('ggplot')

DATASET = "siamese_network"  # browsing
FILE_IN = f"data/{DATASET}_evaluation.csv"

# CHANGE AS REQUIRED:
APPROACH = "Siamese network-based Approach"  # Sequence alignment
TITLE = f"{APPROACH}: Day & Hour"

plt.style.use('ggplot')
df = pd.read_csv(FILE_IN, delimiter=",")
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
fig.suptitle(TITLE, fontsize=14)
ax1.patch.set_facecolor('#e0e0e0')
ax2.patch.set_facecolor('#e0e0e0')

subset_df = df[19:23]  # -2, -1

x = ["w/o Day & Time", "w/ Day & Time", "w/o Day & Time", "w/ Day & Time"]

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
ax1.set_xticklabels(["w/o Day & Hour", "w/ Day & Hour"])
ax1.set_title("Browsing Dataset", fontsize=12)
ax1.set(ylabel='Probability')

ax2.bar(top_1_bar, top_1[2:4], width=BAR_WIDTH, color="#3f51b5",
        yerr=ci_top_1[2:4], capsize=3, label="Top 1")
ax2.bar(top_10_bar, top_10[2:4], width=BAR_WIDTH, color="#f44336",
        yerr=ci_top_10[2:4], capsize=3, label="Top 10")
ax2.bar(top_10_percent_bar, top_10_percent[2:4], width=BAR_WIDTH,
        color="#9e9e9e", yerr=ci_top_10_percent[2:4], capsize=3, label="Top 10%")
ax2.set_xticks([0.2, 1.2])
ax2.set_xticklabels(["w/o Day & Hour", "w/ Day & Hour"])
ax2.set_title("Mobility Dataset", fontsize=12)

plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.tight_layout()

ax1.legend(loc='lower left')
plt.savefig(f"images/{DATASET}/{TITLE}.pdf", format="pdf")
