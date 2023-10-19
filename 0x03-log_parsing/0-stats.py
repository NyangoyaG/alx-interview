#!/usr/bin/python3
import sys
import signal

# Define the status codes to track
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store statistics
total_size = 0
status_code_counts = {str(code): 0 for code in status_codes}
line_count = 0

def print_statistics():
    print("Total file size:", total_size)
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def process_line(line):
    parts = line.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
            global total_size
            total_size += file_size

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Set up the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        process_line(line)
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle CTRL+C gracefully
    signal_handler(None, None)

