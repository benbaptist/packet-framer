from packetframer import PacketFramer
from packetframer.globals import *
from builtins import input

import os

TEST_PATH = "/tmp/amazing_fifo"

if not os.path.exists(TEST_PATH):
    os.mkfifo(TEST_PATH)

print("Opening fifo at path %s" % TEST_PATH)
print("Max message length is %s bytes" % MAX_PACKET_SIZE)

framer = PacketFramer(
    fh_write=open(TEST_PATH, "wb")
)

while True:
    message = input("Input a message: ")
    if len(message) > MAX_PACKET_SIZE:
        print("Too long!")
        continue

    message = message.encode("utf-8")

    framer.write_packet(message)
