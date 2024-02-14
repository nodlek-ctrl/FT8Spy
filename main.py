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
print("Connected to Discord RPC")

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
            print("Got status packet")
            frequency = packet.dial_frequency
            # convert hertz to megahertz
            frequency = frequency/1000000
            mode = packet.mode
            dx=packet.dx_call
            RPC.update(details="Using WSJT-X", state=f"{mode} on {frequency}", large_image="logo")
            print(f"Updated presence with {mode} on {frequency} MHz")
    # supposedly can only update rich presence every 15 seconds
    time.sleep(1)
