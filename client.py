import socket
import threading

username = input("Ingrese su user: ")

HOST = "127.0.0.1"
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recibir_mensaje():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode('utf-8'))

            else:
                print(message)
        except:
            print("An error ocurred")
            client.close
            break

def escribir_mensaje():
    while True:
        message = (f"{username}: {input('')}")
        client.send(message.encode('utf-8'))

recibir_thread = threading.Thread(target=recibir_mensaje)
recibir_thread.start()

escribir_thread = threading.Thread(target=escribir_mensaje)
escribir_thread.start()

