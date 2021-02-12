from packetframer import PacketFramer

framer = PacketFramer(fh_write=open("/tmp/testfile", "wb"))
framer.write_packet(b"Helloooooooooooo there!")
