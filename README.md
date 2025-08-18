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

2. 📦 Install Python (if not installed)

Make sure Python 3 is installed:
```
python --version
```
