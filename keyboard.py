import sys
from os import path
import html

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk, Gio

from characters import CHARS, find_mapped_char, char_location, BACKSPACE, ENTER, SHIFT, SPACE


class KeyboardApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mrwormhole.virtual-keyboard")
        GLib.set_application_name("Virtual Keyboard")
        style_path: str = path.abspath(path.join(path.dirname(__file__), "data", "style.css"))

        self.css_provider = Gtk.CssProvider()
        self.css_provider.load_from_path(style_path)
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.textarea: Gtk.Entry = Gtk.Entry(hexpand=True)  # Multi-line support for "↵ Enter" requires TextView+ScrollableWindow
        self.textarea.add_css_class("input-box")
        self.grid: Gtk.Grid = Gtk.Grid(row_spacing=5, column_spacing=5, focusable=False, column_homogeneous=True)

        self.current_langauge: str = "TH"
        self.enabled_shift: bool = False

    def tint(self, char: str):
        location = char_location(char)
        if location is not None:
            button = self.grid.get_child_at(location[1], location[0])
            if button.has_css_class("keyboard-activating"):
                button.remove_css_class("keyboard-activating")
            else:
                button.add_css_class("keyboard-activating")

    def on_key_released(self, event_controller: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType) -> bool:
        if keyval == Gdk.KEY_Return:
            self.tint(ENTER)
            return True

        if keyval == Gdk.KEY_BackSpace:
            self.tint(BACKSPACE)
            return True

        if keyval == Gdk.KEY_space:
            self.tint(SPACE)
            return True

        # lowercase it first so that UK mappings are used correctly
        keyval = Gdk.keyval_to_lower(keyval)
        char = chr(Gdk.keyval_to_unicode(keyval))
        mapped_char = find_mapped_char(char, self.current_langauge)
        if mapped_char != "":
            self.tint(char)
            return True
        return False

    def on_key_pressed(self, event_controller: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType) -> bool:
        if keyval == Gdk.KEY_Escape:
            self.window.close()
            return True

        if keyval == Gdk.KEY_Return:
            self.tint(ENTER)
            return True

        if keyval == Gdk.KEY_Shift_L or keyval == Gdk.KEY_Shift_R:
            if self.current_langauge.endswith("_"):
                self.current_langauge = self.current_langauge.rstrip("_")
            else:
                self.current_langauge = f"{self.current_langauge}_"
            self.enabled_shift = not self.enabled_shift
            self.generate_grid_buttons(self.current_langauge)
            return True

        cursor_position: int = self.textarea.get_position()
        if keyval == Gdk.KEY_BackSpace and cursor_position != 0:
            buff: Gtk.EntryBuffer = self.textarea.get_buffer()
            buff.delete_text(cursor_position - 1, 1)
            self.tint(BACKSPACE)
            return True

        if keyval == Gdk.KEY_space:
            buff: Gtk.EntryBuffer = self.textarea.get_buffer()
            buff.insert_text(cursor_position, " ", -1)
            self.textarea.set_position(cursor_position + 1)
            self.tint(SPACE)
            return True

        # lowercase it first so that UK mappings are used correctly
        keyval = Gdk.keyval_to_lower(keyval)
        char = chr(Gdk.keyval_to_unicode(keyval))
        mapped_char = find_mapped_char(char, self.current_langauge)
        if mapped_char != "":
            buff: Gtk.EntryBuffer = self.textarea.get_buffer()
            buff.insert_text(cursor_position, mapped_char, -1)
            self.textarea.set_position(cursor_position + 1)
            self.tint(char)
            return True

        return False

    def generate_grid_buttons(self, language: str):
        default_chars = CHARS["UK"]
        for i in range(len(default_chars)):
            for j in range(len(default_chars[i])):
                widget: Gtk.Widget | None = self.grid.get_child_at(j, i)
                if widget is not None:
                    self.grid.remove(widget)

                char = default_chars[i][j]
                markup = f"<span foreground='grey' size='125%'>{html.escape(char)}</span>"
                mapped_char = CHARS[language][i][j]
                ACTIONABLE_CHARS = [BACKSPACE, ENTER, SHIFT, SPACE]
                if mapped_char not in ACTIONABLE_CHARS:
                    # rather than using double tabs, use keybutton.py to set left text and right text
                    markup += f"\t\t<span foreground='#E0115F' size='250%'>{html.escape(mapped_char)}</span>"

                label: Gtk.Label = Gtk.Label()
                label.set_markup(markup)
                label.add_css_class("key")
                if mapped_char not in ACTIONABLE_CHARS:
                    label.set_halign(Gtk.Align.START)
                keybutton: Gtk.Button = Gtk.Button()
                keybutton.set_child(label)
                keybutton.set_can_focus(False)
                keybutton.connect("clicked", self.on_keybutton_clicked, mapped_char)
                if mapped_char == ENTER:
                    self.grid.attach(keybutton, j, i, 2, 1)
                    continue
                elif mapped_char == SHIFT:
                    if self.enabled_shift and not keybutton.has_css_class("keyboard-activating"):
                        keybutton.add_css_class("keyboard-activating")
                self.grid.attach(keybutton, j, i, 1, 1)

    def change_language(self, action: Gio.SimpleAction, param: GLib.VariantType):
        action_name: str = action.get_name()
        language: str = action_name.split("-")[1]
        self.generate_grid_buttons(language)
        self.current_langauge = language
        self.enabled_shift = False

    def on_quick_copy_button_clicked(self, _: Gtk.Button):
        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.set(self.textarea.get_text())

    def on_quick_delete_button_clicked(self, _: Gtk.Button):
        buff: Gtk.EntryBuffer = self.textarea.get_buffer()
        buff.delete_text(0, buff.get_length())

    def on_keybutton_clicked(self, _: Gtk.Button, text: str):
        if text == ENTER:
            return

        if text == SHIFT:
            if self.current_langauge.endswith("_"):
                self.current_langauge = self.current_langauge.rstrip("_")
            else:
                self.current_langauge = f"{self.current_langauge}_"
            self.enabled_shift = not self.enabled_shift
            self.generate_grid_buttons(self.current_langauge)
            return

        cursor_position: int = self.textarea.get_position()
        if text == BACKSPACE and cursor_position == 0:
            return
        if text == BACKSPACE and cursor_position != 0:
            buff: Gtk.EntryBuffer = self.textarea.get_buffer()
            buff.delete_text(cursor_position - 1, 1)
            return

        if text == SPACE:
            text = " "

        # Append text and move cursor
        buff: Gtk.EntryBuffer = self.textarea.get_buffer()
        buff.insert_text(cursor_position, text, -1)
        self.textarea.set_position(cursor_position + 1)

    def do_activate(self):
        self.window: Gtk.ApplicationWindow = Gtk.ApplicationWindow(application=self, title="Virtual Keyboard")
        self.window.set_default_size(400, 300)

        controller: Gtk.EventController = Gtk.EventControllerKey.new()
        controller.connect("key-released", self.on_key_released)
        controller.connect("key-pressed", self.on_key_pressed)
        controller.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
        self.window.add_controller(controller)

        # Create header bar
        header_bar = Gtk.HeaderBar()
        self.window.set_titlebar(header_bar)

        # Create 2 actions
        action: Gio.SimpleAction = Gio.SimpleAction.new("select-TH", None)
        action.connect("activate", self.change_language)
        self.window.add_action(action)
        action: Gio.SimpleAction = Gio.SimpleAction.new("select-TR", None)
        action.connect("activate", self.change_language)
        self.window.add_action(action)

        # Create a new menu, containing actions
        menu: Gio.Menu = Gio.Menu.new()
        menu.append("Select Thai", "win.select-TH")
        menu.append("Select Turkish", "win.select-TR")

        # Create a popover button
        popover = Gtk.PopoverMenu()
        popover.set_menu_model(menu)
        hamburger_button = Gtk.MenuButton()
        hamburger_button.set_popover(popover)
        hamburger_button.set_icon_name("open-menu-symbolic")

        quick_copy_button = Gtk.Button(focusable=False)
        quick_copy_button.connect("clicked", self.on_quick_copy_button_clicked)
        quick_copy_button.set_icon_name("edit-copy")

        quick_delete_button = Gtk.Button(focusable=False)
        quick_delete_button.connect("clicked", self.on_quick_delete_button_clicked)
        quick_delete_button.set_icon_name("edit-delete")

        # Add menu buttons to the header bar
        header_bar.pack_start(hamburger_button)
        header_bar.pack_start(quick_copy_button)
        header_bar.pack_start(quick_delete_button)

        # Vbox to hold textarea and the buttons
        container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        container.set_margin_start(20)
        container.set_margin_end(20)
        container.set_margin_top(10)
        container.set_margin_bottom(10)
        self.window.set_child(container)

        # Box to hold the textarea
        textarea_container: Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        textarea_container.append(self.textarea)
        container.append(textarea_container)

        # Grid to hold the buttons
        container.append(self.grid)

        self.generate_grid_buttons(self.current_langauge)
        self.window.present()


if __name__ == "__main__":
    app: KeyboardApp = KeyboardApp()
    exit_status: int = app.run(sys.argv)
    sys.exit(exit_status)
