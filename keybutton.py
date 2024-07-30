import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class KeyButton(Gtk.Button):
    def __init__(self, left_text, right_text):
        super().__init__()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        left_label = Gtk.Label(label=left_text)
        left_label.set_halign(Gtk.Align.START)
        left_label.set_hexpand(True)

        right_label = Gtk.Label(label=right_text)
        right_label.set_halign(Gtk.Align.END)
        right_label.set_hexpand(True)

        hbox.append(left_label)
        hbox.append(right_label)

        self.set_child(hbox)