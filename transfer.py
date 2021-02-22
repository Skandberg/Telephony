import asyncio
from aiortsp.rtsp.reader import RTSPReader

to_read=input()
async with RTSPReader(to_read) as reader:
	async for pkt in reader.iter_packets():
        	print('PKT', pkt.seq, pkt.pt, len(pkt))
