from packetframer import PacketFramer

import time

framer = PacketFramer(fh_read=open("/tmp/testfile", "rb"))

while True:
    print("RECV", framer.read_packet())

    time.sleep(.01)
