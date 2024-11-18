import socket
import threading

# Basic server setup
host = '127.0.0.1'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message, exclude_client=None):
    """Send a message to all connected clients."""
    for client in clients:
        if client != exclude_client:  # Avoid echoing to the sender
            client.send(message)

def handle_client(client):
    """Handle communication with a single client."""
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise ConnectionError
            broadcast(message, exclude_client=client)
        except Exception as e:
            index = clients.index(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat.".encode('ascii'))
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            break

def accept_clients():
    """Accept new client connections."""
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        # Ask for and store the nickname
        client.send("NICKNAME".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        broadcast(f"{nickname} has joined the chat!".encode('ascii'))
        client.send("Welcome to the chat!".encode('ascii'))

        # Handle this client in a separate thread
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
accept_clients()
