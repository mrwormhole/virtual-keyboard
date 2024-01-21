# virtual-keyboard

I have realized I need a some sort of virtual keyboard to continue on my private language lessons so that I can type different alphabet(อักษรไทย) faster with my latin keyboard. 
This is currently at PoC phase but I have plans to make it better with additional !reliable! C tooling and dead simple non-fancy UI.

### Dependencies

- GTK3

### How to compile

You need C compiler to compile on your platform, you also need to have GTK in your system.

#### Linux

```shell
clang -Wall -Wextra -pedantic -std=c17 keyboard.c -o keyboard `pkg-config --cflags --libs gtk+-3.0`
```

or with cmake

```shell
mkdir build && cd ./build
cmake ..
make && ./virtual-keyboard
```

### TODOs

- [ ] Solve the text area issue when text area is filled, clicking a button goes back to the start
- [ ] Complete PoC for thai to look like [this](https://www.branah.com/thai) for layout and key binding wise
- [ ] Ensure additional keyboard bindings mirror the different alphabet like in the PoC example
- [ ] Write all tests for unicodes to confirm the text that was inputted have correct unicode
- [ ] Port it to latest GTK 4.12.4
- [ ] (OPTIONAL) Release executable binaries through GH releases

