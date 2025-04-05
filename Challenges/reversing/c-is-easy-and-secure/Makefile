CC = gcc
STD = -std=gnu99

SRC = main.c

all: public.elf private.elf

public.elf: $(SRC)
	$(CC) -DPUBLIC_BUILD -g $(SRC) -o $@ $(STD)

private.elf: $(SRC)
	$(CC) $(STD) -o $@ $(SRC)

clean:
	rm -f public.elf private.elf

new:
	make clean
	make all

.PHONY: all clean new
