from packetframer.globals import *

import struct
import hashlib
from reedsolo import RSCodec

class EncodeFrame:
    def __init__(self):
        self.payload = b""

    def ecc(self, data):
        if ERROR_CORRECTION > 0:
            rsc = RSCodec(ERROR_CORRECTION)
            return rsc.encode(data)
        else:
            return data

    def pad(self, data, length):
        assert len(data) <= length, "Length of data > specified length"

        if len(data) < length:
            delta = length - len(data)
            data += b"\xff" * delta

        return data

    def split_n(self, data, nth):
        return [data[i:i+nth] for i in range(0, len(data), nth)]

    def checksum(self, data):
        h = hashlib.shake_128()
        h.update(data)
        return h.digest(CHECKSUM_SIZE)

    @property
    def digest(self):
        # Pad payload to MAX_PACKET_SIZE
        payload = self.pad(self.payload, MAX_PACKET_SIZE)

        # Create checksum of payload
        digested = self.checksum(payload)

        # Length of actual payload, unpadded
        digested += struct.pack("H", len(self.payload))

        # Actual payload, padded
        digested += payload

        # Wrap entire payload in error correction
        digested = self.ecc(digested)

        return digested

if __name__ == "__main__":
    frame = EncodeFrame()
    frame.payload = b"Hello there packet boy!"
    print(frame.digest, len(frame.digest))
