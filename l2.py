import socket
import threading
from colorama import Fore, Style
import c

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr.bind(ADDR)
svr.listen()

print(Style.BRIGHT + Fore.CYAN + "server===============================================================================")
print("[LISTENING] Server running on " + Fore.GREEN + f"{SERVER}:{PORT}")

def client_recive_msg(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Message from {addr}: {data.decode(FORMAT)}")
        conn.send(b"Message received")
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

while True:
    conn, addr = svr.accept()
    thread = threading.Thread(target=client_recive_msg, args=(conn, addr))
    thread.start()
