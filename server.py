import socket
import ssl
import threading

HOST = '127.0.0.1'
PORT = 65432

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='certs/server.crt', keyfile='certs/server.key')

clients = []

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            for client in clients:
                if client != conn:
                    client.sendall(data)
    finally:
        print(f"[-] Disconnected {addr}")
        clients.remove(conn)
        conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[+] Server listening on {HOST}:{PORT}")
    
    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

