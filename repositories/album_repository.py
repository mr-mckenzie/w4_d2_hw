from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repo

def save(album):
    sql = f"INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    rows = run_sql(sql, values)
    id = rows[0]['id']
    album.id = id
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]

    rows = run_sql(sql, values)
    
    if rows:
        selected_album = rows[0]
        artist = artist_repo.select(selected_album['artist_id'])
        album = Album(selected_album['title'], selected_album['genre'], artist, selected_album['id'])

    return album


def select_all():  
    albums = [ ]

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id']) 
        album = Album(row['title'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums