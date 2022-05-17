# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BAR_WIDTH = 0.2

DATASET = "siamese_network" 
FILE_IN = f"{DATASET}_evaluation.csv"

APPROACH = "Siamese network-based Approach" # Siamese network-based Approach # Comparison
TITLE = f"{APPROACH}: Loss & Sampling Strategy" #  Loss vs. Sampling Strategy

plt.style.use('ggplot')
df = pd.read_csv("data/" + FILE_IN, delimiter=",")
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
ax.patch.set_facecolor('#e0e0e0')

subset_df = df[0:6] # -2, -1 # CHANGE HERE
x = ["(TL, Random)", "(TL, Semi-Hard)", "(TL, Hard)", "(CL, Random)", "(CL, Semi-Hard)", "(CL, Hard)"] # CHANGE HERE
# x = ["Histogram-based", "Sequence alignment-based", "Siamese network-based",]
sample_size = subset_df["client_sample_size"].values[0]
print(subset_df.shape)

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
 
plt.bar(top_1_bar, top_1, width=BAR_WIDTH, color="#3f51b5", yerr=ci_top_1, capsize=3, label="Top 1")
plt.bar(top_10_bar, top_10, width=BAR_WIDTH, color="#f44336", yerr=ci_top_10, capsize=3, label="Top 10")
plt.bar(top_10_percent_bar, top_10_percent, width=BAR_WIDTH, color="#9e9e9e", yerr=ci_top_10_percent, capsize=3, label="Top 10%")

plt.xticks([r + BAR_WIDTH for r in range(len(top_1_bar))], x, rotation=0)
plt.legend(loc='lower right')
plt.title(TITLE)
plt.ylabel('Probability')
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.tight_layout()
# plt.show()

plt.savefig(f"images/{DATASET}/{TITLE}.pdf", format="pdf")