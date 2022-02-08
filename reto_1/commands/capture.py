import pyshark
import click

@click.command()
def cli():
    iface_name = 'eth0'

    capture = pyshark.LiveCapture(interface=iface_name, bpf_filter='80')
    capture.packets_from_tshark
    capture.sniff(timeout=10)
    print(f'capturado: {capture}') 