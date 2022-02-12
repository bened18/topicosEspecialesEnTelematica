import socket
import click
@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                 
    sock.connect((host, port))                       
    
    message = f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n"
    request = message.encode('utf-8')
    sent = 0

    while sent < len(request):
        sent = sent + sock.send(request[sent:])   # This is to asure that we are not losing sent packages
    response = b""

    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0: # If no more data received, quitting
            break
        response = response + chunk

    response_decode = response.decode('latin-1') 
    
    sock.close()          

    print(response_decode)
    