A simple, weird little packet framing system. Can be used in conjunction with a modem for radio communication, serial lines, and more.

# Quickstart

## Install packetframer
```
# Install dependencies
pip3 install -r https://raw.githubusercontent.com/benbaptist/packet-framer/main/requirements.txt

# Install packetframer
pip3 install https://github.com/benbaptist/packet-framer/archive/main.zip
```

## Try the example encoders

# Technical Info
Packets are ALWAYS 64 bytes in length*. Syncing is determined by attempting to decode/verify a packet, and if it fails, attempt decode again, offsetting by one byte, until it succeeds.

Each packet is encapsulated with error correction, if enabled*. This is the first verification step for determining if packet is valid.

Next step is to read checksum and verify following packets; if checksum does not match, discard packet and try again.

> * Eventually, these things will be adjustable parameters.
