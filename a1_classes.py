"""
Name: Lin Han-Wei
Date started: 2/28-3/10
GitHub URL: https://github.com/Vince-1206
"""

"""Song List 1.0 updated with classes - by Lin Han-Wei"""
from song import Song
from songcollection import SongCollection

FILENAME = "songs.json"

def display_songs(collection):
    """Display all songs with unlearned songs first, then learned, both sorted by title."""
    sorted_songs = sorted(collection.songs, key=lambda song: (song.is_learned, song.title))
    for i, song in enumerate(sorted_songs, 1):
        status = "* " if not song.is_learned else "  "
        print(f"{i}. {status}{song.title} - {song.artist} ({song.year})")
    print(f"{collection.get_number_of_learned_songs()} songs learned, "
          f"{collection.get_number_of_unlearned_songs()} songs to learn.")

def add_song(collection):
    """Add a new song to the collection."""
    print("Enter details for a new song.")
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_year("Year: ")
    collection.add_song(Song(title, artist, year, False))
    print(f"{title} by {artist} ({year}) added to song list.")


def mark_learned(collection):
    """Mark a song as learned based on displayed order."""
    if collection.get_number_of_unlearned_songs() == 0:
        print("No more songs to learn!")
        return

    # Get the same sorted list as display_songs
    sorted_songs = sorted(collection.songs, key=lambda song: (song.is_learned, song.title))
    display_songs(collection)

    while True:
        try:
            song_number = int(input("Enter the number of a song to mark as learned: "))
            if song_number <= 0 or song_number > len(sorted_songs):
                print("Invalid song number")
            elif sorted_songs[song_number - 1].is_learned:
                print(f"You have already learned {sorted_songs[song_number - 1].title}")
            else:
                sorted_songs[song_number - 1].mark_learned()
                print(f"{sorted_songs[song_number - 1].title} by {sorted_songs[song_number - 1].artist} learned")
                break
        except ValueError:
            print("Invalid input; enter a valid number.")
def get_valid_string(prompt):
    """Get a non-empty string input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be blank.")

def get_valid_year(prompt):
    """Get a valid positive year."""
    while True:
        try:
            year = int(input(prompt))
            if year > 0:
                return year
            print("Year must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")

def main():
    """Main program loop."""
    print("Song List 1.0 - by Lindsay Ward")
    collection = SongCollection()
    collection.load_songs(FILENAME)
    print(f"{len(collection.songs)} songs loaded.")

    while True:
        print("\nMenu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").strip().lower()
        if choice == 'd':
            display_songs(collection)
        elif choice == 'a':
            add_song(collection)
        elif choice == 'c':
            mark_learned(collection)
        elif choice == 'q':
            collection.save_songs(FILENAME)
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()