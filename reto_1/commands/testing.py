import socket
import click
@click.command()
@click.option("-h", "--host", prompt=True)
@click.option("-p", "--port", type=int, prompt=True, default=80)
def cli(host, port):
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.connect(('www.eltiempo.com', 443))

    http_get = """GET / HTTP/1.1\r
    Host: www.cnn.com/\r
    Connection: keep-alive\r
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
    Upgrade-Insecure-Requests: 1\r
    User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36\r
    Accept-Encoding: gzip, deflate, sdch\r
    Accept-Language: en-US,en;q=0.8\r\n\r\n"""

    http_get_minimum = b"""GET / HTTP/1.1\r\nHost: www.eltiempo.com\r\nConnection: close\r\n\r\n"""

    tcpSocket.sendall(http_get_minimum.encode('utf-8'))
    m = tcpSocket.recv(4096)
    decodificado = m.decode('latin-1')
    print(decodificado)
    tcpSocket.close()