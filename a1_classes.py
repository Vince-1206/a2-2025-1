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
    """Display all songs in the collection."""
    for i, song in enumerate(collection.songs, 1):
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
    """Mark a song as learned."""
    if collection.get_number_of_unlearned_songs() == 0:
        print("No more songs to learn!")
        return
    display_songs(collection)
    while True:
        try:
            song_number = int(input("Enter the number of a song to mark as learned: "))
            if song_number <= 0 or song_number > len(collection.songs):
                print("Invalid song number")
            elif collection.songs[song_number - 1].is_learned:
                print(f"You have already learned {collection.songs[song_number - 1].title}")
            else:
                collection.songs[song_number - 1].mark_learned()
                print(f"{collection.songs[song_number - 1].title} learned!")
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