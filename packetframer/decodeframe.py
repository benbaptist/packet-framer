from packetframer.globals import *
from packetframer.exceptions import *

import struct
import hashlib
from reedsolo import RSCodec

class DecodeFrame:
    def __init__(self, payload):
        if ERROR_CORRECTION > 0:
            rsc = RSCodec(ERROR_CORRECTION)

            try:
                decoded_payload = rsc.decode(payload)[0]
            except:
                raise PacketError("Corrupted packet, too many ECC errors")
        else:
            decoded_payload = payload

        checksum = decoded_payload[0:CHECKSUM_SIZE]
        packet_payload = decoded_payload[CHECKSUM_SIZE:]

        if self.checksum(packet_payload) != checksum:
            raise PacketError("Checksum did not match")

        self.payload = packet_payload

    def checksum(self, data):
        h = hashlib.shake_128()
        h.update(data)
        return h.digest(CHECKSUM_SIZE)
