from email.policy import default
import socket
import pyshark
import click

@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):
    iface_name = 'eth0'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as yacurl:
        yacurl.connect((host , port))
        print(f'connected to {host} by port {port}')
        request = f"GET / HTTP/1.1\r\nHost:{host}\r\nAccept: text/html\r\nConnection: close\r\n\r\n"
        yacurl.sendall(request.encode("utf-8"))
        #yacurl.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

        while True:
            response = yacurl.recv(4096)
            capture = pyshark.LiveCapture(interface=iface_name, bpf_filter=port)
            capture.packets_from_tshark
            print(f'capturado: {capture}')
            if not response:
                break

            response = response.decode("utf-8")
            with open("mi_archivito.html", "w") as f:
                f.write(response)
            