from pymodbus.client import ModbusTcpClient

# Connect to the Modbus TCP server
client = ModbusTcpClient('127.0.0.1')

# Write a True value to coil 1
client.write_coil(0, True)  # Note: Modbus uses 0-based addressing
client.write_coil(5, True)  # Note: Modbus uses 5-based addressing

# Read the state of coil 1
result = client.read_coils(0, 1)  # Reading from coil 0
r2 = client.read_coils(5, 1)      # Reading from coil 5

# Print the result
print(f"State of coil 0: {result.bits[0]}")
print(result.bits)
print(f"State of coil 5: {r2.bits[0]}")
print(r2.bits)
# Depending on your needs, you might want to print result.bits or result as well

# Close the Modbus TCP connection
client.close()
