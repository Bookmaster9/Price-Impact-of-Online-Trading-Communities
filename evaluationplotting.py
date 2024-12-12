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
    avg_change_bids[offset] = np.mean(np_overall_price_change_bids[offset], axis=0)

    np_overall_price_change_asks[offset] = np.load("processedasks/np_overall_price_change_" + offset + ".npy")
    avg_change_asks[offset] = np.mean(np_overall_price_change_asks[offset], axis=0)

    np_overall_price_change_avgbidask[offset] = np.load("processedavgbidask/np_overall_price_change_" + offset + ".npy")
    avg_change_avgbidask[offset] = np.mean(np_overall_price_change_avgbidask[offset], axis=0)
indices_bids = np.load("processedbids/valid_id_order.npy")
indices_asks = np.load("processedasks/valid_id_order.npy")
indices_avgbidask = np.load("processedavgbidask/valid_id_order.npy")

times = np.arange(-60,301)

# Plot each  of the offsets on separate subplots
fig, axs = plt.subplots(3, 1, figsize=(9, 12))
for offset in ["-2", "-1", "0", "+1", "+2"]:
    axs[1].plot(times[2:], avg_change_bids[offset][2:], label=f"Contract {offset}")
    axs[2].plot(times[2:], avg_change_asks[offset][2:], label=f"Contract {offset}")
    axs[0].plot(times[2:], avg_change_avgbidask[offset][2:], label=f"Contract {offset}")
axs[1].legend(loc = "upper left")
axs[2].legend(loc = "upper left")
axs[0].legend(loc = "upper left")
axs[1].set_title("Average Bid Prices of Contracts")
axs[2].set_title("Average Ask Prices of Contracts")
axs[0].set_title("Average Mid Prices of Contracts")
axs[1].set_ylabel("Average Change", labelpad=10)
axs[2].set_ylabel("Average Change", labelpad=10) 
axs[0].set_ylabel("Average Change", labelpad=10)


for ax in axs:
    ax.set_ylim(-0.012, 0.02)

axs[2].set_xlabel("Seconds Since Message Sent")

#increase space between sub plots
plt.tight_layout()

# make title bigger and closer to the plots
plt.subplots_adjust(top=0.92)

plt.suptitle("Average Bid/Ask/Mid Price Change of Mentioned Contracts", fontsize=20)
# Make suptitle bigger
# plt.savefig("plots/evaluationplotting_averages.png", dpi = 300, bbox_inches = "tight")
plt.show()
