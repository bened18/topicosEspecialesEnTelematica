import socket
print("Escriba url a la que desea realizar la peticion")
host = input()
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as yacurl:

    yacurl.connect((host , port))
    print(f'connected to {host} by port {port}')
    yacurl.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

    while True:
        data = yacurl.recv(1024)
        if not data:
            break

        print(data.decode('utf-8'))