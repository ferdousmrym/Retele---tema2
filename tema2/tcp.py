import socket
import logging
import time

logging.basicConfig(formt = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.sock_stream, proto=socket.IPPROTO_TCP)

port = 10000
address = '0.0.0.0'
server_address = (address,port)
sock.bind(server_address)
logging.info("The server started on %s and port %d", address, port)
sock.listen(5)
while True:
    logging.info('Asteptam conexiui...')
    conexiune, address = sock.accept()
    logging.info("Handshake cu %s", address)
    time.sleep(2)
    data = conexiune.recv(1)
    logging.info('Content primit: "%s"', data)

    conexiune.close()
sock.close()

