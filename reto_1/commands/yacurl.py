from email.policy import default
import socket
import pyshark
import click

@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # In seconds. Choose a value that makes sense to you
    sock.connect((host, port))
    capture = pyshark.LiveCapture(interface='eth0')
    
    message = f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n"
    request = message.encode('utf-8')
    sent = 0

    while sent < len(request):
        sent = sent + sock.send(request[sent:])   # Send a portion of 'request', starting from 'sent' byte      
    response = b""
    print("toy aqui")
    print(capture)
    # for packet in capture.sniff_continuously(packet_count=1):
    #     print('---------------------------------new packet just sent--------------------------------------')
    #     print(packet)
    #     print('---------------------------------end of sent packet content--------------------------------')

    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0:     # No more data received, quitting
            break
        response = response + chunk
    sock.close()
    print(capture)

    # for packet in capture.sniff_continuously(packet_count=1):
    #     print('---------------------------------new packet just received-----------------------------------')
    #     print(packet)
    #     print('---------------------------------end of received packet content-----------------------------')
    
    response_decode = response.decode('latin-1')

    with open("parsing.html", "w") as file:
        file.write(response_decode)

    