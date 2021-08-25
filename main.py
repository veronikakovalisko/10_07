'''Task 1

Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. You need to get four
lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.

 '''
import asyncio
from typing import Generator

import requests
from bs4 import BeautifulSoup


async def kwadrat(x):
    print(x**2)
async def kub(x):
    print(x**3)
async def facktorial(x):
    f = 1
    for i in range(x+1):
         f *=i
    print(f)
async def action():
    await asyncio.gather(
        kwadrat(2),
        kub(2),
        facktorial(2)
    )

asyncio.run(action())

'''Task 3'''
import socket

PORT = 65434


async def hand_con(client, addr):
    loop = asyncio.get_event_loop()
    data = ''
    while data != '.':
        await loop.sock_sendall(client, (f"{addr} PONG"+data.upper().encode()))
        data = (await loop.sock_recv(client, 1024)).decode()
    await loop.sock_sendall(client, "CLOSE".encode())
    client.close()


async def ser():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', PORT))
    server.listen(9)
    server.setblocking(False)
    loop = asyncio.get_event_loop()
    while True:
        connection, client_address = await loop.sock_accept(server)
        print(f'conection from{client_address}')
        loop.create_task(hand_con(connection, client_address))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ser())

