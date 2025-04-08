"""..."""
"""SongCollection class for managing a list of songs."""
import json
from song import Song

class SongCollection:
    """A collection of songs."""
    def __init__(self):
        """Initialize an empty song collection."""
        self.songs = []

    def load_songs(self, filename):
        """Load songs from a JSON file."""
        try:
            with open(filename, 'r') as file:
                song_data = json.load(file)
                self.songs = [Song(song['title'], song['artist'], song['year'], song['is_learned'])
                              for song in song_data]
            print(f"Loaded {len(self.songs)} songs from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty collection.")

    def save_songs(self, filename):
        """Save songs to a JSON file."""
        song_data = [{'title': s.title, 'artist': s.artist, 'year': s.year,
                      'is_learned': s.is_learned} for s in self.songs]
        with open(filename, 'w') as file:
            json.dump(song_data, file, indent=4)
        print(f"Saved {len(self.songs)} songs to {filename}")

    def add_song(self, song):
        """Add a song to the collection."""
        self.songs.append(song)

    def get_number_of_learned_songs(self):
        """Return the number of learned songs."""
        return sum(1 for song in self.songs if song.is_learned)

    def get_number_of_unlearned_songs(self):
        """Return the number of unlearned songs."""
        return sum(1 for song in self.songs if not song.is_learned)

    def sort(self, key):
        """Sort songs by the given key."""
        if key == "title":
            self.songs.sort(key=lambda song: song.title)
        elif key == "artist":
            self.songs.sort(key=lambda song: song.artist)
        elif key == "year":
            self.songs.sort(key=lambda song: song.year)
        elif key == "learned":
            # Sort by is_learned (False first) and then by title within each group
            self.songs.sort(key=lambda song: (song.is_learned, song.title))