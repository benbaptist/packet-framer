from packetframer.globals import *
from packetframer.exceptions import *

import struct
import hashlib
from reedsolo import RSCodec
from reedsolo import ReedSolomonError

class DecodeFrame:
    def __init__(self, payload):
        if ERROR_CORRECTION > 0:
            print(len(payload))
            ecc_len = int(len(payload) * ERROR_CORRECTION)
            rsc = RSCodec(ecc_len)

            print("ecc length", ecc_len)

            try:
                decoded_payload = rsc.decode(payload)[0]
            except ReedSolomonError:
                print("Too many ECC errors")
                raise PacketError("Corrupted packet, too many ECC errors")
        else:
            decoded_payload = payload

        checksum = decoded_payload[0:CHECKSUM_SIZE]

        packet_payload_length = \
            struct.unpack("B", decoded_payload[CHECKSUM_SIZE:1])

        packet_payload = decoded_payload[CHECKSUM_SIZE + 1:]

        if self.checksum(packet_payload) != checksum:
            print("Checksum did not match")
            raise PacketError("Checksum did not match")

        # Eliminate padding, if added
        packet_payload = packet_payload[0:packet_payload_length]

        self.payload = packet_payload

    def checksum(self, data):
        h = hashlib.shake_128()
        h.update(data)
        return h.digest(CHECKSUM_SIZE)
