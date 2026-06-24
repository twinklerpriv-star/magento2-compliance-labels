import os
import shutil
import sys

# Configure stdout for German Windows encoding (prevent Unicode errors)
sys.stdout.reconfigure(encoding='utf-8')

# Dynamically determine workspace directory (parent of the scratch folder)
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BRAIN_DIR = r"C:\Users\thomas.winkler\.gemini\antigravity\brain\cb4e98c8-ac23-43f6-ad56-7f4599f9b4da"

def make_long_path(path):
    abs_path = os.path.abspath(path)
    if not abs_path.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_path
    return abs_path

def get_md_files(base_dir):
    md_files = {}
    long_base = make_long_path(base_dir)
    EXCLUDE_DIRS = {'EINSTUFUNG', 'Archiv', '.git', '.system_generated'}
    for root, dirs, files in os.walk(long_base):
        # Exclude hidden directories, .git, and configured directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                # Compute relative path from long_base
                rel_path = os.path.relpath(full_path, long_base)
                md_files[rel_path] = {
                    'full_path': full_path,
                    'mtime': os.path.getmtime(full_path)
                }
    return md_files

def main():
    print("Starte Workspace-Synchronisation mit Long-Path-Support...")
    ws_long = make_long_path(WORKSPACE_DIR)
    br_long = make_long_path(BRAIN_DIR)

    if not os.path.exists(ws_long):
        print(f"Fehler: Workspace-Pfad existiert nicht: {{WORKSPACE_DIR}}")
        return
    if not os.path.exists(br_long):
        os.makedirs(br_long)
        print(f"Brain-Verzeichnis erstellt: {{BRAIN_DIR}}")

    workspace_files = get_md_files(WORKSPACE_DIR)
    brain_files = get_md_files(BRAIN_DIR)

    all_rel_paths = set(workspace_files.keys()).union(set(brain_files.keys()))
    copied_to_brain = 0
    copied_to_workspace = 0

    for rel_path in all_rel_paths:
        ws_info = workspace_files.get(rel_path)
        br_info = brain_files.get(rel_path)

        if ws_info and not br_info:
            # File is in workspace only, copy to brain
            dest_path = os.path.join(br_long, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(ws_info['full_path'], dest_path)
            print(f"[Workspace -> Brain] Kopiert: {{rel_path}}")
            copied_to_brain += 1
        elif br_info and not ws_info:
            # File is in brain only, copy to workspace
            dest_path = os.path.join(ws_long, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(br_info['full_path'], dest_path)
            print(f"[Brain -> Workspace] Kopiert: {{rel_path}}")
            copied_to_workspace += 1
        else:
            # File is in both, compare mtime
            time_diff = ws_info['mtime'] - br_info['mtime']
            if time_diff > 0.1:
                # Workspace is newer, copy to brain
                dest_path = os.path.join(br_long, rel_path)
                shutil.copy2(ws_info['full_path'], dest_path)
                print(f"[Workspace -> Brain] Aktualisiert (Workspace neuer): {{rel_path}}")
                copied_to_brain += 1
            elif time_diff < -0.1:
                # Brain is newer, copy to workspace
                dest_path = os.path.join(ws_long, rel_path)
                shutil.copy2(br_info['full_path'], dest_path)
                print(f"[Brain -> Workspace] Aktualisiert (Brain neuer): {{rel_path}}")
                copied_to_workspace += 1

    print("\nSynchronisation abgeschlossen:")
    print(f"- Kopiert/Aktualisiert zu Brain: {{copied_to_brain}}")
    print(f"- Kopiert/Aktualisiert zu Workspace: {{copied_to_workspace}}")

if __name__ == "__main__":
    main()
