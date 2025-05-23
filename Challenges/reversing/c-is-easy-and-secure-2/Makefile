CC = gcc
STD = -std=gnu99
RCE = -no-pie -O0 -fno-stack-protector

SRC = main.c

all: public.elf private.elf

public.elf: $(SRC)
	$(CC) -DPUBLIC_BUILD -g $(SRC) $(RCE) -o $@ $(STD)

private.elf: $(SRC)
	$(CC) $(STD) $(RCE) -o $@ $(SRC) 

clean:
	rm -f public.elf private.elf

new:
	make clean
	make all

.PHONY: all clean new
