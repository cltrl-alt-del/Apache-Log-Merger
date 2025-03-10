import re
import glob
import os

# Prompt user for log file directory and output file
log_dir = input("Enter the directory containing the log files: ").strip()
output_file = input("Enter the output file path (e.g., merged_access.log): ").strip()
order = input("Enter sorting order (asc/desc): ").strip().lower()

# Validate sorting order
if order not in ["asc", "desc"]:
    print("Invalid sorting order! Defaulting to ascending (asc).")
    order = "asc"

# Define log file pattern to include .log, .log.2, ..., .log.13
log_files = sorted(glob.glob(os.path.join(log_dir, "access.log*")), key=lambda x: (len(x), x))

# Apache log timestamp regex pattern
log_pattern = re.compile(r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})')

# Function to extract timestamp for sorting
def extract_timestamp(log):
    match = log_pattern.search(log)
    return match.group(1) if match else ""

# Read logs
logs = []
for log_file in log_files:
    with open(log_file, "r", encoding="utf-8") as f:
        logs.extend(f.readlines())

# Sort logs by timestamp
logs.sort(key=extract_timestamp, reverse=(order == "desc"))

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(logs)

print(f"Merged and sorted logs saved to {output_file}")
