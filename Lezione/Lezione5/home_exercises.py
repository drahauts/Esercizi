"""
Write a function called create_playlist() that accepts a playlist name
and a variable number of song titles. The function should return a dictionary
with the playlist name and a set of songs. Call the function with different
numbers of songs to demonstrate flexibility.

    Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary,
the name of a playlist, and a boolean value indicating whether
it is liked (True or False). This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)
"""

def create_playlist(name_playlist: str, *songs: set) -> dict:
    playlist: dict = {"name" :name_playlist, "songs" : set(songs)}
    return playlist


print(create_playlist("Drake", "God's Plan", "Hotline Bling", "One Dance"))
print(create_playlist("The Beatles", "Let it Be"))
print(create_playlist("Gaming", "Song 1", "Song 2", "Song 3", "Song 4", "Song 5"))
print(create_playlist("Romantic"))



def add_like(playlist: dict, name_playlist:str, liked: bool) -> dict:
    playlist: dict[name_playlist]["liked"] = liked
    return playlist


playlist = create_playlist("Road Trip", "Song 1", "Song 2")
print(add_like(playlist, "Road Trip", liked=True))