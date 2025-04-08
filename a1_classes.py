"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to

"""
Name: Lin Han-Wei
Date started: 2/28-3/10
GitHub URL: https://github.com/Vince-1206
"""

import csv

FILENAME = "songs.csv"


def load_songs():
    """Load songs from the CSV file into a list."""
    songs = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = int(row[2])  # Convert year to integer
                songs.append(row)
    except FileNotFoundError:
        print("File not found. Starting with an empty song list.")
    return songs


def save_songs(songs):
    """Save the current song list back to the CSV file in sorted order."""
    songs.sort(key=lambda s: (s[2], s[0]))  # Sort before saving
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(songs)
    print(f"{len(songs)} songs saved to {FILENAME}")


def display_songs(songs):
    """Display the song list, sorted by year and title with proper formatting."""
    songs.sort(key=lambda s: (s[2], s[0]))  # Sort by year, then title
    learned_count = sum(1 for song in songs if song[3] == 'l')

    for i, song in enumerate(songs, 1):
        status = "* " if song[3] == 'u' else "  "
        print(f"{i}. {status}{song[0]} - {song[1]} ({song[2]})")

    print(f"{learned_count} songs learned, {len(songs) - learned_count} songs still to learn.")


def add_song(songs):
    """Add a new song to the list after validating input."""
    print("Enter details for a new song.")
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_year("Year: ")
    songs.append([title, artist, year, 'u'])  # New songs are unlearned
    print(f"{title} by {artist} ({year}) added to song list.")


def mark_learned(songs):
    """Mark a song as learned."""
    unlearned_songs = [song for song in songs if song[3] == 'u']
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    display_songs(songs)
    while True:
        try:
            song_number = int(input("Enter the number of a song to mark as learned: "))
            if song_number <= 0:
                print("Number must be > 0.")
            elif song_number > len(songs):
                print("Invalid song number")
            elif songs[song_number - 1][3] == 'l':
                print(f"You have already learned {songs[song_number - 1][0]}")
                return
            else:
                songs[song_number - 1][3] = 'l'
                print(f"{songs[song_number - 1][0]} by {songs[song_number - 1][1]} learned!")
                return
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_string(prompt):
    """Get a non-empty string input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank.")


def get_valid_year(prompt):
    """Get a valid positive integer for the year."""
    while True:
        try:
            year = int(input(prompt))
            if year > 0:
                return year
            print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")


def main():
    """Main function to run the program."""
    print("Song List 1.0 - by Lindsay Ward")
    songs = load_songs()
    print(f"{len(songs)} songs loaded.")

    while True:
        print("\nMenu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").strip().lower()
        if choice == 'd':
            display_songs(songs)
        elif choice == 'a':
            add_song(songs)
        elif choice == 'c':
            mark_learned(songs)
        elif choice == 'q':
            save_songs(songs)
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")
if __name__ == '__main__':
    main()