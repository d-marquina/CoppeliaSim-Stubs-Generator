
import subprocess
import sys
from pathlib import Path

def run():
    """
    Orchestrates the execution of scripts to generate the CoppeliaSim API stubs.
    """
    try:
        # 1. Determine the project root path
        project_root = Path(__file__).parent.parent.parent
        
        # 2. Define paths to directories
        vendor_dir = project_root / "vendor" / "coppeliasim"
        build_tools_dir = project_root / "build_tools"
        generated_data_dir = project_root / "generated_data"
        src_dir = project_root / "src" / "coppeliasim_api_stubs"
        
        # 3. Create the generated_data directory if it doesn't exist
        generated_data_dir.mkdir(exist_ok=True)
        
        # Define file paths
        calltips_json = generated_data_dir / "calltips.json"
        constants_json = generated_data_dir / "constants.json"
        stubs_pyi = src_dir / "stubs.pyi"
        
        print("Executing get_raw_calltips.py...")
        # 4. Execute get_raw_calltips.py, passing the output path as an argument
        subprocess.run(
            [
                sys.executable,
                str(vendor_dir / "get_raw_calltips.py"),
                str(calltips_json)
            ],
            check=True,
            text=True
        )
        
        print("Executing get_constants.py...")
        # 5. Execute get_constants.py
        subprocess.run(
            [
                sys.executable,
                str(vendor_dir / "get_constants.py"),
                str(constants_json)
            ],
            check=True,
            text=True
        )
        
        print("Executing generate_stubs.py...")
        # 6. Execute generate_stubs.py
        subprocess.run(
            [
                sys.executable,
                str(build_tools_dir / "generate_stubs.py"),
                str(calltips_json),
                str(constants_json),
                str(stubs_pyi),
            ],
            check=True,
            text=True
        )
        
        print(f"Stubs generated successfully at: {stubs_pyi}")

    except subprocess.CalledProcessError as e:
        print(f"Error during subprocess execution: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run()
