# Exercise 8-8; Page 142; User Albums
#   Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the user's input and print the dictionary that's created.
#Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_songs=None): 
    """Return a dictionary regarding music albums"""
    album_details = {'artist': artist_name, 'title': album_title}

    if number_of_songs:
        album_details['song_amount'] = number_of_songs
    return album_details

while True:
    print("\nPlease describe an album:")
    print("(enter 'q' at any time to quit)")

    singer = input("Artist Name: ")
    if singer == 'q':
        break
    album_name = input("Album Name: ")
    if album_name == 'q':
        break
    track_number = input("Number of songs: ")
    if track_number == 'q':
        break
    elif track_number:
        int(track_number)
    else:
        track_number = False

    if track_number:
        album = make_album(singer, album_name, track_number)
    else:
        album = make_album(singer, album_name)
    
    print(album)