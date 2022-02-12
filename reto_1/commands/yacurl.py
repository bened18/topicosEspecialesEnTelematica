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
    capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp port 80')
    
    message = f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n"
    request = message.encode('utf-8')
    sent = 0

    while sent < len(request):
        sent = sent + sock.send(request[sent:])   # Send a portion of 'request', starting from 'sent' byte      
    response = b""
    print("-----------------------------------------------------------------------------packet sent---------------------------------------------------------------------------")
    
   
    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0:     # No more data received, quitting
            break
        response = response + chunk
    print("-----------------------------------------------------------------------------packet received--------------------------------------------------------------------------")
    capture.sniff(timeout=1)
    for packet in capture.sniff_continuously(packet_count=1):
        print(f"    {packet}")
    sock.close()
    
    response_decode = response.decode('latin-1')
<<<<<<< HEAD
    print(response_decode)
    print("---------------------------End of Connection----------------------------------------")
    # with open("parsing.html", "w") as file:
    #     file.write(response_decode)

            
=======

    with open("parsing.html", "w") as file:
        file.write(response_decode)
    
>>>>>>> 8a2c84d38fe3a9c8f0c008daea918fac589fe6ff
