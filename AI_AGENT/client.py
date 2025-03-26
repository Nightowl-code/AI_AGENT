import socket

# Client side code

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 65432)

    try:
        # Connect to the server
        client_socket.connect(server_address)
        print('Connected to server')

        # Sending messages to the server
        for i in range(2):
            message = f'Hello Server, this is message {i+1}'
            client_socket.sendall(message.encode())
            print(f'Sent: {message}')

            # Receiving response from server
            response = client_socket.recv(1024)
            print(f'Received: {response.decode()}')

    finally:
        # Close the socket
        client_socket.close()
        print('Connection closed')

if __name__ == '__main__':
    main()