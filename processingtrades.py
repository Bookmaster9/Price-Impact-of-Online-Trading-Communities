import pandas as pd
import numpy as np
import os

to_combine = []
count = 0

for file in os.listdir("datatrades"):
    if count%100 == 0:
        print(count)
    count += 1
    if file.endswith(".csv"):
        data = pd.read_csv("datatrades/"+file)
        data["index"] = file.split(".")[0]
        to_combine.append(data)

combined = pd.concat(to_combine)
combined.to_csv("combinedtrades.csv", index=False)

