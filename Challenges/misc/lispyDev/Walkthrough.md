# lispyDev - Walkthrough

## guessing the password

Upon reading the text on Alex' page you will see some characters which are odd. These are called [thorn](https://de.wikipedia.org/wiki/%C3%9E) and are most commonly pronounced like the `th`. If you inspect the pages source code you will see comment which gives you a hint. `The password is the name of a programming language that sounds like my condition.` Focusing only on the last part `my condition` you can put together that Alex has a lisp as he seems to pronounce some `s` as `th`.

Alex also states that he/she enjoys `old, elegant languages` and that he/she particularly likes one that `have use of paranthesese`. One of the oldest languages still in use ist [Lisp](https://de.wikipedia.org/wiki/Lisp) developed in 1958. A "Hello World" program looks like this:

```
(princ "Hello World!")
(terpri)
```

Putting these two pieces of information together the password is `lisp`

## logging in
The login page has an input for the password and a button with the text `public login`. When clicking this password an alert appears stating that the password was incorrect. It will do this every time you click it. Inspecting the source code you will find a hidden button which actually calles a function to perform the password check. You need to remove the attribute so you can click it or call the function manually.

## the secret space

The secret space contains three sub pages, but only the webterminal is of interest for now. Its a simple form that sends "commands" to the backend. Available are `help`, `list`, `cat` and `download`. Running `list` reveales that two files are present (`archive.txt` and `secret.png`). `secret.png` is the interesting one.
![alt text](src/ctf/resource/public/secret_space/egarots/secret.png)
Each pixel encodes three ascii characters. One in each channel of RGB.

