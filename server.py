import socket
import threading

HOST = "127.0.0.1"
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
print(f"Server runing on {HOST}:{PORT}")

clients = []
usernames = []

def transmision (message, _client):
    for client in clients:
        if client != _client:
            client.send(message)


def handle_message(client):
    while  True:
        try:
            message = client.recv(1024)
            transmision(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            print(f"Chatbot: {username} disconected".encode('utf-8'))
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break

def recibir_coneccion():
    while True:
        client, dir_addres = server.accept()

        client.send("@username".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} is connected with {str(dir_addres)}")

        message = (f"ChatBot: {username} joined the chat!".encode('utf-8'))
        transmision(message, client)
        client.send(f"Connected to server".encode('utf-8'))

        thread = threading.Thread(target=handle_message, args=(client,))
        thread.start()

recibir_coneccion()