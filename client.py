#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread 
import sys

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print("\n"+msg)
            send_thread = Thread(target=send)
            send_thread.start()
            # msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send():  # event is passed by binders.
    """Handles sending of messages."""

    msg = input("Enter Message : ")
    print("\n[Me]"+msg)
    # my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()   
        # top.quit()    
    else:
        receive_thread = Thread(target=receive)
        receive_thread.start()


HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not HOST:
    HOST = "13.126.183.145"
if not PORT:
    PORT = 27001
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
