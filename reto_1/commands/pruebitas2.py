import logging
from time import sleep
import multiprocessing as mp

import click
import socket
import pyshark
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.DEBUG)

def capture_traffic(interface="eth0", filter='tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'):
    with pyshark.LiveCapture(interface=interface, bpf_filter=filter) as traffic:
        # packets = traffic.sniff_continuously(packet_count=2)
        # packets = traffic.sniff_continuously()
        for packet in traffic.sniff_continuously(packet_count=2):
            print('--------------------------------------just arrived: ---------- ------------------------------------')
            print(packet)
            print('-----------------------------------end of packet content: ---------- ---------------------------')


@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):
    capture_process = mp.Process(target=capture_traffic)
    capture_process.start()

    sleep(1)
    if port == 80:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Family and type of socket
        sock.settimeout(10)                                      # Time that socket will we alive
        sock.connect((host, port))                               # Stableshing connection to host and port given

        message = f"GET / HTTP/1.1\r\nHost:{host}\r\nAccept: text/html\r\nConnection: close\r\n\r\n"
        request = message.encode('utf-8')
        sent = 0

        while sent < len(request):
            sent = sent + sock.send(request[sent:])              # This is to asure that we are not losing sent packages
        response = b""

        while True:
            chunk = sock.recv(4096)
            if len(chunk) == 0:                                   # If no more data received, quitting
                break
            response = response + chunk

        sock.close()                                               # Connection closed

    response_decode = response.decode('latin-1')               # We decode the response from bytes to latin-1


    with open("reto_1/responses/parsing.html", "w") as file:
        file.write(response_decode)


    with open("reto_1/responses/parsing.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        soup_string = str(soup)


    for img in soup.find_all("img"):
        with open("reto_1/responses/imagenes.doc", "w") as i:
            i.write(img.get("src"))

    with open("reto_1/responses/parsing_soup.html", "w") as f:
        f.write(soup_string)

    sleep(1)
    capture_process.kill()