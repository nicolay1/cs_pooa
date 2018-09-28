import socket
import sys
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

operations = {
    b'ADD':lambda x,y:x+y,
    b'SOU':lambda x,y:x-y,
    b'MUL':lambda x,y:x*y,
    b'DIV':lambda x,y:x/y,
}

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            tram_type = connection.recv(3)
            print('received "%s" tram' % tram_type)
            if tram_type == b'HLO':
                connection.send(b'HLO')
            elif tram_type in operations:
                params = connection.recv(16)
                nums = struct.unpack('dd',params)
                print('received params : ',nums)
                connection.send(struct.pack('d',operations[tram_type](nums[0],nums[1])))
            elif tram_type==b'QUT':
                print('client disconnected', client_address)
                break
            else:
                print('no more data from tram type :', tram_type)
            
    finally:
        # Clean up the connection
        connection.close()