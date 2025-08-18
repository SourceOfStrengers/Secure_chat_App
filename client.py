import socket
import ssl
import threading

HOST = '127.0.0.1'
PORT = 65432

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # For demo only. Use CERT_REQUIRED in production.

def receive_messages(ssl_sock):
    while True:
        try:
            data = ssl_sock.recv(1024)
            if data:
                print("\n[Received]:", data.decode())
        except:
            break

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[+] Connected securely to server.")

        threading.Thread(target=receive_messages, args=(ssock,), daemon=True).start()

        while True:
            msg = input("You: ")
            if msg.lower() == 'exit':
                break
            ssock.sendall(msg.encode())

