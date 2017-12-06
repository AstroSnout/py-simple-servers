from socket import *


sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(input('Unesi neku recenicu').encode(), ('localhost', 8090))
print(sock.recvfrom(4096)[0].decode())