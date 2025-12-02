from pathlib import Path
import shutil
import sys



def recursive_folder_copy(scr, dst):
    try:
        for element in scr.iterdir():
            if element.is_dir():
                # Recursive call for subdirectory
                recursive_folder_copy(element, dst)
            elif element.is_file():
                # Determine the file extension
                ext = element.suffix[1:].lower()
                if not ext:
                    ext = 'no_extension'
                
                # Create subdirectory for the extension
                ext_dir = dst / ext
                ext_dir.mkdir(parents=True, exist_ok=True)
                
                # Copy file to the target directory
                shutil.copy2(element, ext_dir / element.name)
                print(f"Copied {element} -> {ext_dir / element.name}")
    except PermissionError:
        print(f"No permission to access {scr}")
    except Exception as e:
        print(f"Error while processing {scr}: {e}")



def main():

    # --- Check command line arguments ---
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_dir> [destination_dir]")
        sys.exit(1)

    
    source_dir = Path(sys.argv[1])
    dest_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else source_dir.parent / 'dist'
        
    # Make destination absolute if relative
    if not dest_dir.is_absolute():
        dest_dir = Path.cwd() / dest_dir

    # Verify that source directory exists
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Source directory does not exist: {source_dir}")
        sys.exit(1)

    # Create destination directory if it doesn't exist
    dest_dir.mkdir(parents=True, exist_ok=True)

    recursive_folder_copy(source_dir, dest_dir)

if __name__ == "__main__":
    main()