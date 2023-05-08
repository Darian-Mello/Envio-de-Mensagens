import socket
import threading
import time

def envia_mensagem (ip, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((ip, porta))

    cont_mensagens = 0
    while True:
        cont_mensagens += 1
        msg = f"ID: {threading.current_thread().ident}, Mensagem: {cont_mensagens}"
        print(f"Enviando mensagem para: {ip}:{porta} - {msg}")
        sock.send(msg.encode())
        time.sleep(0.5)

    client_socket.close()

enderecos = [("127.0.0.1", 5000), ("127.0.0.1", 5001)]

for e in enderecos:
    thread = threading.Thread(target=envia_mensagem, args=e)
    thread.start()
