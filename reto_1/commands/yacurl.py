from email.policy import default
import socket
import click

@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # In seconds. Choose a value that makes sense to you
    sock.connect((host, port))
    message = f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n"
    print("----------------------Message to sent------------------------")
    print(message)
    request = message.encode('utf-8')
    print("----------------------Encoding Message-----------------------")
    print(request)
    print("----------------------RESPONSE------------------------------")

    sent = 0
    while sent < len(request):
        sent = sent + sock.send(request[sent:])   # Send a portion of 'request', starting from 'sent' byte
    response = b""
    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0:     # No more data received, quitting
            break
        response = response + chunk
    sock.close()
    response_decode = response.decode('latin-1')
    print(response_decode)
    print("---------------------------End of Connection----------------------------------------")
    with open("parsing.html", "w") as file:
        file.write(response_decode)

            