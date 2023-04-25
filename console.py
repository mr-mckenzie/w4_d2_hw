from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository 
import repositories.album_repository as album_repository

#delete all artists worked 
#artist_repository.delete_all()

#add new artist worked
new_artist = Artist('Mr Blobby')
artist_repository.save(new_artist)

#Select artist by id worked
mr_blobby = artist_repository.select(5)
print(mr_blobby.__dict__)

#Select all artists worked
list_of_artists = artist_repository.select_all()
for artist in list_of_artists:
    print(artist.__dict__)

#Create new album works
new_album = Album('Blobby sings The BeeGees', 'Disco', mr_blobby)
print(new_album.__dict__)
album_repository.save(new_album)

#delete all albums worked
#album_repository.delete_all()

#Selecting an album by id
album = album_repository.select(2)
print(f'My selected album is {album.__dict__}')

#select all albums worked
list_of_albums = album_repository.select_all()
for album in list_of_albums: 
    print(album.__dict__)