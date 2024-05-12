# virtual-keyboard

I have realized I need a some sort of virtual keyboard so that I can type different alphabets(such as Thai or Turkish) faster with UK keyboard layout.

![screenshot](./screenshot.png)

### Dependencies

- Python (>=3.12)
- GTK 4 (you can see what you need to download on [here](https://gnome.pages.gitlab.gnome.org/pygobject/getting_started.html))

Note: please do not do global system installation of poetry defined dependencies through pip, poetry already installs it!

#### Linux

```shell
poetry install
python ./keyboard.py
```

### TODOs

- [X] Design the layout for buttons with label size and color
- [X] Finish the text area input implementation with Gtk.Entry
- [ ] Key Event Presses on itself and maybe on other tabs too
- [ ] All tests for unicodes validity
- [X] Port it to GTK 4
- [ ] (optional) Use multi-line text area input implementation with Gtk.TextView
- [ ] (optional) Release executable binaries for linux/windows/macosx through GH releases

