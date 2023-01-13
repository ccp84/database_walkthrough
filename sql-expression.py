from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


# connect to database
db = create_engine("postgresql:///chinook")


meta = MetaData(db)


# create tables
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)


album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)


track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


with db.connect() as connection:
    # select all from artist table
    # query = artist_table.select()

    # select name column from artist table
    # query = artist_table.select().with_only_columns([artist_table.c.Name])

    # find queen from artist table
    # query = artist_table.select().where(artist_table.c.Name == "Queen")

    # select from tracks where composer is queen
    query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(query)
    for result in results:
        print(result)
