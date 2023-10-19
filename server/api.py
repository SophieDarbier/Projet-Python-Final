from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import *

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# un nom d’artiste, et afficher les artistes comprenant le nom donné
@app.get("/artists/{artist_name:path}")
async def getArtists(artist_name : str, db: Session = Depends(get_db)):
    Artists = get_artists_by_name(db, artist_name)
    if Artists is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return Artists

# un identifiant d’artiste, et afficher les noms d’albums correspondants
@app.get("/albums/{album_id}")
async def getAlbums(album_id: int, db: Session = Depends(get_db)):
    Albums = get_albums_by_name(db, album_id)
    if Albums is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return Albums

# un identifiant d’album, et afficher les noms de pistes correspondants

#@app.get("/artists/{artist_name}")
#async def getArtists(artist_name :str, db: Session = Depends(get_db)):
#    return db.query(models.Artists).filter(artist_name).all()