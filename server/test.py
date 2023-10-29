from fastapi.testclient import TestClient
from server.api import app

client = TestClient(app)


def test_get_artists_by_name_good():
    response = client.get("/artists/AC/DC")
    assert response.status_code == 200


def test_get_albums_by_name_good():
    response = client.get("/albums/1")
    assert response.status_code == 200


def test_get_tracks_by_album_good():
    response = client.get("/tracks/1")
    assert response.status_code == 200


def test_get_artists_by_name_bad():
    response = client.get("/artists/Sosoydtqkuhgd")
    assert response.status_code == 404


def test_get_albums_by_name_bad():
    response = client.get("/albums/9999")
    assert response.status_code == 404


def test_get_tracks_by_album_bad():
    response = client.get("/tracks/9999")
    assert response.status_code == 404
