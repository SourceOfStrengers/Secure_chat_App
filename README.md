
# Secure_chat_App
Secure Chat App using TLS (SSL over Sockets)  Terminal-based chat application that uses **TLS/SSL over sockets** to ensure encrypted communication between clients and a server. 
Built with **Python**, it demonstrates key cybersecurity principles including encryption, certificate handling, and secure client-server communication.



## 📌 Features

- TLS/SSL secured chat
- Multi-client support
- Self-signed certificate for demo use
- Simple terminal interface

---

## 📁 Project Structure
```
secure_chat/
├── server.py # Secure chat server
├── client.py # Secure chat client
├── certs/
│ ├── server.crt # Self-signed certificate
│ └── server.key # Private key
└── README.md # Project instructions
```

---

## ⚙️ Requirements

- Python 3.6+
- OpenSSL (for certificate generation)

---

## 🔧 Setup Instructions

### 1. 🔽 Clone the Repository

```bash
git clone https://github.com/SourceOfStrengers/Secure_Chat_App.git
cd Secure_Chat_App
```
Or just download the ZIP and extract it.

### 2. 📦 Install Python (if not installed)

Make sure Python 3 is installed:
```
python --version
```
If not, download from: https://www.python.org/downloads/

### 3. 🔐 Generate SSL Certificate (Optional)

Already included, but you can regenerate:
```
mkdir certs
openssl req -new -x509 -days 365 -nodes -out certs/server.crt -keyout certs/server.key
```

You can customize the details when prompted.


### 🚀 How to Run
#### 🔹 Start the Server
```
python server.py
```
The server will start on `127.0.0.1:65432`.


#### 🔹 Run the Client (In a new terminal)
```
python client.py
```
Open multiple terminals to connect multiple clients.
