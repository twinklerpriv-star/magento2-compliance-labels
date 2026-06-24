import shutil
import os

src_dir = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\scratch\test_render"
dest_dir = r"C:\Users\thomas.winkler\.gemini\antigravity\brain\c0963404-99f0-498e-9958-b86a3114c369\scratch\test_render"

os.makedirs(dest_dir, exist_ok=True)

for i in [1, 7, 11, 15]:
    filename = f"Folie{i}.PNG"
    src_file = os.path.join(src_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)
        print(f"Copied {filename} to {dest_file}")
