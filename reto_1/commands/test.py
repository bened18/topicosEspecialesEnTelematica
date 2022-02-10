from email.policy import default
import socket
from urllib import request
import click

@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.settimeout(10)
    request = b"GET / HTTP/1.1\r\nHost:%a\r\nConnection: close\r\n\r\n" % host
    sent    = 0
    while sent < len(request):
        sent = sent + sock.send(request[sent:])  
    # print("this is the message in bytes ----------------------------------------------------")
    # print(request)
    # print("this is the response ------------------------------------------------------------")
    
    response = b""
    try:
        while True:
            response = response + sock.recv(4096)
    except socket.timeout as e:
        print("Time out!")
    sock.close()
    print(response.decode())
    print("---------------------------End of Connection----------------------------------------")