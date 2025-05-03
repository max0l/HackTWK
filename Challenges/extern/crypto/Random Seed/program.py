import random

a = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_")

def obfuscate(flag, shift, multiplier):
    shifted = ''.join(a[(a.index(char) + shift) % len(a)] for char in flag)
    
    if multiplier % 2 == 0:
        obfuscated = shifted[::-1]
    else:
        obfuscated = ''.join(a[(a.index(char) * multiplier) % len(a)] for char in shifted)
    
    return obfuscated

flag = "CTFkom{s3ed_i5_n0t_so_r4nd0m}"
random.seed(len(flag))

shift = random.randint(1, 100)
multiplier = random.randint(1, 100)

obfuscated = obfuscate(flag, shift, multiplier)
print(obfuscated)

# Output:
# es6jt{xfuyfz6tf}ofjk9ydsuqLZI