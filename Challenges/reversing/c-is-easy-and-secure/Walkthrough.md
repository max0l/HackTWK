# C is super easy and secure

First open it with a reversing tool like Binaryninja or Ghidra. This will show the structure of the code.

The reversing tool will show a few interesting things since the binary file has been compiled with the debug flag. You will also see that there is a Struct `User user` used, which can be overwritten. This is because there is no secure method called (`gets`) to get the string (contrary to the username which uses `fgets`). This can be easaly exploitet to overwrite the `user.is_admin`. You just have to write anything into it, since the chack `user.is_admin != 0` only checks if it's not null.

You could also use `strings` which will print the password and the username.

Username: `HackTWK`
Password: `0Lf8YdTDk4oiCfcuBHLatVy0XTckZCGQ`

To get the flag, just connect over netcat to the server and paste the Username and then the password. You have to append something at the end so `user.is_admin` will be overwritten.

Flag: `HackTWK{7H12_W42_4_S1mpl3_0v3rFLOW}`
