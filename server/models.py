from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class artists(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)

class albums(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artists.ArtistId"))

class customers(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key = True)
    Firstname = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)

# employees

class genres(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key = True)
    Name = Column(String)

# invoices

# invoice_items

class media_types(Base):
    __tablename__ = 'media_types'
    MediaTypeiId = Column(Integer, primary_key = True)
    Name = Column(String)

class playlists(Base):
    __tablename__ = 'playlists'
    PlaylistId = Column(Integer, primary_key = True)
    Name = Column(String)

class playlist_track(Base):
    __tablename__ = 'playlist_track'
    PlaylistId = Column(Integer, ForeignKey("playlists.PlaylistId"), primary_key = True)
    TrackId = Column(Integer, ForeignKey("tracks.TrackId"), primary_key = True)

class tracks(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key = True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    MediaTypeId = Column(Integer, ForeignKey("media_types.MediaTypeId"))
    GenreId = Column(Integer, ForeignKey("genres.GenreId"))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Integer)