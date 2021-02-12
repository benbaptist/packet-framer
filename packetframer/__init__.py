from packetframer.decodeframe import DecodeFrame
from packetframer.encodeframe import EncodeFrame
from packetframer.framereader import FrameReader

import time

class Main:
    def __init__(self):
        pass

frame_reader = FrameReader()

frame = EncodeFrame()
frame.payload = b"Hello there packet boy!"
# print(frame.digest, len(frame.digest))

frame_reader.feed(frame.digest)
frame_reader.feed(frame.digest)
frame_reader.feed(frame.digest)
frame_reader.feed(frame.digest)
frame_reader.feed(frame.digest)

while True:
    while True:
        frame = frame_reader.read_frame()

        if frame:
            print(frame.payload)
        else:
            break

    time.sleep(.01)

# print(DecodeFrame(frame.digest).payload)
