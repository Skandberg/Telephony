"""
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "calls"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("New call") % event.src_path

"""
from pycall import CallFile, Call, Application
import  encrypt
import pyrtp.pyrtp as pyrtp
import random
import socket
import time

 
""" 
start = time.time()
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main()) 
end = time.time() 

print ('time: {}' .format(end - start))
"""

def call():
    print("Enter phone number")
    phone_number=input()
    call = Call('SIP/flowroute/'+phone_number)	
    print("Type your message")
    message = input()
    print("Write your key")	
    key =int(input())
    return encrypt.encrypt(message, key)
   
    """
    action = Application('Playback', encrypt.encrypt(message, key))

    c = CallFile(call, action, spool_dir='calls')
    c.spool()
    """

    
def transfer(content):
    lowest_port = 16384         #Both these values must be even
    max_port = 32766            #Even this one... Trust me.
    destination = "1.2.3.4"
    packets = 3
    packetization = 150         

    port = (random.randint(lowest_port/2,max_port/2)*2)       #Selects our RTP port by picking a random number between half the highest port value and half the lowest, and multiplying it by 2 to always get an even number
    print("Selected Port is: " + str(port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    print("Enter destination: ")
    sock.bind((input(), 1447))


    #sequence_number = random.randint(1,9999)
    sequence_number = 54321
    #time_int = random.randint(1,9999)
    time_int = 12345

    while packets != 0:


        packets = packets - 1
        time_int = time_int + 1
        sequence_number = sequence_number + 1
        payload=content
        #payload = 'd5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'
        packet_vars = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : sequence_number, 'timestamp' : time_int, 'ssrc' : 185755418, 'payload' : payload}

        header_hex = pyrtp.GenerateRTPpacket(packet_vars)
        
        sock.sendto(bytes.fromhex(header_hex), (destination, port))
        
        time.sleep(float(packetization * 0.0001))
    sock.close()
