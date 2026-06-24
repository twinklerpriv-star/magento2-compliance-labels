import zipfile
import os
import re

pptx_path = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\WKO-Seminar - Folien.pptx"
extract_dir = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\scratch\extracted_images"

os.makedirs(extract_dir, exist_ok=True)

with zipfile.ZipFile(pptx_path, 'r') as z:
    # Let's list all files to see the structure
    namelist = z.namelist()
    print(f"Total files in PPTX: {len(namelist)}")
    
    # Find all media files
    media_files = [f for f in namelist if f.startswith('ppt/media/')]
    print(f"Found {len(media_files)} media files:")
    for mf in sorted(media_files):
        print(f"  {mf}")
        
    # Extract media files
    for mf in media_files:
        base_name = os.path.basename(mf)
        dest_path = os.path.join(extract_dir, base_name)
        with open(dest_path, 'wb') as out_f:
            out_f.write(z.read(mf))
        print(f"Extracted {mf} to {dest_path}")

print("Extraction complete.")
