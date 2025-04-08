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
        self.is_learn_mode = False  # Flag to track if "learned" mode is active

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
        """Load songs and create buttons."""
        self.collection.load_songs(FILENAME)
        # Sort by title initially, or by learned if in learn mode
        if self.is_learn_mode:
            self.collection.sort("learned")
        else:
            self.collection.sort("title")
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
            on_press=lambda instance: self.toggle_song(song),  # Simplified on_press
            size_hint=(1, None),
            height=50,
            font_size=20
        )
        self.root.ids.song_box.add_widget(button)

    def update_status(self):
        """Update the top status label."""
        self.status_top = (f"To learn: {self.collection.get_number_of_unlearned_songs()}\n"
                          f"Learned: {self.collection.get_number_of_learned_songs()}")

    def toggle_song(self, song):
        print(f"Toggling song: {song.title}, current status: {song.is_learned}")
        """Toggle a song's learned status."""
        if song.is_learned:
            song.mark_unlearned()
            self.status_bottom = f"Unlearned {song.title}"
        else:
            song.mark_learned()
            self.status_bottom = f"Learned {song.title}"
        self.load_songs()  # Reload to reflect new status and sorting
        self.update_status()

    def add_song(self):
        """Add a new song from input fields."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()

        if not all([title, artist, year_text]):
            self.status_bottom = "Complete all the fields"
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
        """Sort songs by the selected key or set learn mode."""
        self.is_learn_mode = (sort_key == "learned")
        self.load_songs()  # Reload with appropriate sorting

if __name__ == '__main__':
    SongListApp().run()