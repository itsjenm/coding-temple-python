'''
Music Festival Playlist Organization

Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. 
Using a loop, compile these artist names into a set to create a unique lineup without duplicates.

Expected Outcome:
A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True

'''

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
is_duplicate = False

for artist in artist_names:
    if artist_names.count(artist) > 1:
        is_duplicate = True
    unique_artists.add(artist)

# Display the unique artist lineup
print(f"Unique artist lineup: {unique_artists}")
# Confirm whether there are duplicate playlists
print(f"Duplicatie playlist found: {is_duplicate}")
