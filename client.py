import socket
import threading
import ssl




nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
client = context.wrap_socket(client, server_hostname='127.0.0.1')
client.connect(('127.0.0.1', 7976))

def receive_messages():
    """Continuously receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICKNAME":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print("Disconnected from server.")
            client.close()
            break

def send_messages():
    """Continuously send messages to the server."""
    while True:
        try:
            message = input("")
            if message.startswith('/exit'):
                client.send('/exit'.encode('ascii'))
                print("You left the chat.")
                client.close()
                break
            else:
                client.send(f"{nickname}: {message}".encode('ascii'))
        except Exception as e:
            print("Disconnected from server.")
            client.close()
            break


# Start threads for receiving and sending
thread_receive = threading.Thread(target=receive_messages)
thread_receive.start()

thread_send = threading.Thread(target=send_messages)
thread_send.start()
