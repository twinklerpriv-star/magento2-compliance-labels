import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

prev_conv_id = "7e277a43-3316-4b0b-94c4-d9a7d90933e8"
log_file = rf"C:\Users\thomas.winkler\.gemini\antigravity\brain\{prev_conv_id}\.system_generated\logs\transcript.jsonl"

if not os.path.exists(log_file):
    print(f"Log file not found at: {log_file}")
    sys.exit(0)

print(f"Searching in previous conversation log: {log_file}")

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

found = 0
for idx, line in enumerate(lines, 1):
    if 'wko' in line.lower() or 'wko.at' in line.lower():
        found += 1
        print(f"Line {idx}:")
        # Print a snippet of the line since it might be a JSON line
        if len(line) > 300:
            print(f"  {line[:300]}... [TRUNCATED]")
        else:
            print(f"  {line.strip()}")

print(f"Found {found} matches in log.")
