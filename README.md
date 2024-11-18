# Chat Application

A simple multi-client chat application built using Python's `socket` and `threading` modules. The application includes features like secure communication, private messaging, and user commands. It uses a client-server architecture.

---

## Features

- **Multi-client Support**: Connect multiple clients to the server.
- **Commands**:
  - `/list`: View all connected users.
  - `/pm [user] [message]`: Send a private message to a specific user.
  - `/exit`: Disconnect gracefully from the chat.
- **Secure Communication**: Messages are encrypted using SSL.
- **Extensibility**: Easy to add more features like file sharing or graphical interfaces.

---

## Project Structure

```
chat-app/
├── server.py         # Server-side script
├── client.py         # Client-side script
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

---

## Prerequisites

- Python 3.x
- OpenSSL (for SSL encryption)

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/chat-app.git
   cd chat-app
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Generate SSL certificates (if not already provided):

   ```
   openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes
   ```

---

## Usage

### Server
1. Start the server:
   ```
   python server.py
   ```
   The server will run on `127.0.0.1` and listen on port `7976`.

### Client
1. Start the client:
   ```
   python client.py
   ```
2. Enter a nickname when prompted.
3. Use the following commands in the client:
   - `/list`: List all connected users.
   - `/pm [nickname] [message]`: Send a private message to another user.
   - `/exit`: Disconnect from the chat.

---

## Example

### Terminal 1: Server
```
$ python server.py
Server is running...
Connected with ('127.0.0.1', 12345)
Connected with ('127.0.0.1', 12346)
```

### Terminal 2: Client 1
```
$ python client.py
Enter your nickname: Alice
Welcome to the chat!
Bob has joined the chat!
Bob: Hi Alice!
/pm Bob Hi Bob!
```

### Terminal 3: Client 2
```
$ python client.py
Enter your nickname: Bob
Welcome to the chat!
Alice has joined the chat!
Alice: Hello everyone!
```

---

## Future Enhancements

- Add file sharing support.
- Build a graphical user interface using `Tkinter` or `PyQt`.
- Store user credentials and chat logs in a database for persistence.
- Deploy on a cloud platform for public access.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
