from pymodbus.client import ModbusTcpClient

# Connect to the Modbus TCP server
client = ModbusTcpClient('127.0.0.1', port=502)

# Specify the register address and the value to write
register_address = 0
value_to_write = 1234  # Adjust this based on the numeric value you want to write

# Write the value to the holding register
client.write_register(register_address, value_to_write)

# Read the value back from the holding register
result = client.read_holding_registers(register_address, 1)

# Print the result
print(f"Value read from holding register: {result.registers[0]}")

# Close the Modbus TCP connection
client.close()
