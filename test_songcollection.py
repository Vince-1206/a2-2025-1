"""Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection

def run_tests():
    """Test SongCollection class."""
    # Test empty SongCollection
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs

    # Test adding a new song
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)
    assert len(song_collection.songs) == 1

    # Test loading songs (create a test JSON file first)
    print("Test loading songs:")
    with open("test_songs.json", "w") as f:
        json.dump([{"title": "Song A", "artist": "Artist A", "year": 2000, "is_learned": False}], f)
    song_collection.load_songs("test_songs.json")
    print(song_collection)
    assert song_collection.songs

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.add_song(Song("Song B", "Artist B", 1990, False))
    song_collection.sort("year")
    print(song_collection)
    assert song_collection.songs[0].year == 1990

    # Test learned/unlearned counts
    print("Test learned/unlearned counts:")
    assert song_collection.get_number_of_learned_songs() == 1
    assert song_collection.get_number_of_unlearned_songs() == 2

    print("All SongCollection tests passed!")

if __name__ == "__main__":
    run_tests()