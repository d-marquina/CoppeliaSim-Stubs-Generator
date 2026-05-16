"""
Basic example of connecting to CoppeliaSim and using the stubs for type hinting.
"""
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# The 'typing.TYPE_CHECKING' block is a standard practice.
# The code inside it only runs during static type checking, never at runtime.
# This prevents runtime errors while still providing full type information to the IDE.
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from coppeliasim_api_stubs import stubs

print("Connecting to CoppeliaSim...")
client = RemoteAPIClient()

# Get the 'sim' object from the client.
# The type hint 'stubs.sim' tells the IDE what 'sim' is, enabling autocompletion.
# At runtime, this hint is ignored, and 'sim' is just the object returned by the client.
sim: "stubs.sim" = client.require('sim')

# Now you can use the 'sim' object with full autocompletion and type checking.
# For example, try typing 'sim.' and see the suggestions from your IDE.
try:
    # Get the simulation time
    sim_time = sim.getSimulationTime()
    print(f"Simulation time: {sim_time:.2f}s")

    # Start the simulation
    print("Starting simulation...")
    sim.startSimulation()

    # Wait for a few seconds
    import time
    time.sleep(5)

    # Stop the simulation
    print("Stopping simulation...")
    sim.stopSimulation()

    print("Example finished successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Closing connection.")
    client.close()
