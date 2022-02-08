import pyshark

import socket
print("Write the URL to request")
host = input()
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as yacurl:

    yacurl.connect((host , port))
    print(f'connected to {host} by port {port}')
    request = "GET / HTTP/1.1\r\nHost:%s\r\nAccept: text/html\r\nConnection: close\r\n\r\n" % host
    yacurl.sendall(request.encode())
    #yacurl.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

    while True:
        response = yacurl.recv(4096)
        capture = pyshark.LiveCapture(interface=iface_name, bpf_filter='')
        capture.packets_from_tshark
        print(f'capturado: {capture}')
        if not response:
            break

        print(response.decode())


