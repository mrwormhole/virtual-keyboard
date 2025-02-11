# virtual-keyboard

[![Version](https://img.shields.io/github/tag/mrwormhole/virtual-keyboard.svg)](https://github.com/mrwormhole/virtual-keyboard/tags)
[![CI Build](https://github.com/mrwormhole/virtual-keyboard/actions/workflows/tests.yaml/badge.svg)](https://github.com/mrwormhole/virtual-keyboard/actions/workflows/tests.yaml)
[![License](https://img.shields.io/github/license/mrwormhole/virtual-keyboard)](https://github.com/mrwormhole/virtual-keyboard/blob/main/LICENSE)

I have realized I need some sort of virtual keyboard so that I can type different alphabets faster with UK keyboard layout.

I have been inspired by [this website](https://www.branah.com/) in my trilingual language journey.

![screenshot](screenshots/screenshot.png)

### Dependencies

- Python (>=3.13) download [here](https://www.python.org/downloads/)
- GTK (>=4) download [here](https://pygobject.gnome.org/getting_started.html)
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

Run the command below after understanding what it does

```shell
VERSION="1.0.1" PYVERSION="3.12.8" GLIBVERSION="2.39"; curl -L "https://github.com/mrwormhole/virtual-keyboard/releases/download/v${VERSION}/virtual-keyboard-py${PYVERSION}-glib${GLIBVERSION}-x86_64" -o virtual-keyboard-test && sudo mv virtual-keyboard-test /usr/local/bin/ && sudo chmod +x /usr/local/bin/virtual-keyboard-test && sudo curl -o /usr/share/applications/virtual-keyboard-test.desktop "https://raw.githubusercontent.com/mrwormhole/virtual-keyboard/main/virtual-keyboard.desktop
```

Please set the VERSION, PYVERSION and GLIBVERSION above, it will grab the binary from releases for you then rename it to `virtual-keyboard` and move to `/usr/local/bin`

Then will put the `virtual-keyboard.desktop` in `/usr/share/applications` and copy the contents of [this desktop file](https://github.com/mrwormhole/virtual-keyboard/blob/main/virtual-keyboard.desktop)

### FAQs

- Why is there an error message saying `GskMessage - Failed to realize renderer of type 'GskGLRenderer' for surface 'GdkWaylandToplevel': Failed to create EGL display`?

Just do `GSK_RENDERER=cairo ./binary` if you got the binary from the releases,  you won't have this message if you build the binary manually on your machine.

- Do you plan to add more languages?

We can consider as long as we don't break existing languages, I will not support chinese or japanese due to the complexity it brings.

- Do you plan to add support for Windows or Macos?

Absolutely no for Macos, maybe for Windows. On windows, you can still run the binary through WSL(windows subsystem for linux). I have tested locally with WSL, it works on Windows with WSL but windows support and CI are gonna cost me time/money so I am not willing to put time/money for it for now.

- Why GTK?

I use GNOME so I wanted to feel the native experience.

- Will you support GTK3?

No, please use up-to-date software.


### References

- [PyGObject Docs](https://api.pygobject.gnome.org/)
