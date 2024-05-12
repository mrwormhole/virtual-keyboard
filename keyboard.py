import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk

from characters import CHARACTERS


class KeyboardApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mrwormhole.virtual-keyboard")
        GLib.set_application_name("Virtual Keyboard")
        self.textarea: Gtk.Entry = Gtk.Entry(hexpand=True)  # Multi-line support for "↵ Enter" requires TextView

    def do_activate(self):
        window: Gtk.ApplicationWindow = Gtk.ApplicationWindow(application=self, title="Virtual Keyboard")
        window.set_default_size(400, 300)

        # event_controller_key: Gtk.EventController = Gtk.EventControllerKey.new()
        # event_controller_key.connect("key-pressed", self.on_key_pressed)
        # window.add_controller(event_controller_key)
        #self.textarea.add_controller(event_controller_key)

        # Vbox to hold textarea and the buttons
        container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        container.set_margin_start(20)
        container.set_margin_end(20)
        container.set_margin_top(10)
        container.set_margin_bottom(10)
        window.set_child(container)

        # Box to hold the textarea
        textarea_container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        textarea_container.append(self.textarea)
        container.append(textarea_container)

        # Grid to hold the buttons
        grid: Gtk.Grid = Gtk.Grid(row_spacing=5, column_spacing=5, focusable=False)
        container.append(grid)

        default_chars = CHARACTERS["UK"]
        for i in range(len(default_chars)):
            for j in range(len(default_chars[i])):
                label: Gtk.Label = Gtk.Label(label=default_chars[i][j])

                char = default_chars[i][j]
                markup = f"<span foreground='grey' size='125%'>{char}</span>"
                special_char = CHARACTERS["TH"][i][j]
                if char != special_char:
                    special_markup = f"    <span foreground='#E0115F' size='250%'> {special_char}</span>"
                    markup += special_markup

                label.set_markup(markup)
                button: Gtk.Button = Gtk.Button()
                button.set_child(label)
                button.set_can_focus(False)
                button.connect("clicked", self.on_button_clicked, default_chars[i][j])
                if default_chars[i][j] == "↵ Enter":
                    grid.attach(button, j, i, 2, 1)
                    continue
                grid.attach(button, j, i, 1, 1)
        window.present()

    def on_button_clicked(self, button: Gtk.Button, text: str):
        # Avoid commands to be appended to text
        if text == "↵ Enter" or text == "⇧":
            return

        cursor_position: int = self.textarea.get_position()
        if text == "← Backspace":
            buff: Gtk.EntryBuffer = self.textarea.get_buffer()
            buff.delete_text(cursor_position-1, -1)
            return

        if text == "Space":
            text = " "

        # Append text and move cursor
        buff: Gtk.EntryBuffer = self.textarea.get_buffer()
        buff.insert_text(cursor_position, text, -1)
        self.textarea.set_position(cursor_position + 1)

    # def on_key_pressed(self, event_controller: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType):
    #     print(f"{type(event_controller)} {type(keyval)} {type(keycode)} {type(state)}")
    #     print("Key pressed: " + str(keycode) + " " + str(keyval) + " " + Gdk.keyval_name(keyval))


if __name__ == "__main__":
    app: KeyboardApp = KeyboardApp()
    exit_status: int = app.run(sys.argv)
    sys.exit(exit_status)
