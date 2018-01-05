from socket import *
import binascii
import struct


ip = 0b00001010000000000000000000000001          # This is ip 10.0.0.1

first_ip = ip >> 8 << 8
broadcast_ip = ip | 2**24 - 1
last_ip = broadcast_ip - 1
proto = struct.pack('!H', 0x806)
broadcast_mac = struct.pack('!6B', *[0xFF] * 6)
source_mac = struct.pack('!6B', *[0x00] * 6)

frame = broadcast_mac + source_mac + proto + struct.pack('!L', first_ip) + struct.pack('!L', last_ip)

print(first_ip)
print(last_ip)
print(broadcast_ip)

#binary_frame = int(frame, 2)

def send_eth(frame):

    s = socket(AF_PACKET, SOCK_RAW)
    # s.setsockopt(SOCK_RAW, SO_REUSEADDR, 1)
    s.bind(('lo', 0))
    s.send(frame)





# struct.pack('!L', first_ip) + struct.pack('!L', last_ip) +

send_eth(frame)