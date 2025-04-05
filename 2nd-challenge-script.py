
strings = [
    "SfBsOxPvNMDyNAhRSgsG",
    "VjYOkGDgkkXgULZUkCeh",
    "OYgUClVWJQAvOtMfBSPg",
    "UgGADoBNyIpiGNyfyuet",
    "RoSgSYiwNwAcSgnPOsMB",
    "4sGvkBZfEqfHEgvkUeUL",
    "ullIdbFSSDZrKCSAJIUz",
    "FPVZxzrNHXShDeRb1GXd",
    "RNpVNeyZRVHTOwZuNdQq",
    "VALsFVveUNPuUoDWlpXu",
    "VyNbOyZjyGBwQUiUxeSe",
    "xO2rYv2pXL3UWoDvBTDQ",
    "qCOaRDOZicRnhDSacIgc",
    "bGUTstlyoElXoIVVghRO",
    "MmNRiDVggENtBjNHvw>g",
    "MC2BCa1DjAyglyzgwQ>v",
    "LeNdcAOGPROrjrOUSiWC",
    "YQEvXfUjbEERJDEjLZcS",
    "baCAeWZGrnROqkJKchEi",
    "oLDKgG6TxDzrQu6amIlZ"
]

password = ""

for i in range(96):
    
    string_index = i % 20
    selected_string = strings[string_index]
    
    
    offset = (i // 10) * 2
    
    
    char = selected_string[offset]
    
    
    password_char = chr(ord(char) - 1)
    
    
    password += password_char

print("Password:", password)