import argparse
import subprocess
import sys
from pathlib import Path

def run():
    """
    Orchestrates the execution of scripts to generate the CoppeliaSim API stubs.
    Accepts flags to generate stubs for specific languages.
    """
    parser = argparse.ArgumentParser(description='Generate API stubs for CoppeliaSim.')
    parser.add_argument('--python', action='store_true', help='Generate Python stubs.')
    parser.add_argument('--typescript', action='store_true', help='Generate TypeScript definitions.')
    args = parser.parse_args()

    # If no specific language is requested, generate for all
    generate_all = not args.python and not args.typescript
    generate_python = args.python or generate_all
    generate_typescript = args.typescript or generate_all

    try:
        package_root = Path(__file__).parent
        project_root = package_root.parent.parent

        vendor_dir = package_root / "vendor" / "coppeliasim"
        build_tools_dir = package_root / "build_tools"
        
        stubs_dir = project_root / "stubs"
        generated_data_dir = project_root / "generated_data"
        
        generated_data_dir.mkdir(exist_ok=True)
        (stubs_dir / "python" / "coppeliasim_api_stubs").mkdir(exist_ok=True, parents=True)
        (stubs_dir / "typescript").mkdir(exist_ok=True, parents=True)

        calltips_json = generated_data_dir / "calltips.json"
        constants_json = generated_data_dir / "constants.json"
        
        # These steps are common and always need to run if any generation is happening
        if generate_python or generate_typescript:
            print("Executing get_raw_calltips.py...")
            subprocess.run(
                [sys.executable, str(vendor_dir / "get_raw_calltips.py"), str(calltips_json)],
                check=True, text=True
            )
            
            print("Executing get_constants.py...")
            subprocess.run(
                [sys.executable, str(vendor_dir / "get_constants.py"), str(constants_json)],
                check=True, text=True
            )

        if generate_python:
            print("Executing generate_stubs.py for Python...")
            stubs_pyi = stubs_dir / "python" / "coppeliasim_api_stubs" / "stubs.pyi"
            subprocess.run(
                [sys.executable, str(build_tools_dir / "generate_stubs.py"), str(calltips_json), str(constants_json), str(stubs_pyi)],
                check=True, text=True
            )
            print(f"Python stubs generated successfully at: {stubs_pyi}")

        if generate_typescript:
            print("Executing generate_typescript.py for TypeScript...")
            stubs_d_ts = stubs_dir / "typescript" / "coppeliasim-api.d.ts"
            subprocess.run(
                [sys.executable, str(build_tools_dir / "generate_typescript.py"), str(calltips_json), str(constants_json), str(stubs_d_ts)],
                check=True, text=True
            )
            print(f"TypeScript definitions generated successfully at: {stubs_d_ts}")

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
