#!/usr/bin/env python3
# capture.py
import pyshark
iface_name = 'eth0'

capture = pyshark.LiveCapture(interface=iface_name, bpf_filter='')
capture.packets_from_tshark
capture.sniff(timeout=10)
print(f'capturado: {capture}')