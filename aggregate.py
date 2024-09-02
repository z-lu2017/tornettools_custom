import os
import json
import itertools 
import numpy as np
import math
from tornettools.util import open_readable_file, dump_json_data


def element_wise_average(listoflist):
    max_row_len=max([len(ll) for ll in listoflist])
    returnlist = []
    for i in range(max_row_len):
        count = 0
        s = 0
        for j in range(len(listoflist)):
            if not math.isnan(listoflist[j][i]):
                count += 1
                s += listoflist[j][i]
        avg = float(s)/count
        returnlist.append(avg)
    return returnlist

def find_folder_with_keyword(root_dir, keyword):
    """Finds folders containing the given keyword in their name."""

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if keyword in dirname:
                yield os.path.join(dirpath, dirname)

# aggregate the three types
root_dir = '/home/ubuntu/tornettools_custom'
keyword = '0.1-matching'

# type of file to aggregate
ttlb = []
rt = []
gp_client = []
cbt = []

for folder in find_folder_with_keyword(root_dir, keyword):
    with open(folder + "/tornet.plot.data/" + "time_to_last_byte_recv.exit.json") as f:
        d = json.load(f)
        ttlb.append(d)
    
    with open(folder + "/tornet.plot.data/" + "round_trip_time.exit.json") as f:
        d = json.load(f)
        rt.append(d)

    with open(folder + "/tornet.plot.data/" + "perfclient_goodput.exit.json") as f:
        d = json.load(f)
        gp_client.append(d)

    with open(folder + "/tornet.plot.data/" + "perfclient_circuit_build_time.exit.json") as f:
        d = json.load(f)
        cbt.append(d)

# average all data
T = list(itertools.zip_longest(*rt, fillvalue=np.nan)) 
average_rt = [np.nanmean(i) for i in T]
# average_rt = element_wise_average(T)

#with open(root_dir + "/" + keyword.replace("0.1-","") + "/tornet.plot.data/" + "round_trip_time.exit.json", "w") as f:
#    json.dumps(average_rt, f)
dump_json_data(average_rt, root_dir + "/" + keyword.replace("0.1-","") + "/tornet.plot.data/" + "round_trip_time.exit.json", compress=False)
print("average round trip = ", np.mean(average_rt))

T = list(itertools.zip_longest(*gp_client, fillvalue=np.nan)) 
average_gp_client = [np.nanmean(i) for i in T]
# average_gp_client = element_wise_average(T)

#with open(root_dir + "/" +  keyword.replace("0.1-","") + "/tornet.plot.data/" + "perfclient_goodput.exit.json", "w") as f:
#    json.dumps(average_gp_client, f)
dump_json_data(average_gp_client, root_dir + "/" +  keyword.replace("0.1-","") + "/tornet.plot.data/" + "perfclient_goodput.exit.json", compress=False)


T = list(itertools.zip_longest(*cbt, fillvalue=np.nan)) 
average_cbt = [np.nanmean(i) for i in T]
# average_cbt = element_wise_average(T)

#with open(root_dir + "/" + keyword.replace("0.1-","") + "/tornet.plot.data/" + "perfclient_circuit_build_time.exit.json", "w") as f:
#    json.dumps(average_cbt, f)
dump_json_data(average_cbt, root_dir + "/" + keyword.replace("0.1-","") + "/tornet.plot.data/" + "perfclient_circuit_build_time.exit.json", compress=False)
print("average circuit build time = ", np.mean(average_cbt))

newttlb = {}
properties = ttlb[0].keys()
for p in properties:
    ttlb_nl = []
    for t in ttlb:
        ttlb_nl.append(t[p])
    T = list(itertools.zip_longest(*ttlb_nl, fillvalue=np.nan)) 
    average = [np.nanmean(i) for i in T]
    # average = element_wise_average(T)
    print("new ttlb for keyword = ", keyword)
    print("with prop =", p)
    print(np.mean(average))
    newttlb[p] = average

#with open(root_dir + "/" + keyword.replace("0.1-", "")+ "/tornet.plot.data/" + "time_to_last_byte_recv.exit.json", "w") as f:
#    json.dumps(newttlb, f)
dump_json_data(newttlb, root_dir + "/" + keyword.replace("0.1-", "")+ "/tornet.plot.data/" + "time_to_last_byte_recv.exit.json", compress=False)
