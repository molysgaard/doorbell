import socket
import json
import sys
import subprocess
import datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

def play_doorbell():
    now = datetime.datetime.now()
    print(f'doorbell pressed: {now}')
    subprocess.Popen(['aplay', '-q', 'doorbell.wav'])

def main():
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        try:
            request = json.loads(data.decode('utf-8'))
        except Exception as e:
            print(f'Error: {e}', file=sys.stderr)

        if 'event' in request and request['event'] == 'doorbell':
            play_doorbell()

if __name__=='__main__':
    main()
