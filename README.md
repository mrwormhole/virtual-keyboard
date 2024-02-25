# virtual-keyboard

I have realized I need a some sort of virtual keyboard so that I can type different alphabets(such as Thai or Turkish) faster with UK keyboard layout.

### Dependencies

- Python (>=3.11)
- GTK 4 (you can see what you need to download on [here](https://gnome.pages.gitlab.gnome.org/pygobject/getting_started.html))

Note: please do not do global system installation of poetry defined dependencies through pip, poetry already installs it!

#### Linux

```shell
poetry install
python ./keyboard.py
```

### TODOs

- [X] Solve the text area issue when text area is filled, clicking a button goes back to the start
- [ ] Design a CSS layout for buttons label size and do the layouts for thai/turkish
- [ ] Implement hotkey bindings from UK keyboard to other 2 layouts
- [ ] Write all tests for unicodes to confirm the text that was inputted have correct unicode
- [X] Port it to GTK 4
- [ ] (OPTIONAL) Release executable binaries through GH releases

