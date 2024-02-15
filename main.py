from pypresence import Presence
import time
import server
import wsjtx_decoder as pywsjtx # Why the hell not, much more readable

client_id = "1207218142099677234"  # This is not me leaking my discord token, it's the application id
RPC = Presence(client_id=client_id)
RPC.connect()
print("Connected to Discord RPC")

IP_ADDRESS = '127.0.0.1'
PORT = 2237

server = server.SimpleServer(IP_ADDRESS, PORT, timeout=2.0)

while True:
    (pkt, addr_port) = server.rx_packet()
    if pkt is not None: 
        packet = pywsjtx.WSJTXPacketClassFactory.from_udp_packet(addr_port, pkt)
        if type(packet) == pywsjtx.StatusPacket:
            print("Got status packet")
            frequency = packet.dial_frequency
            # Convert hz to mhz
            frequency = frequency/1000000
            mode = packet.mode
            dx = packet.dx_call #not yet implemented
            RPC.update(details="Using WSJT-X", state=f"{mode} on {frequency}", large_image="logo")
            print(f"Updated presence with {mode} on {frequency} MHz")
    # Supposedly can only update rich presence every 15 seconds; no evidence in docs so 5 it is
    time.sleep(5)
