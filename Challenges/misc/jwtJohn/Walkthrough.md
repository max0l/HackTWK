# grandpa john's secret cake recipe - walktrough

JWTs are used to identify the if a user is a public user or grandpa/admin. The `user` claim of the JWT needs to be set to `grandpa` in order to access the restricted space. Based on the videos played on the public page it can be deduced, that the key used to sign the tokens is `baking`.

Using a tool like [https://10015.io/tools/jwt-encoder-decoder](https://10015.io/tools/jwt-encoder-decoder) a JWT with the needed claims can be created and signed. Setting the `hacktwk_auth` cookie to the new JWT and reloading the website now opens the admin page containing a link to the secret recipe.

The link downloads a file called `recipe.zip` which is password protected. A tool like [John The Ripper](https://github.com/openwall/john) can be used to crack the password.

Extracting the hashed password:

```sh
zip2john recipe.zip > hash.txt
```

Cracking the password using a wordlist (here [rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)):

```sh
john --format=pkzip --wordlist=/path/to/rockyou.txt hash.txt
```

This results in the password `glados`.

After extracting the file, the flag (`Hacktwk{THE3_C4K3_15_4_L13}`) is stored in the `flag.txt` file.
