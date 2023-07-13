#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize metrics variables
total_file_size = 0
status_code_counts = defaultdict(int)

# Process lines from stdin
try:
    for i, line in enumerate(sys.stdin, start=1):
        # Parse the line and extract relevant information
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

