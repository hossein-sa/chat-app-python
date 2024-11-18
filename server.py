import socket
import threading
import ssl

# Basic server setup
host = '127.0.0.1'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# SSL wrapping
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
server = context.wrap_socket(server, server_side=True, keyfile="key.pem", certfile="cert.pem")

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
            message = client.recv(1024).decode('ascii')
            if message.startswith('/list'):
                client.send(f"Users online: {', '.join(nicknames)}".encode('ascii'))
            elif message.startswith('/pm'):
                _, target_nickname, private_message = message.split(" ", 2)
                if target_nickname in nicknames:
                    target_index = nicknames.index(target_nickname)
                    target_client = clients[target_index]
                    target_client.send(f"PM from {nicknames[clients.index(client)]}: {private_message}".encode('ascii'))
                else:
                    client.send("User not found.".encode('ascii'))
            elif message.startswith('/exit'):
                raise ConnectionError
            else:
                broadcast(message.encode('ascii'), exclude_client=client)
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
