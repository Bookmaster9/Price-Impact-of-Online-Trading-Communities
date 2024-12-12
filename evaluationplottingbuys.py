import numpy as np
import matplotlib.pyplot as plt

avg_change_bids = {}
np_overall_price_change_bids = {}

avg_change_asks = {}
np_overall_price_change_asks = {}

avg_change_avgbidask = {}
np_overall_price_change_avgbidask = {}

for offset in ["-2", "-1", "0", "+1", "+2"]:
    np_overall_price_change_bids[offset] = np.load("processedbids/np_overall_price_change_" + offset + ".npy")
    np_overall_price_change_asks[offset] = np.load("processedasks/np_overall_price_change_" + offset + ".npy")
    np_overall_price_change_avgbidask[offset] = np.load("processedavgbidask/np_overall_price_change_" + offset + ".npy")
indicies_bids = np.load("processedbids/valid_id_order.npy")
indicies_asks = np.load("processedasks/valid_id_order.npy")
indicies_avgbidask = np.load("processedavgbidask/valid_id_order.npy")

def find_indices(input):
    indices = []
    for i in range(len(input)):
        if input[i][0] == "O":
            indices.append(i)
    return indices

# find the indices that start with "O"
indices_bids_buys_locs = indicies_bids[find_indices(indicies_bids)]
indices_asks_buys_locs = indicies_asks[find_indices(indicies_asks)]
indices_avgbidask_buys_locs = indicies_avgbidask[find_indices(indicies_avgbidask)]

for offset in ["-2", "-1", "0", "+1", "+2"]:
    np_overall_price_change_bids[offset] = np_overall_price_change_bids[offset][find_indices(indicies_bids)] 
    np_overall_price_change_asks[offset] = np_overall_price_change_asks[offset][find_indices(indicies_asks)]
    np_overall_price_change_avgbidask[offset] = np_overall_price_change_avgbidask[offset][find_indices(indicies_avgbidask)]
    
    avg_change_bids[offset] = np.mean(np_overall_price_change_bids[offset], axis=0)
    avg_change_asks[offset] = np.mean(np_overall_price_change_asks[offset], axis=0)
    avg_change_avgbidask[offset] = np.mean(np_overall_price_change_avgbidask[offset], axis=0)


times = np.arange(-60,301)

# Plot each  of the offsets on separate subplots
fig, axs = plt.subplots(3, 1, figsize=(6, 12))
for offset in ["-2", "-1", "0", "+1", "+2"]:
    axs[1].plot(times[2:], avg_change_bids[offset][2:], label=f"Contract {offset}")
    axs[2].plot(times[2:], avg_change_asks[offset][2:], label=f"Contract {offset}")
    axs[0].plot(times[2:], avg_change_avgbidask[offset][2:], label=f"Contract {offset}")
axs[1].legend(loc = "lower right",fontsize = "small")
axs[2].legend(loc = "lower right",fontsize = "small")
axs[0].legend(loc = "lower right",fontsize = "small")
axs[1].set_title("Average Bid Prices of Contracts")
axs[2].set_title("Average Ask Prices of Contracts")
axs[0].set_title("Average Mid Prices of Contracts")
axs[1].set_ylabel("Average Change", labelpad=10)
axs[2].set_ylabel("Average Change", labelpad=10) 
axs[0].set_ylabel("Average Change", labelpad=10)


for ax in axs:
    ax.set_ylim(-0.005, 0.025)

axs[2].set_xlabel("Seconds Since Message Sent")

#increase space between sub plots
plt.tight_layout()

# make title bigger and closer to the plots
plt.subplots_adjust(top=0.92)

plt.suptitle("Buy To Open Message Contracts Only", fontsize=20)
# Make suptitle bigger
plt.savefig("plots/buytoopenonly_averages.png", dpi = 300, bbox_inches = "tight")
plt.show()
