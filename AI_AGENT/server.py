import socket

# Server code

def main():
    server_address = ('localhost', 65432)  # Server address and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen()
        print('Server listening on', server_address)

        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            for _ in range(2):  # Receive two messages
                data = conn.recv(1024)
                print('Received from client:', data.decode())
                conn.sendall(b'Received: ' + data)  # Send response

if __name__ == '__main__':
    main()