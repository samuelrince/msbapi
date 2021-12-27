from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


TORRENT_URL = 'https://webtorrent.io/torrents/big-buck-bunny.torrent'


def test_add_torrent_file():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_movie():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL,
        'type': 'movie'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_series():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL,
        'type': 'series'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_music():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL,
        'type': 'music'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_default():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL,
        'type': 'default'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_null():
    response = client.post('/add-torrent', json={
        'url': TORRENT_URL,
        'type': None
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_not_exist():
    response = client.post('/add-torrent', json={
        'url': 'https://example.com/'
    })
    assert response.status_code == 200
    assert response.json() == {'success': False}
