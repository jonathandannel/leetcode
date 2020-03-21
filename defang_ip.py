# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

def defangIPaddr(self, address: str) -> str:
    return "[.]".join(address.split("."))