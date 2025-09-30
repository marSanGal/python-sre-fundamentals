# Problem

# You are given a list of IPv4 addresses as strings.
# Some addresses may be duplicated, and the list may not be sorted.

# Write a function that:
# 	1.	Removes duplicates.
# 	2.	Sorts the remaining IP addresses in ascending numeric order.
# 	3.	Returns the cleaned list.

import ipaddress

ips = ["10.0.0.2", "192.168.1.5", "10.0.0.1", "192.168.1.5"]

def sort_ips(ips):
    single_ips = set(ips) # remove duplicates
    sorted_ips = sorted(single_ips, key=ipaddress.IPv4Address) # sort numerically as real IPs
    return sorted_ips 

print(sort_ips(ips))