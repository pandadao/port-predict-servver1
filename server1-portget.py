# -*- coding: utf-8 -*-

import socket
import threading 
import os
import sys, struct


def addr2bytes(addr):
    host, port = addr
    try:
        host = socket.gethostbyname(host)
    except (socket.gaierror, socket.error):
        raise ValueError("invalid host")

    try:
        port = str(port)
    except:
        ValueError("invalid port")

    return str(host), port


def main():
    HOST = "127.0.0.1"
    PORT = 30333

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        (csock, adr) = s.accept()
        #print "Client Info: ", csock, adr
        msg = csock.recv(1024)

        dhost, dport = addr2bytes(adr)
        if not dhost:
            pass
        else:
            print "The Client port is " + dport + " and IP is " + dhost
            csock.send(dport + " " + dhost)

        csock.close()

if __name__ == "__main__":
    main()