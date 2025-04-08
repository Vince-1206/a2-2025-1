
class Song:
    """Represents a song with title, artist, year, and learned status."""
    def __init__(self, title="", artist="", year=0, is_learned=False):
        """Initialize a Song with default or provided values."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def mark_learned(self):
        """Mark the song as learned."""
        self.is_learned = True

    def mark_unlearned(self):
        """Mark the song as unlearned."""
        self.is_learned = False

    def __str__(self):
        """Return a string representation of the song."""
        learned_status = "learned" if self.is_learned else "unlearned"
        return f"{self.title} by {self.artist} ({self.year}) - {learned_status}"
