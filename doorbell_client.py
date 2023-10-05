import json
import socket

def trigger_doorbell():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = json.dumps({'event':'doorbell'}).encode('utf-8')

    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

if __name__=='__main__':
    trigger_doorbell()
