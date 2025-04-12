Unhackerman

We are given a file with the name encrypted.png. The intended solution is to look up the file header for the png file format. As per http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html the first eight bytes of a PNG file always contain these values (decimal) 137 80 78 71 13 10 26 10 if we convert that to HEX we get 89 50 4E 47 0D 0A 1A 0A (Or we just look it up on wikipedia). Now we XOR the png with the known bytes of the header:

```python
def xor_image_file(image_path, key, output_path):  
    with open(image_path, 'rb') as f:  
        image_data = f.read()  
    byte_string = bytes.fromhex(key)  
    key_bytes = byte_string  
    xor_data = bytes([b ^ k for b, k in zip(image_data, itertools.cycle(key_bytes))])  
      
    with open(output_path, 'wb') as f:  
        f.write(xor_data)  
  
input_image = "challenge.png"  
output_image = "output_challenge.png"  
key = "89 50 4E 47 0D 0A 1A 0A"  
  
xor_image_file(input_image, key, output_image)
```

If we look at the output_challenge.png in a hex editor we can see the key that was used to XOR the file which is "canyons"

If we use that key to XOR the whole challenge.png file we get the image which includes the flag.

Flag: `CTFkom{x0r_4int_th4t_h4rd}`
