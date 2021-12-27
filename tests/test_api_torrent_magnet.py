from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

MAGNET_LINK = 'magnet:?xt=urn:btih:c9e15763f722f23e98a29decdfae341b98d53056' \
              '&dn=Cosmos+Laundromat&tr=udp%3A%2F%2Fexplodie.org%3A6969' \
              '&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969' \
              '&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337' \
              '&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969' \
              '&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337' \
              '&tr=wss%3A%2F%2Ftracker.btorrent.xyz' \
              '&tr=wss%3A%2F%2Ftracker.fastcast.nz' \
              '&tr=wss%3A%2F%2Ftracker.openwebtorrent.com' \
              '&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F' \
              '&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fcosmos-laundromat.torrent'


def test_add_torrent_file():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_movie():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK,
        'type': 'movie'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_series():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK,
        'type': 'series'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_music():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK,
        'type': 'music'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_default():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK,
        'type': 'default'
    })
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_add_torrent_file_type_null():
    response = client.post('/add-torrent', json={
        'url': MAGNET_LINK,
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
