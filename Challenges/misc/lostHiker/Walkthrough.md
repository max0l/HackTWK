# Lost Hiker - Walkthrough

When looking at the recording as a spectrum in f.ex. audacity it looks like this:
![spectrum](spectrum.png)

The message at 800 Hz starts with `... --- ...` or `sos`  in morsecode indicating the hiker is sending on that frequency.

Isolating it gives this spectrum:

![spectrum 800 Hz isolated](spectrum800.png)

The extracted morsecode looks like this:
```
... --- ... .... .- -.-. -.- - .-- -.- ..-. ----- ..- .-. .---- ...-- .-. .- -. ....- .-.. -.-- ... .---- .....
```

which translates to: `SOSHACKTWKF0UR13RAN4LYS15`, omitting the `SOS` the flag is `HACKTWKF0UR13RAN4LYS15`
