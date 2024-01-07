# virtual-keyboard

I have realized I need a some sort of virtual keyboard to continue on my private language lessons so that I can type different alphabet(อักษรไทย) faster with my latin keyboard. 
This is currently at PoC phase but I have plans to make it better with additional !reliable! C tooling and dead simple non-fancy UI.

### How to compile 

## Linux

```sh
gcc -Wall keyboard.c -o keyboard `pkg-config --cflags --libs gtk+-3.0`
```

### TODOs

- [] Design the android keyboard layout for Thai
- [] Solve the buffering issue in the input text area 
- [] Complete PoC for thai to look like [this](https://www.branah.com/thai) for layout and key binding wise
- [] Ensure additional keyboard bindings mirror the different alphabet like in the PoC example
- [] Write all tests for ASCII/unicodes to confirm the text that was inputted
- [] Port it to latest GTK 4.12.4
- [] (OPTIONAL) Investigate touch-screen support
- [] (OPTIONAL) Add more language scripts (korean/japanese/mandarin etc...)

