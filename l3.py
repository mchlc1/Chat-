import socket
from colorama import Fore, Style
import c 

FORMAT = 'utf-8'
PORT = 8080
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

clin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clin.connect(ADDR)
print(Style.BRIGHT + Fore.CYAN + "CLIENT=========================================================")
print(f"Connected to server {ADDR}")

def recieve():
        rs = clin.recv(2048).decode(FORMAT)
        print(f"Server says: {rs}")

def send():
    while True:
        w = input("Masukkan teks: ")
        g = int(input("Masukkan geser: "))
        clin.send(w.encode(FORMAT))
        if w.lower() == "exit":
            break

send()
ce()
recieve()
de()
clin.close()
print("Disconnected from server.")













