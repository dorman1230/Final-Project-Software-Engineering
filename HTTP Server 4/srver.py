import socket
import select
import protocol


print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 80))
server_socket.listen()
print("Listening for clients...")

client_sockets = []
messages_to_send = []
block_sockets = []


while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])

    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)

        else:
            data = current_socket.recv(1024).decode()

            if protocol.chck_HTTP_request(data) is False:
                print("Connection closed")
                client_sockets.remove(current_socket)
                current_socket.close()

            else:
                print("=============================================================")
                print(data)
                print("=============================================================")
