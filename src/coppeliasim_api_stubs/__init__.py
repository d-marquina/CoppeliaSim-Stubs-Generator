"""
CoppeliaSim API Stubs
"""
# This allows for `from coppeliasim_api_stubs import stubs`
from . import stubs

# For convenience, we can also expose placeholder objects for the main API modules.
# This allows for `from coppeliasim_api_stubs import sim` and `sim: sim.sim`.
# At runtime, these are just simple objects. For type checkers, they resolve to the .pyi file.
class _SimPlaceholder:
    pass

sim = _SimPlaceholder()
simUI = _SimPlaceholder()
