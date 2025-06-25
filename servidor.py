import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clientes = []

def broadcast(mensagem, cliente_origem):
    for cliente in clientes:
        if cliente != cliente_origem:
            try:
                cliente.send(mensagem)
            except (BrokenPipeError, ConnectionResetError):
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def lidar_com_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem:
                break
            broadcast(mensagem, cliente)
        except (ConnectionResetError, OSError):
            break
    if cliente in clientes:
        clientes.remove(cliente)
    cliente.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"[SERVIDOR] Servidor rodando em {HOST}:{PORT}...")

while True:
    try:
        cliente, endereco = servidor.accept()
        print(f"[NOVA CONEXÃO] Conectado com {endereco}")
        clientes.append(cliente)
        thread = threading.Thread(target=lidar_com_cliente, args=(cliente,))
        thread.start()
    except KeyboardInterrupt:
        print("\n[SERVIDOR] Encerrando servidor.")
        break

servidor.close()