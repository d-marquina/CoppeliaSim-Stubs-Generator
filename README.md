# CoppeliaSim API Stubs

## 1. Description

This package provides Python type stubs (`.pyi` files) for the CoppeliaSim ZMQ Remote API. Its main purpose is to enable robust autocompletion and static type analysis in modern IDEs (like PyCharm, VS Code, etc.), improving developer experience and code quality.

The package achieves this in two ways:
1.  It includes a pre-generated `stubs.pyi` file that works out-of-the-box with a recent version of CoppeliaSim (4.10.0).
2.  It provides a command-line tool to allow users to easily regenerate these stubs based on their specific, running version of CoppeliaSim.

This package bundles and uses three utility scripts from the official CoppeliaSim installation (`get_raw_calltips.py`, `get_constants.py`, and `get_constants.lua`), which can be originally found in `CoppeliaSimFolder/programming/zmqRemoteApi/tools`. These scripts are used by the `update-coppeliasim-stubs` command to query the simulator's API.

## 2. Requirements

Before using this package, please ensure you have the following:
*   **CoppeliaSim**: An active and running instance of the CoppeliaSim simulator. The generation script needs to connect to it.
*   **Python Environment**: Python 3.7+ with the official `zmqRemoteApi` library installed. This library can be installed with:
```bash
pip install coppeliasim-zmqremoteapi-client
```

## 3. Installation

You can install this package in two ways from the project's root directory.

#### Editable Mode (Recommended for Development)
If you have cloned this repository and want your local changes to be immediately reflected, install it in editable mode:
```bash
pip install -e .
```
To remove the package, you can run:
```bash
pip uninstall coppeliasim-api-stubs
```

#### Regular Installation from Source
To install the package from the local source code in a standard way (without a symbolic link), run the following command. This is useful for testing the final installation behavior before publishing.
```bash
pip install .
```

## 4. Usage: Updating the Stubs

If you update your CoppeliaSim version or suspect the bundled stubs are out of sync, you can easily regenerate them.

First, ensure the CoppeliaSim application is running. Then, execute the following command in your terminal:
```bash
update-coppeliasim-stubs
```
This command will automatically run the necessary scripts to query the CoppeliaSim API, generate the intermediate JSON files, and build the final `stubs.pyi` file within the package.

**Note on `simROS2`:** The pre-generated stub file included in this package was created on Windows. The `simROS2` plugin is only available on Linux, so its API information is not included. If you are working on Linux and need stubs for `simROS2`, you can regenerate the file using the `update-coppeliasim-stubs` command.

## 5. Example

For complete, runnable scripts demonstrating how to use the ZMQ Remote API with the benefits of these type stubs, please refer to the files in the `/examples` directory.

A typical client script using these stubs would look like this:
```python
# This example assumes you have the zmqRemoteApi library installed
from coppeliasim_zmqremoteapi_client import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from coppeliasim_api_stubs import stubs

# Create the client
client = RemoteAPIClient()
sim: "stubs.sim" = client.require('sim')

# Now you can use the API with full autocompletion
sim.startSimulation()
# ...
sim.stopSimulation()
```
