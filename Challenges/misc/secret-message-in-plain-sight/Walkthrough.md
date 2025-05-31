# Secret Message in Plain sight

1. Inspect the message (if you use deepl to translate it, it will tell you that there are sine weird chars. With google translate it will automatically cut them out)
2. If you try to delete some charecters or try to navigate with the curses and the arrow keys, you will see that at the end are somehow more chars that visible (first clue)
3. You can put the text into a binary text analyzer like: https://www.soscisurvey.de/tools/view-chars.php or https://dencode.com/string/bin to see what chars are there after the chineese ones (the chineese chars should give a hint that the challenge is using utf16)
4. The first chars is `U+FEFF` and if you look for it on google you will find articles about the invisible chars and might come across this article: https://www.gadgethacks.com/how-to/use-invisible-zero-width-characters-hide-secret-messages-plain-sight-0385009/
5. go to the linked website: https://neatnik.net/steganographr/ and get the flag

Flag: HackTWK{Th1s_15_4_53cr3t_M35534G3!}
