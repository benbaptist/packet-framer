CHECKSUM_SIZE = 4
ERROR_CORRECTION = 12
MAX_FRAME_SIZE = 64

# Never change this formula!
MAX_PACKET_SIZE = MAX_FRAME_SIZE - ERROR_CORRECTION - CHECKSUM_SIZE - 2
