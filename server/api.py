from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from server.database import *

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# an artist name, and display artists with the given name
@app.get("/artists/{artist_name:path}")
async def getArtists(artist_name: str, db: Session = Depends(get_db)):
    Artists = get_artists_by_name(db, artist_name)
    if Artists is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return Artists


# an artist ID, and display the corresponding album names
@app.get("/albums/{album_id}")
async def getAlbums(album_id: int, db: Session = Depends(get_db)):
    Albums = get_albums_by_name(db, album_id)
    if Albums is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return Albums


# an album ID, and display the corresponding track names
@app.get("/tracks/{album_id}")
async def getTracks(album_id: int, db: Session = Depends(get_db)):
    tracks = get_tracks_by_album(db, album_id)
    if not tracks:
        raise HTTPException(
            status_code=404, detail="Tracks not found for the specified album"
        )
    return tracks
