import gi
import html

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class KeyButtonDualText(Gtk.Button):
    left_label: Gtk.Label
    right_label: Gtk.Label

    def __init__(self, left_text, right_text):
        super().__init__()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.left_label = Gtk.Label(label=left_text)
        self.left_label.set_halign(Gtk.Align.START)
        self.left_label.set_hexpand(True)
        self.left_label.add_css_class("key")
        markup = f"<span foreground='grey' size='125%'>{html.escape(left_text)}</span>"
        self.left_label.set_markup(markup)

        self.right_label = Gtk.Label(label=right_text)
        self.right_label.set_halign(Gtk.Align.END)
        self.right_label.set_hexpand(True)
        self.right_label.add_css_class("key")
        markup = f"<span foreground='#E0115F' size='250%'>{html.escape(right_text)}</span>"
        self.right_label.set_markup(markup)

        hbox.append(self.left_label)
        hbox.append(self.right_label)

        self.set_child(hbox)
        self.set_can_focus(False)


class KeyButtonSingleText(Gtk.Button):
    center_text: Gtk.Label

    def __init__(self, center_text):
        super().__init__()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.center_text = Gtk.Label(label=center_text)
        self.center_text.set_halign(Gtk.Align.CENTER)
        self.center_text.set_hexpand(True)
        self.center_text.add_css_class("key")
        markup = f"<span foreground='grey' size='125%'>{html.escape(center_text)}</span>"
        self.center_text.set_markup(markup)

        hbox.append(self.center_text)

        self.set_child(hbox)
        self.set_can_focus(False)
