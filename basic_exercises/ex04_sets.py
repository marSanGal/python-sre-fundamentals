# Sets (Uniqueness)

ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3"]

# 1. Remove duplicates using a set

unique_ips = set(ips)
print(unique_ips)

# 2. Check if "10.0.0.2" is in the set

print("10.0.0.2" in unique_ips)

# 3. Add "10.0.0.4"

unique_ips.add("10.0.0.4")
print(unique_ips)
