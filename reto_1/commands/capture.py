from socket import timeout
import pyshark
import click

@click.command()
def cli():
    host = 'www.eltiempo.com'
    capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)')
    print(f'host {host}')

    capture.sniff(timeout=1)
    for packet in capture.sniff_continuously(packet_count=20):
        print('just arrived: ---------- ------------------------------------')
        print(packet)
        print('end of packet content: ---------- ---------------------------')