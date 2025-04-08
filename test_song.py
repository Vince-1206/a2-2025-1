"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert default_song.is_learned is False

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    # TODO: Write tests to show this initialisation works

    # TODO: Add more tests, as appropriate, for each method


run_tests()
