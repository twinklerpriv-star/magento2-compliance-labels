import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

try:
    import win32com.client
except ImportError:
    print("Error: pywin32 is not installed. Please install it using 'pip install pywin32'.")
    sys.exit(1)

def main():
    pptx_path = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\wko_seminar_verbrauchsaenderungsgesetz.pptx"
    output_dir = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\scratch\test_render"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize PowerPoint
    print("Launching PowerPoint in the background...")
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    except Exception as e:
        print(f"Failed to launch PowerPoint: {e}")
        sys.exit(1)
        
    try:
        # Open the presentation
        # Open method arguments: (FileName, ReadOnly, Untitled, WithWindow)
        # We open without a window (WithWindow = 0 / False)
        pres = powerpoint.Presentations.Open(pptx_path, ReadOnly=True, WithWindow=False)
        print(f"Successfully opened: {pptx_path}")
        
        # Save as PNG
        # PP_SAVE_AS_PNG is format number 18
        # We can also use pres.Export(Path, FilterName)
        # This will export all slides to output_dir
        pres.Export(output_dir, "PNG")
        print(f"Successfully exported slides to: {output_dir}")
        
        pres.Close()
    except Exception as e:
        print(f"An error occurred during export: {e}")
    finally:
        powerpoint.Quit()

if __name__ == "__main__":
    main()
