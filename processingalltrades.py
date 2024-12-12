import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# all_ids is all ids in databeforeafter that have _0.csv
all_ids = [file_name.split("_0.csv")[0] for file_name in os.listdir("datatrades") if "_0.csv" in file_name]
valid_ids_lower = [id for id in all_ids if all([os.path.exists(f"datatrades/{id}_{offset}.csv") for offset in ["-2", "-1"]])]
valid_ids_upper = [id for id in all_ids if all([os.path.exists(f"datatrades/{id}_{offset}.csv") for offset in ["+1", "+2"]])]
valid_ids = [id for id in all_ids if all([os.path.exists(f"datatrades/{id}_{offset}.csv") for offset in ["-2", "-1", "+1", "+2"]])]
print(len(valid_ids_lower), len(valid_ids_upper), len(valid_ids))
print(len(all_ids))

# Print valid_ids

trades = {"-2":[], "-1":[], "0":[], "+1":[], "+2":[]}
for id in valid_ids:
    for offset in trades:
        tempdf = pd.read_csv(f"datatrades/{id}_{offset}.csv")
        tempdf["index"] = id
        trades[offset].append(tempdf)

trades_concat = {offset: pd.concat(trades[offset]) for offset in trades}
for offset in trades_concat:
    trades_concat[offset].to_csv(f"processedtrades/trades_{offset}.csv", index=False)