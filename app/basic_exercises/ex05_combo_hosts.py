# Combo Challenge 

# Given:
logs = [
    {"host": "10.0.0.1", "status": "ok"},
    {"host": "10.0.0.2", "status": "fail"},
    {"host": "10.0.0.1", "status": "ok"},
]

# 1. Collect all host IPs into a list

host_ips = [entry["host"] for entry in logs]
print(host_ips)

# 2. Remove duplicates (use a set)

unique_logs = set(host_ips)
print(unique_logs)

# 3. Sort the unique IPs

ordered_ips = sorted(unique_logs)
print(unique_logs)

# 4. Print: "Found hosts: <list>"

print(f"Found hosts: {ordered_ips}")