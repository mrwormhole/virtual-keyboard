#include <stddef.h>

#include <gtk/gtk.h>

typedef struct {
    gint id;
    GtkWidget *button;
} Key;

static const char letters[18] = "QWERTYASDFGHZXCVBN";
static char single_char[2] = "A"; // Need single char as string.

// ANSI / ISO depends on the language of the keyboard.
// US English, Korean, Taiwanese, Thai, Mandarin are ANSI. Everything else is ISO, including International English and UK English
static const char* ansi_english_letters[] = {
    "`1234567890-=",
    "QWERTYUIOP[]\\",
    "ASDFGHJKL;'",
    "ZXCVBNM,./",
};

static void button_clicked(const GtkWidget *button, const void **user_data) {
    const void *button_index = g_hash_table_lookup((GHashTable *)user_data[0], button);
    const int index = *((int *)button_index);
    g_print("Button index %i\n", index);
    single_char[0] = letters[index];
    char *string = g_strdup_printf("%s%s", gtk_entry_get_text(GTK_ENTRY(user_data[1])), single_char);
    gtk_entry_set_text(GTK_ENTRY(user_data[1]), string);
    g_free(string);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    for (size_t i = 0; i < sizeof(ansi_english_letters) / sizeof(ansi_english_letters[0]); ++i) {
        printf("Element %zu: ", i);

        for (size_t j = 0; ansi_english_letters[i][j] != '\0'; ++j) {
            printf("%c ", ansi_english_letters[i][j]);
        }

        printf("\n");
    }

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Keyboard");
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 300);
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    GtkWidget *entry = gtk_entry_new();
    gtk_widget_set_hexpand(entry, TRUE);

    // Save buttons in an array.
    Key k1;
    GArray *keyboard = g_array_new(FALSE, FALSE, sizeof(Key));
    for (size_t i = 0; i < sizeof(letters) / sizeof(char); i++) {
        single_char[0] = letters[i];
        k1.id = i;
        k1.button = gtk_button_new_with_label(single_char);
        g_array_append_val(keyboard, k1);
    }

    // Hash table to look up array index values.
    Key *p1 = NULL;
    GHashTable *hash_table = g_hash_table_new(NULL, NULL);
    for (size_t i = 0; i < sizeof(letters) / sizeof(char); i++) {
        p1 = &g_array_index(keyboard, Key, i);
        g_hash_table_insert(hash_table, p1->button, &(p1->id));
    }

    void *user_data[2] = {hash_table, entry};
    GtkWidget *grid1 = gtk_grid_new();
    const int rows = 3;
    const int cols = 6;
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) {
            const size_t index = i * cols + j;
            if (index < sizeof(letters) / sizeof(char)) {
                p1 = &g_array_index(keyboard, Key, index);
                gtk_grid_attach(GTK_GRID(grid1), p1->button, j, i, 1, 1);
                g_signal_connect(p1->button, "clicked", G_CALLBACK(button_clicked), user_data);
            }
        }
    }

    GtkWidget *scroll = gtk_scrolled_window_new(NULL, NULL);
    gtk_widget_set_vexpand(scroll, TRUE);
    gtk_widget_set_hexpand(scroll, TRUE);
    gtk_container_add(GTK_CONTAINER(scroll), grid1);

    GtkWidget *expander = gtk_expander_new("Keyboard");
    gtk_widget_set_vexpand(expander, TRUE);
    gtk_widget_set_hexpand(expander, TRUE);
    gtk_container_add(GTK_CONTAINER(expander), scroll);

    GtkWidget *grid2 = gtk_grid_new();
    gtk_grid_attach(GTK_GRID(grid2), expander, 0, 0, 1, 1);
    gtk_grid_attach(GTK_GRID(grid2), entry, 0, 1, 1, 1);

    gtk_container_add(GTK_CONTAINER(window), grid2);

    gtk_widget_show_all(window);

    gtk_main();

    g_hash_table_destroy(hash_table);
    g_array_free(keyboard, TRUE);

    return 0;
}
