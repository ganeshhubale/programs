def is_valid_ipv4(ip: str) -> bool:
    # Split the IP into octets
    parts = ip.split(".")

    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Each part must be a number and non-empty
        if not part.isdigit():
            return False

        num = int(part)

        # Each part should be in the range [0, 255]
        if num < 0 or num > 255:
            return False

        # No leading zeros allowed (except single "0")
        if part != str(num):  # "01", "001" should fail
            return False

    return True

# Example Usage
test_ips = [
    "192.168.1.1",   # ✅ Valid
    "255.255.255.255", # ✅ Valid
    "256.100.100.100", # ❌ Invalid (256 out of range)
    "192.168.1",      # ❌ Invalid (Only 3 octets)
    "192.168.1.01",   # ❌ Invalid (Leading zero)
    "abc.def.gha.bcd",# ❌ Invalid (Non-numeric)
]

for ip in test_ips:
    print(f"{ip}: {'Valid' if is_valid_ipv4(ip) else 'Invalid'}")

# Time Complexity	O(1) (Only 4 parts checked)
# Space Complexity	O(1) (Constant space usage)