from packetframer.globals import *

import struct
import hashlib
from reedsolo import RSCodec

class EncodeFrame:
    def __init__(self):
        self.payload = b""

    def ecc(self, data):
        if ERROR_CORRECTION > 0:
            ecc_len = int(len(self.payload) * ERROR_CORRECTION)
            print("ecc length", ecc_len)
            rsc = RSCodec(ecc_len)
            return rsc.encode(data)
        else:
            return data

    def split_n(self, data, nth):
        return [data[i:i+nth] for i in range(0, len(data), nth)]

    def checksum(self, data):
        h = hashlib.shake_128()
        h.update(data)
        return h.digest(CHECKSUM_SIZE)

    @property
    def digest(self):
        payload = self.payload

        # Create checksum of payload
        digested = self.checksum(payload)
        digested += payload

        # Length of payload
        digested += struct.pack("B", len(payload))

        # Wrap entire payload in error correction
        digested = self.ecc(digested)

        return digested
