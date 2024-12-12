import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# all_ids is all ids in databeforeafter that have _0.csv
all_ids = [file_name.split("_0.csv")[0] for file_name in os.listdir("databeforeafter") if "_0.csv" in file_name]
valid_ids = [id for id in all_ids if all([os.path.exists(f"databeforeafter/{id}_{offset}.csv") for offset in ["-2", "-1", "+1", "+2"]])]

overall_price_change = {"-2":[], "-1":[], "0":[], "+1":[], "+2":[]}
valid_id_order = []

maxcount = 0

for id in valid_ids:
    # Load all offsets of data
    data = {}
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        data[offset] = pd.read_csv(f"databeforeafter/{id}_{offset}.csv").dropna()

    # Subtract min of ms_of_day from all ms_of_day
    times = (data["0"]["ms_of_day"]-data["0"]["ms_of_day"].min()-60000)/1000

    weighted_avg_price = {}
    # Calculated a bid_size and ask_size weighted average price
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        weighted_avg_price[offset] = data[offset]["bid"]

    valid_id_flag = True
    for offset in ["-2", "-1", "0", "+1", "+2"]:
        price_change = (weighted_avg_price[offset] - weighted_avg_price[offset][60])/weighted_avg_price[offset][60]
        if len(price_change) == 361 and price_change.notna().all():
            valid_id_flag = True
        else:
            valid_id_flag = False
            break
    
    if valid_id_flag:
        for offset in ["-2", "-1", "0", "+1", "+2"]:
            price_change = (weighted_avg_price[offset] - weighted_avg_price[offset][60])/weighted_avg_price[offset][60]
            overall_price_change[offset].append(price_change.tolist())
        valid_id_order.append(id)
    

# Convert overall_price_change to an np array and calculate all columns averages
np_overall_price_change = {offset: np.array(overall_price_change[offset]) for offset in ["-2", "-1", "0", "+1", "+2"]}
print([np.sum(np.isnan(np_overall_price_change[offset])) for offset in ["-2", "-1", "0", "+1", "+2"]])
avg_change = {offset: np.mean(np_overall_price_change[offset], axis=0) for offset in ["-2", "-1", "0", "+1", "+2"]}
std_change = {offset: np.std(np_overall_price_change[offset], axis=0) for offset in ["-2", "-1", "0", "+1", "+2"]}

for offset in ["-2", "-1", "0", "+1", "+2"]:
    print(np_overall_price_change[offset].shape)
print(len(valid_id_order))

for offset in ["-2", "-1", "0", "+1", "+2"]:
    np.save(f"processedbids/np_overall_price_change_{offset}.npy", np_overall_price_change[offset])
    np.save(f"processedbids/avg_change_{offset}.npy", avg_change[offset])
    np.save(f"processedbids/std_change_{offset}.npy", std_change[offset])
np.save("processedbids/valid_id_order.npy", np.array(valid_id_order))


# Plot all 5 average change lines with labels together
for offset in ["-2", "-1", "0", "+1", "+2"]:
    plt.plot(times, avg_change[offset], label=f"{offset} Average Change")
plt.legend()
plt.show()
