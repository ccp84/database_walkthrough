from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


# create table classes
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# create a new instance of session maker class from the database link
Session = sessionmaker(db)
# open a session by calling the session subclass
session = Session()


# create database from declarative base subclass
base.metadata.create_all(db)


# Select all from artists
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")


# select Queen from artists
# queen = session.query(Artist).filter_by(Name="Queen").first()
# print(queen.ArtistId, queen.Name, sep=" | ")


# all albums by queen
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.Title, album.ArtistId, sep=" | ")


# tracks with composer name queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.Name, track.AlbumId, track.Composer, track.UnitPrice, sep=" | ")
