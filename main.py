from pypresence import Presence
import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pywsjtx.extra.simple_server
import re

client_id = "1207218142099677234"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# IP_ADDRESS = '224.1.1.1'
# PORT = 5007

IP_ADDRESS = '127.0.0.1'
PORT = 2237

s = pywsjtx.extra.simple_server.SimpleServer(IP_ADDRESS, PORT, timeout=2.0)

while True:
    (pkt, addr_port) = s.rx_packet()
    if pkt is not None:
        packet = pywsjtx.WSJTXPacketClassFactory.from_udp_packet(addr_port, pkt)
        if type(packet) == pywsjtx.StatusPacket:
            frequency = packet.dial_frequency
            print(frequency)

    # Add a small delay to avoid unnecessary CPU usage
    time.sleep(0.1)
