# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DATASET = "siamese_network" # browsing
FILE_IN = f"data/{DATASET}_evaluation.csv"
APPROACH_NAME = "Siamese network" # Histogram # Sequence alignment

APPROACH = f"{APPROACH_NAME}-based Approach"
XTITLE = "Number of Observed Traces K" # Number of Linkage Attacks # Number of Observed Traces K
TITLE = f"{APPROACH}: {XTITLE}"
MULTIPE_SAMPLE_SIZES = False

df = pd.read_csv(FILE_IN, delimiter=",")
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)

subset_df = df[9:15] # -2, -1 # CHANGE HERE
x = subset_df["trace_sample_size"].values  # trace_sample_size # client_sample_size

if not MULTIPE_SAMPLE_SIZES:
    sample_size = subset_df["client_sample_size"].values[0]
else:
    sample_size = subset_df["client_sample_size"].values

top_1 = subset_df["top_1"].values
top_10 = subset_df["top_10"].values
top_10_percent = subset_df["top_10_percent"].values

top_1_std = subset_df["top_1_std"].values
top_10_std = subset_df["top_10_std"].values
top_10_percent_std = subset_df["top_10_percent_std"].values

if not MULTIPE_SAMPLE_SIZES:
    ci_top_1 = 1.96 * (top_1_std / np.sqrt(sample_size))
    ci_top_10 = 1.96 * (top_10_std / np.sqrt(sample_size))
    ci_top_10_percent = 1.96 * (top_10_percent_std / np.sqrt(sample_size))
else:
    ci_top_1 = 1.96 * np.divide(top_1_std, np.sqrt(sample_size))
    ci_top_10 = 1.96 * np.divide(top_10_std, np.sqrt(sample_size))
    ci_top_10_percent = 1.96 * np.divide(top_10_percent_std, np.sqrt(sample_size))

ax.plot(x, top_1, marker='o', label="Top 1", color="#3f51b5")
ax.fill_between(x, (top_1-ci_top_1), (top_1+ci_top_1), color="#c5cae9")

ax.plot(x, top_10, marker='o', label="Top 10", color="#f44336")
ax.fill_between(x, (top_10-ci_top_10), (top_10+ci_top_10), color="#ffcdd2")

ax.plot(x, top_10_percent, marker='o', label="Top 10%", color="#9e9e9e")
ax.fill_between(x, (top_10_percent-ci_top_10_percent), (top_10_percent+ci_top_10_percent), color="#eeeeee")

ax.legend(loc='lower right')
ax.set_title(TITLE)
plt.xlabel(XTITLE)
plt.ylabel('Probability')
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.xticks([0, 5, 10, 15, 20, 25])

# plt.show()
plt.savefig(f"images/{DATASET}/{TITLE}.pdf", format="pdf")