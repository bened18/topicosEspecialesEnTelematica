from code import interact
from ipaddress import IPv4Interface
from email.policy import default
from urllib import request
import click
import reto_1.commands.captureshark as captureshark

@click.command()
def cli():
    capture = captureshark.LiveCapture(interface='eth0')
    capture