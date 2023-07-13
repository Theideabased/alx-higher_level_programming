#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Split the line into fields
        fields = line.strip().split()

        # Update total file size
        file_size = int(fields[-1])
        total_file_size += file_size

        # Update status code counts
        status_code = fields[-2]
        status_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")

            # Print status code counts in ascending order
            for code in sorted(status_counts.keys()):
                count = status_counts[code]
                print(f"{code}: {count}")

# Handle keyboard interruption (CTRL + C)
except KeyboardInterrupt:
    print(f"\nTotal file size: {total_file_size}")

    # Print status code counts in ascending order
    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        print(f"{code}: {count}")
