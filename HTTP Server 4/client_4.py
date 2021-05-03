import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 80))
my_input = ""

while True:
    my_input = input("Please enter your command:")
    my_socket.send(my_input.encode("utf-8"))
    data = my_socket.recv(1024).decode("utf-8")
    print(data)

my_socket.close()