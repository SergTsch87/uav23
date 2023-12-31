from dronekit import connect, VehicleMode
from pymavlink import mavutil
import time

# Connect to UDP endpoint.
vehicle = connect('127.0.0.1:14550', wait_ready=True)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print(f"Mode: {vehicle.mode.name}")