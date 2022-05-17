import pandas as pd
import numpy as np

DATASET = "browsing" # browsing
FILE_IN = f"{DATASET}_evaluation.csv"

df = pd.read_csv("data/" + FILE_IN, delimiter=",")
subset_df = df[180:195] # -2, -1 # CHANGE HERE
sample_size = subset_df["client_sample_size"].values[0]

field_map = {"Url": "", "Category": "", "Domain": "", "Age": "", "Gender": "", "Hour": "", "Day": ""}
# field_map = {"Speed": "", "Heading": "", "Street": "", "Postcode": "", "State": "", "Village": "", "Highway": "", "Hamlet": "", "Suburb": "", "LocationCode": "", "Hour": "", "Day": ""}

for index, row in subset_df.iterrows():
    fields = row["fields"]
    field_map_copy = field_map.copy()
    for field in field_map.keys():
        if field in fields:
            field_map_copy[field] = "x"
    
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

    for key, value in field_map_copy.items():
        output_str = output_str + value
        output_str = output_str + "&"

    output_str = output_str + top_1 + " $\pm$ " + top_1_error + " & "
    output_str = output_str + top_10 + " $\pm$ " + top_10_error + " & "
    output_str = output_str + top_10_percent + " $\pm$ " + top_10_percent_error + " \\\\"
    print(output_str)
    print("\hline")


