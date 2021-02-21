from packetframer.decodeframe import DecodeFrame
from packetframer.encodeframe import EncodeFrame

from packetframer.globals import *
from packetframer.exceptions import *
from packetframer.framereader import FrameReader

class PacketFramer:
    def __init__(self,
                 fh_read=None,
                 fh_write=None,
                 sh=None,
                 max_frame_size=64,
                 error_correction=12,
                 checksum_size=4):
        # File descriptor
        self.fh_read = fh_read
        self.fh_write = fh_write
        # Socket
        self.sh = sh

        self.frame_reader = FrameReader()

    def read_bytes(self, i):
        if self.fh_read:
            return self.fh_read.read(i)
        elif self.sh:
            return self.sh.recv(i)

    def write_bytes(self, data):
        if self.fh_write:
            self.fh_write.write(data)
            self.fh_write.flush()
        elif self.sh:
            self.sh.write(data)

    def read_packet(self):
        read_len = 4
        payload = b""

        while True:
            raw = self.read_bytes(read_len)

            print(read_len)

            if len(raw) == 0:
                return

            payload += raw

            self.frame_reader.feed(payload)

            frame = self.frame_reader.read_frame()

            if frame:
                return frame

            if read_len < 256:
                read_len += 1

    def write_packet(self, data):
        frame = EncodeFrame()
        frame.payload = data
        self.write_bytes(frame.digest)

# from packetframer.framereader import FrameReader
#
#
# import time
#
# class Main:
#     def __init__(self):
#         pass
#
# frame_reader = FrameReader()
# frame_reader.feed(b"\x00" * 20)
#
# frame = EncodeFrame()
# frame.payload = b"Hello there packet boy!"
# # print(frame.digest, len(frame.digest))
#
# frame_reader.feed(frame.digest)
# frame_reader.feed(frame.digest)
# frame_reader.feed(frame.digest)
# frame_reader.feed(frame.digest)
# frame_reader.feed(frame.digest)
#
# while True:
#     while True:
#         frame = frame_reader.read_frame()
#
#         if frame:
#             print(frame.payload)
#         else:
#             break
#
#     time.sleep(.01)
#
# # print(DecodeFrame(frame.digest).payload)
