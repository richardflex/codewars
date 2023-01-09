import socket

PORT = 1111
SERVER = '127.0.0.1'
HEADER = 1024
TEXT = 'is anybody there'
FORMAT = 'utf-8'


def socket_client():
    text = TEXT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER, PORT))
        while True:
            client.sendall(TEXT.encode(FORMAT))
            response = client.recv(HEADER).decode(FORMAT)
            return response == TEXT

