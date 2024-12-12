import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math
from scipy.stats import ks_2samp
import itertools


# Load the data
trades = {offset: pd.read_csv(f"processedtrades/trades_{offset}.csv") for offset in ["-2", "-1", "0", "+1", "+2"]}
 
# Identify all unique "condition" columns values
conditions = {offset: sorted([int(x) for x in trades[offset]["condition"].unique() if not math.isnan(x)]) for offset in trades}

# Combine and find unique values in conditions values
all_conditions = set()
for offset in conditions:
    all_conditions.update(conditions[offset])

# Find intersection of all conditions
intersecting_conditions = set(conditions["-2"]).intersection(conditions["-1"]).intersection(conditions["0"]).intersection(conditions["+1"]).intersection(conditions["+2"])

# Non intersection conditions
non_intersecting_conditions = {offset: sorted(list(set(conditions[offset]) - intersecting_conditions)) for offset in conditions}
print(non_intersecting_conditions)

# categories = sorted(list(intersecting_conditions))
# categories.append("other")

# # Create a dictionary of dataframes for each condition
# distribution = {"-2": {"other":0}, "-1": {"other":0}, "0": {"other":0}, "+1": {"other":0}, "+2": {"other":0}}
# for offset in distribution:
#     for condition in categories:
#         if condition == "other":
#             for cd in non_intersecting_conditions[offset]:
#                 distribution[offset]["other"] += trades[offset][trades[offset]["condition"] == cd].shape[0]
#         else:
#             distribution[offset][condition] = trades[offset][trades[offset]["condition"] == condition].shape[0]

# distribution_df = pd.DataFrame(distribution)
# # Plot the columns as histograms
# distribution_df.plot(kind='bar')
# plt.show()

# # log normalize all values in the dataframe
# distribution_df_logged = distribution_df.apply(lambda x: np.log(x+1))
# distribution_df_logged.plot(kind='bar')
# plt.title("Log normalized quantity of trades for each condition")
# plt.xlabel("Condition Number")
# plt.ylabel("Log Quantity")
# plt.savefig("plots/distribution_logged.png")
# plt.show()

# # Pairwise KS test
# columns = distribution_df_logged.columns
# results = {}

# for col1, col2 in itertools.combinations(columns, 2):
#     stat, p_value = ks_2samp(distribution_df_logged[col1], distribution_df_logged[col2])
#     results[(col1, col2)] = p_value

# # Print results
# for (col1, col2), p_value in results.items():
#     print(f"KS test between {col1} and {col2}: p-value = {p_value}")