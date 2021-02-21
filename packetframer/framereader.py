from packetframer.globals import *
from packetframer.exceptions import *
from packetframer.decodeframe import DecodeFrame

class FrameReader:
    def __init__(self):
        self.buffer = b""

    def feed(self, data):
        self.buffer += data

    def read_frame(self):

        buffer = self.buffer[0:]

        while len(buffer) >= 4:

            # Offset from left

            try:
                frame = DecodeFrame(buffer)

                # self.buffer = self.buffer[MAX_FRAME_SIZE:]
            except PacketError:
                # print("Packet error; offsetting buffer by one, retrying...")
                buffer = buffer[1:]

                continue

            return frame.payload

        buffer = self.buffer[0:]

        while len(buffer) >= 4:

            # Offset from right

            try:
                frame = DecodeFrame(buffer)

                # self.buffer = self.buffer[MAX_FRAME_SIZE:]
            except PacketError:
                # print("Packet error; offsetting buffer by one, retrying...")
                buffer = buffer[:-1]

                continue

            return frame.payload

        print("Failed to decode packet with offsetting")
