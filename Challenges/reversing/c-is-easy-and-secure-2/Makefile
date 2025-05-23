CC = gcc
STD = -std=gnu99
RCE = -no-pie -O0 -fno-stack-protector

SRC = main.c

all: program.elf

program.elf: $(SRC)
	$(CC) $(STD) $(RCE) -o $@ $(SRC) 

clean:
	rm -f program.elf

new:
	make clean
	make all

.PHONY: all clean new
