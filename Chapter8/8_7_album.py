# Exercise 8-7; Page 142; Album
#   Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title
# It should return a dictionary containing these two pieces of information.
# Use the fuction to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album's dictionary.
# Make at least one new function call that includes the number of songs on an album.


def make_album(artist_name, album_title, number_of_songs=None): # Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
    """Return a dictionary regarding music albums"""
    album_details = {'artist': artist_name, 'title': album_title}

    # If the calling line includes a value for the number of songs, add that value to the album's dictionary.
    if number_of_songs:
        album_details['song_amount'] = number_of_songs
    return album_details

#2 different ways 

#Output 1
album = make_album('sublime', 'self titled')
print(album)
album = make_album('mac miller', 'swimming')
print(album)
album = make_album('brand new', 'the devil and god are raging inside me')
print(album)
# Make at least one new function call that includes the number of songs on an album.
album = make_album('taking back sunday', 'tell all your friends', 10)
print(album)

#Output 2
album_1 = make_album('sublime', 'self titled')
album_2 = make_album('mac miller', 'swimming')
album_3 = make_album('brand new', 'the devil and god are raging inside me')
# Make at least one new function call that includes the number of songs on an album.
album_4 = make_album('taking back sunday', 'tell all your friends', 10)
print(album_1)
print(album_2)
print(album_3)
print(album_4)