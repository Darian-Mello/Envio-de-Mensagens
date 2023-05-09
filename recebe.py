import socket
import threading
import time

def recebe_mensagem (sock):
    while True:
        msg = sock.recv(1024)
        if not msg:
            break

        msg = msg.decode()
        tempo = time.time_ns()
        print(f"mensagem recebida: {msg}, Timestamp: {tempo}\n")
        with open(f"mensagens.txt", "a") as file:
            file.write(f"{msg}-{tempo}\n")

enderecos = [("", 5000), ("", 5001)]

for e in enderecos:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(e)

    thread = threading.Thread(target=recebe_mensagem, args=(sock,))
    thread.start()