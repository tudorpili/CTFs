import hashlib

location_name = "pizzahut"
sha256_hash = hashlib.sha256(location_name.encode()).hexdigest()
print("ctf{" + sha256_hash + "}")