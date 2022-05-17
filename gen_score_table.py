import pandas as pd
import numpy as np

DATASET = "mobility" # browsing
FILE_IN = f"{DATASET}_evaluation.csv"

df = pd.read_csv("data/" + FILE_IN, delimiter=",")
subset_df = df[97:121] # -2, -1 # CHANGE HERE
sample_size = subset_df["client_sample_size"].values[0]

for index, row in subset_df.iterrows():

    top_1 = row["top_1"]
    top_1 = f'{top_1:.3f}'
    top_1_std = row["top_1_std"]
    top_10 = row["top_10"]
    top_10 = f'{top_10:.3f}'
    top_10_std = row["top_10_std"]
    top_10_percent = row["top_10_percent"]
    top_10_percent = f'{top_10_percent:.3f}'
    top_10_percent_std = row["top_10_percent_std"]

    error = 1.96 * (top_1_std / np.sqrt(sample_size))
    top_1_error = f'{error:.3f}'

    error = 1.96 * (top_10_std / np.sqrt(sample_size))
    top_10_error = f'{error:.3f}'

    error = 1.96 * (top_10_percent_std / np.sqrt(sample_size))
    top_10_percent_error = f'{error:.3f}'

    output_str = ""
    output_str = output_str + row["strategy"] + "&"
    output_str = output_str + row["scope"] + "&"   
    output_str = output_str + row["scoring_matrix"] + "&"

    output_str = output_str + top_1 + " $\pm$ " + top_1_error + " & "
    output_str = output_str + top_10 + " $\pm$ " + top_10_error + " & "
    output_str = output_str + top_10_percent + " $\pm$ " + top_10_percent_error + " \\\\"
    print(output_str)
    print("\hline")


