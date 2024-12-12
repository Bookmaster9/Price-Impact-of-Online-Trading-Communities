import os
import pandas as pd
import matplotlib.pyplot as plt

# all_ids is all ids in databeforeafter that have _0.csv
all_ids = [file_name.split("_0.csv")[0] for file_name in os.listdir("databeforeafter") if "_0.csv" in file_name]
valid_ids = [id for id in all_ids if all([os.path.exists(f"databeforeafter/{id}_{offset}.csv") for offset in ["-2", "-1", "+1", "+2"]])]

overall_price_change = []
valid_id_order = []

for id in valid_ids:
    # Load all offsets of data
    data = {}
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        data[offset] = pd.read_csv(f"databeforeafter/{id}_{offset}.csv").dropna()

    # Subtract min of ms_of_day from all ms_of_day
    times = (data["0"]["ms_of_day"]-data["0"]["ms_of_day"].min()-60000)/1000

    weighted_avg_bid = {}
    # Calculated a bid_size and ask_size weighted average price
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        weighted_avg_bid[offset] = ((data[offset]["bid"]*data[offset]["bid_size"])+(data[offset]["ask"]*data[offset]["ask_size"]))/(data[offset]["bid_size"]+data[offset]["ask_size"])

    # plot the asks from all offsets
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        plt.plot(times, weighted_avg_bid[offset], label=offset)
        plt.plot(times, data[offset]["ask"], label=f"{offset} ask", linestyle="--")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Ask Price")
    plt.title(f"Ask Prices for {id}")
    plt.show()
    break
