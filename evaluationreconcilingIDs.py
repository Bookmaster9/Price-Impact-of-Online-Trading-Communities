import numpy as np
import matplotlib.pyplot as plt
import os

# Load the data

valid_id_order_asks = np.load("processedasks/valid_id_order.npy")
valid_id_order_bids = np.load("processedbids/valid_id_order.npy")
valid_id_order_avgbidask = np.load("processedavgbidask/valid_id_order.npy")

valid_ids = np.intersect1d(np.intersect1d(valid_id_order_asks, valid_id_order_bids), valid_id_order_avgbidask)

# Find the indices of the valid ids in the original data
valid_id_order_asks_locs = np.where(valid_id_order_asks == valid_ids[:, None])[1]
valid_id_order_bids_locs = np.where(valid_id_order_bids == valid_ids[:, None])[1]
valid_id_order_avgbidask_locs = np.where(valid_id_order_avgbidask == valid_ids[:, None])[1]

# select only the indices in the valid_ids that are in the valid_id_order_locs
valid_id_order_asks = valid_id_order_asks[valid_id_order_asks_locs]
valid_id_order_bids = valid_id_order_bids[valid_id_order_bids_locs]
valid_id_order_avgbidask = valid_id_order_avgbidask[valid_id_order_avgbidask_locs]


np_overall_price_change = {}

for offset in ["-2", "-1", "0", "+1", "+2"]:
    np_overall_price_change[offset] = np.load("processedasks/np_overall_price_change_" + offset + ".npy")
    np_overall_price_change[offset] = np_overall_price_change[offset][valid_id_order_asks_locs]
    np.save(f"processedasks/np_overall_price_change_" + offset + ".npy", np_overall_price_change[offset])
    np.save(f"processedasks/valid_id_order.npy", valid_id_order_asks)
    np_overall_price_change[offset] = np.load("processedbids/np_overall_price_change_" + offset + ".npy")
    np_overall_price_change[offset] = np_overall_price_change[offset][valid_id_order_bids_locs]
    np.save(f"processedbids/np_overall_price_change_" + offset + ".npy", np_overall_price_change[offset])
    np.save(f"processedbids/valid_id_order.npy", valid_id_order_bids)
    np_overall_price_change[offset] = np.load("processedavgbidask/np_overall_price_change_" + offset + ".npy")
    np_overall_price_change[offset] = np_overall_price_change[offset][valid_id_order_avgbidask_locs]
    np.save(f"processedavgbidask/np_overall_price_change_" + offset + ".npy", np_overall_price_change[offset])
    np.save(f"processedavgbidask/valid_id_order.npy", valid_id_order_avgbidask)


# avg_change_bids = {}
# np_overall_price_change_bids = {}
# std_change_bids = {}

# for offset in ["-2", "-1", "0", "1", "2"]:
#     avg_change_bids[offset] = np.load("processedbids/avg_change_" + offset + ".npy")
#     np_overall_price_change_bids[offset] = np.load("processedbids/np_overall_price_change_" + offset + ".npy")
#     std_change_bids[offset] = np.load("processedbids/std_change_" + offset + ".npy")


# avg_change_avgbidask = {}
# np_overall_price_change_avgbidask = {}
# std_change_avgbidask = {}

# for offset in ["-2", "-1", "0", "1", "2"]:
#     avg_change_avgbidask[offset] = np.load("processedavgbidask/avg_change_" + offset + ".npy")
#     np_overall_price_change_avgbidask[offset] = np.load("processedavgbidask/np_overall_price_change_" + offset + ".npy")
#     std_change_avgbidask[offset] = np.load("processedavgbidask/std_change_" + offset + ".npy")


