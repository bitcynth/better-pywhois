import socket

BUFFER_SIZE = 1024

def whois_raw(server, query, port=43):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((server, port))
    s.send('{}\r\n'.format(query).encode('utf-8'))
    result = ''
    tmp = b''
    while True:
        tmp = s.recv(BUFFER_SIZE)
        result += tmp.decode('utf-8')
        if len(tmp) == 0:
            break
    return result