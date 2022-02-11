import pyshark
import click

@click.command()
def cli():
    capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp port 80')
    # capture.sniff(timeout=10)
    # print(capture)
    # print('packet 3 captured', capture[3])

    for packet in capture.sniff_continuously(packet_count=2):
        print('just arrived: ---------- ------------------------------------')
        print(packet)
        print('end of packet content: ---------- ---------------------------')