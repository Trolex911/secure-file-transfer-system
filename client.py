import socket

def encrypt_decrypt(data):
    key = 123
    return bytes([b ^ key for b in data])

client = socket.socket()

client.connect(("127.0.0.1", 9999))

file = open("text.txt", "rb")

while True:
    data = file.read(1024)
    if not data:
        break
    
    encrypted_data = encrypt_decrypt(data)
    client.send(encrypted_data)

file.close()
client.close()

print("File sent successfully!")
