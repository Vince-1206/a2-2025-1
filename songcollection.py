"""..."""
"""SongCollection class for managing a list of songs."""
import json
from song import Song

class SongCollection:
    """Manages a collection of Song objects."""
    def __init__(self):
        """Initialize an empty song list."""
        self.songs = []

    def add_song(self, song):
        """Add a Song object to the collection."""
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Return the number of unlearned songs."""
        return sum(1 for song in self.songs if not song.is_learned)

    def get_number_of_learned_songs(self):
        """Return the number of learned songs."""
        return sum(1 for song in self.songs if song.is_learned)

    def load_songs(self, filename):
        """Load songs from a JSON file."""
        try:
            with open(filename, 'r') as file:
                song_data = json.load(file)
                self.songs = [Song(s['title'], s['artist'], s['year'], s['is_learned'])
                              for s in song_data]
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty collection.")

    def save_songs(self, filename):
        """Save songs to a JSON file."""
        song_data = [{'title': s.title, 'artist': s.artist, 'year': s.year,
                      'is_learned': s.is_learned} for s in self.songs]
        with open(filename, 'w') as file:
            json.dump(song_data, file, indent=4)
        print(f"Saved {len(self.songs)} songs to {filename}")

    def sort(self, key):
        """Sort songs by the given key, then by title."""
        self.songs.sort(key=lambda s: (getattr(s, key), s.title))

    def __str__(self):
        """Return a string representation of the collection."""
        return "\n".join(str(song) for song in self.songs)