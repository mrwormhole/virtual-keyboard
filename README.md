# virtual-keyboard

[![Version](https://img.shields.io/github/tag/mrwormhole/virtual-keyboard.svg)](https://github.com/mrwormhole/virtual-keyboard/tags)
[![CI Build](https://github.com/mrwormhole/virtual-keyboard/actions/workflows/tests.yaml/badge.svg)](https://github.com/mrwormhole/virtual-keyboard/actions/workflows/tests.yaml)
[![License](https://img.shields.io/github/license/mrwormhole/virtual-keyboard)](https://github.com/mrwormhole/virtual-keyboard/blob/main/LICENSE)

I have realized I need some sort of virtual keyboard so that I can type different alphabets faster with UK keyboard layout.

I have been inspired by [this website](https://www.branah.com/) in my trilingual language journey.

![screenshot](screenshots/screenshot.png)

### Dependencies

- Python (>=3.12) download [here](https://www.python.org/downloads/)
- GTK (>=4) download [here](https://gnome.pages.gitlab.gnome.org/pygobject/getting_started.html)
- Sarabun font download [here](https://fonts.google.com/specimen/Sarabun)

Run with python

```shell
uv sync
python ./keyboard.py
```

Or roll your own binary

```shell
uv sync --all-extras --dev
uv run pyinstaller keyboard.spec
./dist/keyboard
```

### Linux Binaries

Grab the binary from releases for your OS then rename it to `virtual-keyboard` and move to `/usr/local/bin`

Create the `virtual-keyboard.desktop` in `/usr/share/applications` and copy the contents of [this desktop file](https://github.com/mrwormhole/virtual-keyboard/blob/main/virtual-keyboard.desktop)

### FAQs

- Do you plan to add more languages?

We can consider as long as we don't break existing languages, I will not support chinese or japanese due to the complexity it brings.

- Why Python?

Safest way to touch GTK and not become a sociopath even if python binding is not feasible and has no docs. 

- Why GTK?

I use GNOME so I wanted to feel the native experience even though I hate every library GLib ecosystem produce in raw complex macro-maniac C

- Will you support GTK3 or Python 2.7?

No, please use up-to-date software

### TODOs

- [X] Design the layout for buttons with label size and color
- [X] Finish the text area input implementation with Gtk.Entry
- [X] Add sub-menu to pick target languages
- [X] Key Event presses follows target language mapping
- [X] Port it to GTK 4

### References

- [PyGObject Docs](https://amolenaar.pages.gitlab.gnome.org/pygobject-docs/index.html)