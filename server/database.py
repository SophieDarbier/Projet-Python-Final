from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Artists, Albums

SQLALCHEMY_DATABASE_URL = "sqlite:///../chinook.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_artists_by_name(db, artist_name):
    return db.query(Artists).filter(Artists.Name == artist_name).all()

def get_albums_by_name(db, album_id):
    return db.query(Albums).filter(Albums.AlbumId == album_id).first()