from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', 8090))

while True:
    sentence, client_address = sock.recvfrom(1024)
    sock.sendto(sentence.decode()[::-1].encode(), client_address)
