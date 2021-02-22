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

import aiohttp
import asyncio 
import time
 
print("Enter url")
url= input()
async def getapge(session, url):
	async with session.get(url,timeout=5) as resp: 
		print(await resp.text()) 
async def main(): 
	async with aiohttp.ClientSession() as session: 
		await getapge(session, url) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
start = time.time()
 
loop = asyncio.get_event_loop()
loop.run_until_complplete(main()) 
end = time.time() 

print ('time: {}' .format(end - start))

def startup():
	print("1> start")
	print("2> exit")
	n=input()
	if n== '1':
		main_menu()
	elif n == '2':
		return
	else:
		print("please enter valid variant")
def main_menu():
	print("1> call")
	print("2> listen")
	print("3> configure")
	n=input()
	if n=='1':
		call()
#	else if n == '2':
#		listen()
	#else if n == '3':
	else:
                print("please enter valid variant")
def call():
	print("Enter phone number")
	phone_number=input()
	call = Call('SIP/flowroute/'+phone_number)
	
	print("Type your message")
	message = input()
	print("Write your key")	
	key =int(input())	
	action = Application('Playback', encrypt.encrypt(message, key))

	c = CallFile(call, action, spool_dir='calls')
	c.spool()


while True:
	startup()	
"""
call = Call('SIP/flowroute/18882223333')

action = Application('Playback', 'hello-world')

c = CallFile(call, action, spool_dir='calls')
c.spool()
"""
