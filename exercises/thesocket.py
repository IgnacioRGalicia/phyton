import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# making a socket, that goes through internet and is a series a characters one after another
mysock.connect(('data.pr4e.org', 80))
# is making a phone call to data.pr4e.org as a phone number and 80 as an extension

cmd ='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(300)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()