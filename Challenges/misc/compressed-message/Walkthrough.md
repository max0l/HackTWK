# Why are you not using normal Compression?

1. You need to guess that the Number behind each letter is suppose to be the amout of it (Run Length Encoding)
2. You can use online tools like this https://www.dcode.fr/rle-compression to decode it (decompressed.txt)
3. Now you need to replace all A with 0 and all B with 1 and you got binary (binary.txt)
4. Now with the biary you can get Text out of it (do not use  https://www.rapidtables.com/convert/number/binary-to-ascii.html, use https://dencode.com/string/bin instead) because if there is no spacing between 8 bits it will not work (brainfuck.txt) 
5. The text is a brainfuck code
6. Run it and you will get the flag


Flag: HackTWK{G3t_A_B3TT3R_1nt3n3t_plan}
