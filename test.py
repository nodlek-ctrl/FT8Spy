import re

# Define a regular expression pattern to find the frequency value
pattern = r"frequency:(\d+)"

# Use re.search to find the match in the text
match = re.search(pattern, status_packet)

# Check if a match is found and extract the frequency value
if match:
    frequency_value = match.group(1)
    print("Frequency value:", frequency_value)
else:
    print("Frequency value not found in the status packet.")
