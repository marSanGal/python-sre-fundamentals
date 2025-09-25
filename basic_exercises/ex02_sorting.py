# Sorting (Lists)

latencies = [85, 23, 99, 42, 17]

# 1. Sort ascending

print(sorted(latencies))

# 2. Sort descending

print(sorted(latencies, reverse=True))

# 3. Get the smallest and largest value

print(min(latencies))
print(max(latencies))

# 4. Sort by "closeness to 50" 

print(sorted(latencies, key=lambda x: abs(x-50)))



