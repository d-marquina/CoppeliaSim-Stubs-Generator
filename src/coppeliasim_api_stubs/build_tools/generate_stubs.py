import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple


def parse_signature(signature: str) -> Tuple[List[str], List[str]]:
    """
    Parses a CoppeliaSim function signature to extract parameters and return types.
    Example: "int handle = sim.getObject(string path)" -> (['int'], ['string path'])
    """
    # Separate return from the function call
    if '=' in signature:
        ret_part, call_part = signature.split('=', 1)
    else:
        ret_part, call_part = '', signature

    # Extract parameters from the call
    match = re.search(r'\((.*)\)', call_part)
    params_str = match.group(1) if match else ''
    params = [p.strip() for p in params_str.split(',')] if params_str else []

    # Extract return types
    returns = [r.strip().split(' ')[0] for r in ret_part.split(',')] if ret_part else []

    return returns, params


def py_type(c_type: str) -> str:
    """Converts a C/Lua type to a Python type."""
    TYPE_MAP = {
        'string': 'str',
        'char*': 'str',
        'int': 'int',
        'float': 'float',
        'double': 'float',
        'number': 'float',
        'bool': 'bool',
        'buffer': 'bytes',
        'table': 'dict',
        'map': 'dict',
    }
    c_type = c_type.lower()
    # Look for a direct match first
    return TYPE_MAP.get(c_type, 'list' if '[]' in c_type or '*' in c_type else 'Any')


def generate_stub_file(calltips_path: Path, constants_path: Path, output_pyi: Path):
    """
    Generates a .pyi stub file from a calltips JSON and a constants JSON.
    """
    print(f"Reading calltips from '{calltips_path}'...")
    with open(calltips_path, 'r', encoding='utf-8') as f:
        calltips = json.load(f)

    print(f"Reading constants from '{constants_path}'...")
    try:
        with open(constants_path, 'r', encoding='utf-8') as f:
            constants_data = json.load(f)
    except FileNotFoundError:
        print(f"Warning: Constants file not found at '{constants_path}'. The stub will be generated without constants.")
        constants_data = {}

    # Group functions by module (sim, simUI, etc.)
    modules: Dict[str, Set[str]] = defaultdict(set)
    for func_name, signature in calltips.items():
        if '.' in func_name:
            module_name = func_name.split('.')[0]
            # Ignore low-level or internal functions
            if module_name in ['string', 'table', 'math', 'os', 'debug', 'coroutine']:
                continue
            modules[module_name].add(func_name)

    print(f"Generating stubs for {len(modules)} modules...")

    with open(output_pyi, 'w', encoding='utf-8') as f:
        f.write("from typing import Any, List, Dict, Tuple, Callable, Union\n\n")

        for module_name, funcs in sorted(modules.items()):
            f.write(f"class {module_name}:\n")
            f.write(f'    """API functions for the `{module_name}` module."""\n\n')

            # Write constants for this module
            if module_name in constants_data:
                f.write("    # --- Constants ---\n")
                sorted_constants = sorted(constants_data[module_name].items())
                for const_name, const_value in sorted_constants:
                    const_type = 'str' if isinstance(const_value, str) else 'int' if isinstance(const_value, int) else 'float' if isinstance(const_value, float) else 'Any'
                    # In stubs, we only need the name and type, not the value.
                    f.write(f"    {const_name}: {const_type}\n")
                f.write("\n")

            if funcs:
                f.write("    # --- Functions ---\n")
            
            sorted_funcs = sorted(list(funcs))
            
            if not sorted_funcs:
                f.write("    pass\n\n")
                continue

            for func_name in sorted_funcs:
                full_signature = calltips[func_name].split('\n')[0] # Use only the first overload
                short_func_name = func_name.split('.')[-1]

                try:
                    returns, params = parse_signature(full_signature)

                    # Build the parameter list for Python
                    py_params = ['self']
                    for i, param in enumerate(params):
                        if not param or param == '...':
                            py_params.append('*args')
                            continue
                        
                        parts = param.strip().split(' ')
                        p_type = py_type(parts[0])
                        p_name = parts[1].split('=')[0].replace('[]', '') if len(parts) > 1 else f'arg{i}'
                        p_name = re.sub(r'[^a-zA-Z0-9_]', '', p_name) # Clean name
                        
                        default_val = ""
                        if '=' in param:
                            val_str = parts[1].split('=', 1)[1]
                            if '{' in val_str:
                                default_val = " = ..."  # Use Ellipsis for complex defaults like tables
                            else:
                                default_val = f" = {val_str}"

                        py_params.append(f"{p_name}: {p_type}{default_val}")

                    # Build the return type for Python
                    if not returns or 'void' in returns[0] or '' in returns:
                        py_return_type = 'None'
                    elif len(returns) == 1:
                        py_return_type = py_type(returns[0])
                    else:
                        py_return_type = f"Tuple[{', '.join(py_type(r) for r in returns)}]"

                    f.write(f"    def {short_func_name}({', '.join(py_params)}) -> {py_return_type}:\n")
                    f.write(f'        """{full_signature}"""\n')
                    f.write(f"        ...\n\n")

                except Exception as e:
                    print(f"Could not process signature for '{func_name}': {full_signature} ({e})")
                    f.write(f"    # Could not generate stub for: {func_name}\n")
                    f.write(f"    # Original signature: {full_signature}\n\n")

            f.write("\n")
        
        # Create instances for autocompletion to work directly
        f.write("# --- API instances for autocompletion ---\n")
        for module_name in sorted(modules.keys()):
            f.write(f"{module_name}: {module_name}\n")

    print(f"Success! Stub file saved to '{output_pyi}'")


def main():
    parser = argparse.ArgumentParser(description='Generates a .pyi stub file from CoppeliaSim calltips and constants JSONs.')
    parser.add_argument('calltips_json', type=Path, help='Path to the input calltips.json file.')
    parser.add_argument('constants_json', type=Path, help='Path to the input constants.json file.')
    parser.add_argument('output_pyi', type=Path, help='Path to the output .pyi file.')
    args = parser.parse_args()

    generate_stub_file(args.calltips_json, args.constants_json, args.output_pyi)


if __name__ == '__main__':
    main()