import socket
import sys
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

plops = [
    (b'MUL',123,23),
    (b'SOU',123,23),
    (b'DIV',123,23),
    (b'ADD',123,23),
    b'QUT',
]

try:
    # Send data
    message = b'HLO'
    print('sending "%s"' % message)
    sock.send(message)
    tram_type = sock.recv(3)
    print('got "%s"' % tram_type)
    if tram_type == b'HLO':
        for plop in plops:
            oper = plop[0]
            params = struct.pack('dd',plop[1],plop[2])
            sock.send(oper)
            sock.send(params)
            print('sent %s : ' % oper,params)
            res = struct.unpack('d',sock.recv(8))
            print('got : ',res)
    else:
        print("Error, didn't received b'HLO' as a response")

finally:
    print('closing socket')
    sock.close()