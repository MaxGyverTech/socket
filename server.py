import socket
import asyncio
from database.database import DB

db = DB('data.db',debug=True)
strkdict = {
    'username':'TEXT',
    'socket':'TEXT',
    'port':'TEXT',
    'adress':'TEXT'
}
db.createTable('users',strkdict)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,proto=0)
sock.bind(('', 9090))
sock.listen(10)

async def connection(conn,addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(data.upper().encode())
    conn.close()

while True:
    conn, addr = sock.accept()
    print( 'connected:', addr)

    connection(conn,addr)
    # while True:
    #     data = conn.recv(1024).decode()
    #     if not data:
    #         break
    #     conn.send(data.upper().encode())

    