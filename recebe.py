import socket
import threading
import datetime

def recebe_mensagem (sock, porta):
    while True:
        msg = sock.recv(1024)
        if not msg:
            break

        msg = msg.decode()
        tempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"mensagem recebida: {msg}, Timestamp: {tempo}\n")
        with open(f"mensagens{porta}.txt", "a") as file:
            file.write(f"{msg}, Timestamp: {tempo}\n")

enderecos = [("127.0.0.1", 5000), ("127.0.0.1", 5001)]

for e in enderecos:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(e)

    thread = threading.Thread(target=recebe_mensagem, args=(sock, e[1]))
    thread.start()