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
VALUES ('The Beatles')