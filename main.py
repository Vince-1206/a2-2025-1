"""
Name: Lin Han-Wei
Date Started: 4/7/2025
Brief Project Description: Song List 2.0 with console and GUI versions
using Song and SongCollection classes.
GitHub URL: https://github.com/Vince-1206/a2-2025-1/tree/main
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from song import Song
from songcollection import SongCollection

FILENAME = "songs.json"
LEARNED_COLOR = [0, 1, 0, 1]  # Green
UNLEARNED_COLOR = [1, 0, 0, 1]  # Red

class SongListApp(App):
    """Kivy app for managing a song collection."""
    status_top = StringProperty("To learn: 0\nLearned: 0")
    status_bottom = StringProperty("Welcome to Song List 2.0")

    def __init__(self, **kwargs):
        """Initialize the app with a SongCollection."""
        super().__init__(**kwargs)
        self.collection = SongCollection()
        self.current_sort_key = "title"  # Track the current sort key

    def build(self):
        """Build the app and load songs."""
        self.title = "Song List 2.0 by Lindsay Ward"
        self.root = Builder.load_file('songlist.kv')
        self.load_songs()
        self.update_status()
        return self.root

    def on_stop(self):
        """Save songs when the app closes."""
        self.collection.save_songs(FILENAME)

    def load_songs(self):
        """Load songs and create buttons (called only at startup)."""
        self.collection.load_songs(FILENAME)
        self.collection.sort(self.current_sort_key)
        song_box = self.root.ids.song_box
        song_box.clear_widgets()
        for song in self.collection.songs:
            self.add_song_button(song)

    def add_song_button(self, song):
        """Add a button for a song."""
        learned_text = " (learned)" if song.is_learned else ""
        button = Button(
            text=f"{song.title} by {song.artist} ({song.year}){learned_text}",
            background_color=LEARNED_COLOR if song.is_learned else UNLEARNED_COLOR,
            size_hint=(1, None),
            height=50,
            font_size=20
        )
        # Bind the button to toggle_song, passing both the song and the button instance
        button.bind(on_press=lambda instance: self.toggle_song(song, instance))
        self.root.ids.song_box.add_widget(button)
        return button  # Return the button for potential future use

    def update_status(self):
        """Update the top status label."""
        self.status_top = (f"To learn: {self.collection.get_number_of_unlearned_songs()}\n"
                          f"Learned: {self.collection.get_number_of_learned_songs()}")

    def toggle_song(self, song, button):
        """Toggle a song's learned status and update the button."""
        if song.is_learned:
            song.mark_unlearned()
            button.background_color = UNLEARNED_COLOR
            button.text = f"{song.title} by {song.artist} ({song.year})"
            self.status_bottom = f"Unlearned {song.title}"
        else:
            song.mark_learned()
            button.background_color = LEARNED_COLOR
            button.text = f"{song.title} by {song.artist} ({song.year}) (learned)"
            self.status_bottom = f"Learned {song.title}"
        self.update_status()

    def add_song(self):
        """Add a new song from input fields and save it."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()

        if not all([title, artist, year_text]):
            self.status_bottom = "Complete all the SNIPPETfields."
            return

        try:
            year = int(year_text)
            if year <= 0:
                self.status_bottom = "The year must be > 0"
                return
        except ValueError:
            self.status_bottom = "Enter a valid number"
            return

        new_song = Song(title, artist, year, False)
        self.collection.add_song(new_song)
        self.add_song_button(new_song)
        self.collection.save_songs(FILENAME)  # Save to file immediately
        self.clear_inputs()
        self.status_bottom = f"Added {title}"
        self.update_status()

    def clear_inputs(self):
        """Clear all input fields and bottom status."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_bottom = ""

    def sort_songs(self, sort_key):
        """Sort songs by the selected key."""
        self.current_sort_key = sort_key
        self.collection.sort(self.current_sort_key)
        song_box = self.root.ids.song_box
        song_box.clear_widgets()
        for song in self.collection.songs:
            self.add_song_button(song)

if __name__ == '__main__':
    SongListApp().run()