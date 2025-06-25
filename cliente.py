import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5000

nickname = input("Escolha um apelido: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((HOST, PORT))
except ConnectionRefusedError:
    print("[ERRO] Não foi possível conectar ao servidor.")
    sys.exit()

def enviar_mensagens():
    while True:
        msg = input()
        if msg.lower() == '/sair':
            cliente.send(f"{nickname} saiu do chat.".encode('utf-8'))
            cliente.close()
            print("Você saiu do chat.")
            break
        try:
            cliente.send(f"{nickname}: {msg}".encode('utf-8'))
        except BrokenPipeError:
            print("[ERRO] Conexão perdida.")
            break

def receber_mensagens():
    while True:
        try:
            msg = cliente.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)
        except ConnectionResetError:
            print("[ERRO] Conexão perdida.")
            break
        except OSError:
            break

thread_enviar = threading.Thread(target=enviar_mensagens)
thread_receber = threading.Thread(target=receber_mensagens)

thread_enviar.start()
thread_receber.start()