A simple, weird little packet framing system. Can be used in conjunction with a modem for radio communication, serial lines, and more.

This is the variable-length packet version. It's a failure, and doesn't work. 

# Quickstart

## Install packetframer
```
# Install dependencies
pip3 install -r https://raw.githubusercontent.com/benbaptist/packet-framer/main/requirements.txt

# Install packetframer
pip3 install https://github.com/benbaptist/packet-framer/archive/main.zip
```

## Try the example encoders
In one console, run:
```
python3 examples/test-write.py
```

and in another, run:
```
python3 examples/test-read.py
```

Magic will ensue. Clearly.

# Technical Info
Packet frames are variable in length, up to a maximum of 256 bytes. Length and syncing is determined by reading a minimum of 4 bytes, attempting to decode/verify a packet, and if it fails, attempt decode again, increasing length by one byte, or offsetting by one byte, until it succeeds.

Each packet is encapsulated with error correction, if enabled. This is the first verification step for determining if packet is valid.

Next step is to read checksum and verify following packets; if checksum does not match, discard packet and try again.
