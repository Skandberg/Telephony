import selectors
import socket


host = '127.0.0.1'  
port = 65432   

sel = selectors.DefaultSelector()
# ...
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    events = sel.select(timeout=None)
    data = conn.recv(1024)
    if not data: break
    action = Application('Playback', data)

    c = CallFile(call, action, spool_dir='calls')
    c.spool()
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)