from packetframer.globals import *
from packetframer.exceptions import *
from packetframer.decodeframe import DecodeFrame

class FrameReader:
    def __init__(self):
        self.buffer = b""

    def feed(self, data):
        self.buffer += data

    def read_frame(self):

        while len(self.buffer) >= MAX_FRAME_SIZE:

            try:
                frame = DecodeFrame(self.buffer[0:MAX_FRAME_SIZE])

                self.buffer = self.buffer[MAX_FRAME_SIZE:]
            except PacketError:
                print("Packet error; offsetting buffer by one, retrying...")
                self.buffer = self.buffer[1:]

                continue

            return frame.payload
