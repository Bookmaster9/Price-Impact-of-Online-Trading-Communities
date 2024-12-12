import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math
from scipy.stats import ks_2samp
import itertools


# # Load the data
trades = {offset: pd.read_csv(f"processedtrades/trades_{offset}.csv") for offset in ["-2", "-1", "0", "+1", "+2"]}
# for offset in trades:
#     trades[offset] = trades[offset].dropna()

# cats = [1.1, 4.1, 8.1, 16.1, 32.1, 64.1, 128.1, 256.1, 512.1, 1024.1]
# mapping = {"-2":0, "-1":1, "0":2, "+1":3, "+2":4}
# output = np.zeros([len(trades.keys()), len(cats)+1])
# for offset in trades:
#     for ind, row in trades[offset].iterrows():
#         added = False
#         for i in range(len(cats)):
#             if row["size"] < cats[i]:
#                 output[mapping[offset], i] += 1
#                 added = True
#                 break
#         if not added:
#             output[mapping[offset], -1] += 1

# np.save("processedtradefreq/output.npy", output)
output = np.load("processedtradefreq/output.npy")
normalized_output = output / np.sum(output, axis=1, keepdims=True)
# plot the data using seaborn
import seaborn as sns
df = pd.DataFrame(normalized_output, columns = ["1", "2-4", "5-8", "9-16", "17-32", "33-64", "65-128", "129-256", "257-512", "513-1024", "1024+"])
df.index = trades.keys()
sns.heatmap(df, annot=True, fmt='.3f')
# limit digits to 3

plt.title("Frequency of trades of different sizes over different offsets")
plt.xlabel("Trade Size")
plt.ylabel("Offset")
plt.savefig("plots/tradesizeheatmap.png")
plt.show()

