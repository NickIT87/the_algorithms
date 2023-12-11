from pymodbus.client import ModbusTcpClient

# Connect to the Modbus TCP server
client = ModbusTcpClient('127.0.0.1', port=502)

# Specify the starting address and the number of discrete inputs to read
start_address = 0
num_inputs = 10  # Adjust this based on the number of discrete inputs you want to read

# Read the states of discrete inputs starting from the specified address
result = client.read_discrete_inputs(start_address, num_inputs)

# Print the result
print("States of discrete inputs:", result.bits)

# Close the Modbus TCP connection
client.close()
