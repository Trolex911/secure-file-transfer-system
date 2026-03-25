import socket

def encrypt_decrypt(data):
    key = 123
    return bytes([b ^ key for b in data])

server = socket.socket()

server.bind(("0.0.0.0", 9999))

server.listen(1)
print("Waiting for connection...")

conn, addr = server.accept()
print("Connected from:", addr)

file = open("received.txt", "wb")

while True:
    data = conn.recv(1024)
    if not data:
        break
    
    decrypted_data = encrypt_decrypt(data)
    file.write(decrypted_data)

file.close()
conn.close()

print("File received successfully!")
