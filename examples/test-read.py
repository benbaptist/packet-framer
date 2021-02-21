from packetframer import PacketFramer

TEST_PATH = "/tmp/amazing_fifo"

framer = PacketFramer(
    fh_read=open(TEST_PATH, "rb")
)

while True:
    packet = framer.read_packet()

    if not packet:
        print("All done!")
        break

    print("Read", packet)
