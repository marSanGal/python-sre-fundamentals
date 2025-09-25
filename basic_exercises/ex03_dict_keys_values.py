# Keys & Values (Dicts)

service_status = {
    "api": "healthy",
    "db": "degraded",
    "cache": "healthy"
}

# 1. Print all keys

print(list(service_status.keys()))

# 2. Print all values

print(list(service_status.values()))

# 3. Print "api is healthy" style strings for each

for k, v in service_status.items():
    print(f"{k} is {v}")

# 4. Check if "db" is in the dict

print("db" in service_status)

# 5. Add a new key "queue": "down"

service_status["queue"] = "down"
print(service_status)

