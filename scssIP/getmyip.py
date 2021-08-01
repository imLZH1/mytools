import socket,struct,fcntl
def get_ip(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    a = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(n[:15],'utf-8')))[20:24])
    #return a
    l=[]
    for b in a:
        l.append(str(b))
        if l.count('.') == 3:
            break
    i = ''
    for e in l:
        i+=e
    return i
