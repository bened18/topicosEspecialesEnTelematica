import logging
from time import sleep
import multiprocessing as mp

import click
import socket
import ssl
import pyshark

logging.basicConfig(level=logging.DEBUG)

def capture_traffic(interface="eth0", filter='tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'):
    with pyshark.LiveCapture(interface=interface, bpf_filter=filter) as traffic:
        for packet in traffic.sniff_continuously(packet_count=2):
            print('-------------------------------------Packet Captured---------- ------------------------------------')
            print(packet)
            print('-----------------------------------End of Packet Content ---------- ---------------------------')

@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):
    
    capture_process = mp.Process(target=capture_traffic, kwargs={"filter": f'tcp port {port} and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'})
    capture_process.start()
    sleep(1)

    message = f"GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\nOrigin: https://{host}\r\nConnection: close\r\n\r\n"
    package = message.encode('utf-8')

    context = ssl.create_default_context()

    sent = 0    

    if port == 80:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Family and type of socket
        sock.connect((host, port))                               # Stableshing connection to host and port given

        while sent < len(package):
            sent = sent + sock.send(package[sent:])              # This is to asure that we are not losing sent packages
        response = b""

        while True:
            chunk = sock.recv(4096)
            if len(chunk) == 0:                                   # If no more data received, quitting
                break
            response = response + chunk

        sock.close() 
    else:
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as yacurl:
                while sent < len(package):
                    sent = sent + yacurl.send(package[sent:])
                response = b""

                while True:
                    chunk = yacurl.recv(4096)
                    if ( len(chunk) == 0 ) :
                        break
                    response = response + chunk   

    response_decode = response.decode('latin-1')

    with open("reto_1/responses/parsing.html", "w") as file:
            file.write(response_decode)

    sleep(1)
    capture_process.kill()



