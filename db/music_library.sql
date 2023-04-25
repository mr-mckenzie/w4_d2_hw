DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  artist_id INT NOT NULL REFERENCES artists(id)
);

INSERT INTO artists (name) 
VALUES ('Led Zeppelin');

INSERT INTO artists (name) 
VALUES ('Angel Witch');

INSERT INTO artists (name) 
VALUES ('Iron Maiden');

INSERT INTO artists (name)
VALUES ('The Beatles');

INSERT INTO albums (title, genre, artist_id)
VALUES ('Killers', 'Metal', 3);

INSERT INTO albums (title, genre, artist_id)
VALUES ('Rubber Soul', 'Pop', 4);

INSERT INTO albums (title, genre, artist_id)
VALUES ('Angel Witch', 'Metal', 2);

INSERT INTO albums (title, genre, artist_id)
VALUES ('Led Zeppelin III', 'Rock', 1);

INSERT INTO albums (title, artist_id, genre)
VALUES ('Help!', 4, 'Pop');

INSERT INTO albums (genre, title, artist_id)
VALUES ('Rock', 'CODA', 1);