import socket
import pickle

a= 10

#Address Family AF_INET
#Requires address and port number

#SOCK_STREAM is used to create TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket.gethostname() get's current machines ip address
#1025 is the port number
s.bind((socket.gethostname(), 1025))
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")

    m={1:"Client", 2:"Server"}
    mymsg = pickle.dumps(m)
    mymsg = bytes(f'{len(mymsg):<{a}}',"utf-8") + mymsg
    clt.send(mymsg)