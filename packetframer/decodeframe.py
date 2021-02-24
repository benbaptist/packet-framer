from packetframer.globals import *
from packetframer.exceptions import *

import struct
import hashlib
from reedsolo import RSCodec
from reedsolo import ReedSolomonError

class DecodeFrame:
    def __init__(self, payload):
        if ERROR_CORRECTION > 0:
            rsc = RSCodec(ERROR_CORRECTION)

            try:
                decoded_payload = rsc.decode(payload)[0]
            except ReedSolomonError:
                raise PacketError("Corrupted packet, too many ECC errors")
        else:
            decoded_payload = payload

        checksum = decoded_payload[0:CHECKSUM_SIZE]

        packet_length = struct.unpack("H",
                        decoded_payload[CHECKSUM_SIZE:CHECKSUM_SIZE + 2]
                        )[0]
        packet_payload = decoded_payload[CHECKSUM_SIZE + 2:]

        if self.checksum(packet_payload) != checksum:
            raise PacketError("Checksum did not match")

        self.payload = packet_payload[0:packet_length]

    def checksum(self, data):
        h = hashlib.shake_128()
        h.update(data)
        return h.digest(CHECKSUM_SIZE)
