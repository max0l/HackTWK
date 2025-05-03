import random

a = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_")
output = "es6jt{xfuyfz6tf}ofjk9ydsuqLZI"

# The method only switches the charaters, which means the output contains the same amount of characters as the flag
random.seed(len(output))

# random with seed always produce the same numbers
shift = random.randint(1, 100)        # 71
multiplier = random.randint(1, 100)   # 10



# Reverse the obfuscation method:

# CODE:
# if multiplier % 2 == 0:
#         obfuscated = shifted[::-1]
#     else:
#         obfuscated = ''.join(a[(a.index(char) * multiplier) % len(a)] for char in shifted)

# 10 % 2 = 0, so the string should be reversed
rev = output[::-1]

# CODE:
# shifted = ''.join(a[(a.index(char) + shift) % len(a)] for char in flag)

# The code shifts the characters 71 places to the right, so we need to do the same thing but to the left
flag = ''.join(a[(a.index(char) - shift) % len(a)] for char in rev)
# Flag: CTFkom{s3ed_i5_n0t_so_r4nd0m}
print(flag)