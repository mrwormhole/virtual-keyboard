import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

CHARACTERS: dict[str, list[list[str]]] = {
    "UK": [
        ["1", "2", "3", "4", "5"],
        ["q", "w", "e", "r", "t"],
        ["ก", "s", "d", "f", "g", "g"],
        ["z", "x", "c", "v", "b"],
    ],
    "TH": [],
    "TR": [],
}


class KeyboardApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mrwormhole.virtual-keyboard")
        GLib.set_application_name("Virtual Keyboard")
        self.textarea: Gtk.Entry = Gtk.Entry(hexpand=True)

    def do_activate(self):
        window: Gtk.ApplicationWindow = Gtk.ApplicationWindow(application=self, title="Virtual Keyboard")
        window.set_default_size(400, 300)

        # Create a vertical box to hold textarea and the buttons
        container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        container.set_margin_start(20)
        container.set_margin_end(20)
        container.set_margin_top(10)
        container.set_margin_bottom(10)
        window.set_child(container)

        # Create a box to hold the textarea
        textarea_container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        textarea_container.append(self.textarea)
        container.append(textarea_container)

        # Create a grid to hold the buttons
        grid: Gtk.Grid = Gtk.Grid(row_spacing=5, column_spacing=5, focusable=False)
        container.append(grid)
        """
        we should support these characters below first
        // https://www.branah.com/thai
        // https://www.branah.com/turkish
        static const char* ansi_english_letters[] = {
            "`1234567890-=",
            "QWERTYUIOP[]\\",
            "ASDFGHJKL;'",
            "ZXCVBNM,./",
        };
        """

        # Create buttons for each character
        characters_uk = CHARACTERS["UK"]
        for i in range(len(characters_uk)):
            for j in range(len(characters_uk[i])):
                button: Gtk.Button = Gtk.Button(label=characters_uk[i][j])
                button.connect("clicked", self.on_button_clicked, characters_uk[i][j])
                grid.attach(button, j, i, 1, 1)

        window.present()

    def on_button_clicked(self, button: Gtk.Button, character: str):
        # current_text = self.textarea.get_text() # stubs don't show up, FFS
        # self.textarea.set_text(current_text + character)

        # Get the current position of the cursor
        cursor_position: int = self.textarea.get_position()
        buff: Gtk.EntryBuffer = self.textarea.get_buffer()
        buff.insert_text(cursor_position, character, -1)
        self.textarea.grab_focus()


app: KeyboardApp = KeyboardApp()
exit_status: int = app.run(sys.argv)
sys.exit(exit_status)
