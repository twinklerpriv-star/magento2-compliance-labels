import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\thomas.winkler\.gemini\antigravity\brain"
found_matches = []

if not os.path.exists(brain_dir):
    print("Brain directory not found.")
    sys.exit(0)

# Traverse all conversation directories
for conv_id in os.listdir(brain_dir):
    conv_path = os.path.join(brain_dir, conv_id)
    if not os.path.isdir(conv_path) or conv_id == "tempmediaStorage":
        continue
        
    log_file = os.path.join(conv_path, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(log_file):
        continue
        
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            for idx, line in enumerate(f, 1):
                if 'wko' in line.lower() or 'wko.at' in line.lower():
                    # Parse as json to get content if possible
                    try:
                        data = json.loads(line)
                        content = data.get("content", "")
                        source = data.get("source", "UNKNOWN")
                        # Look for links in content
                        # Let's extract any URLs containing wko
                        urls = []
                        import re
                        urls = re.findall(r'https?://[^\s\'"\]\)]+', content)
                        wko_urls = [u for u in urls if 'wko' in u.lower()]
                        if wko_urls:
                            for url in wko_urls:
                                found_matches.append((conv_id, source, url))
                        else:
                            # If no direct URL pattern matched but 'wko' is in it, save the text snippet
                            found_matches.append((conv_id, source, f"Snippet (Line {idx}): {content[:150]}..."))
                    except Exception:
                        found_matches.append((conv_id, "RAW", f"Snippet (Line {idx}): {line[:150]}..."))
    except Exception as e:
        pass

print(f"Found {len(found_matches)} matches across all past logs:")
# Remove duplicates
unique_matches = list(set(found_matches))
for conv_id, source, val in unique_matches:
    print(f"Session: {conv_id} ({source}):")
    print(f"  {val}")
