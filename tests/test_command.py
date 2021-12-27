from msbapi.command import add_torrent_file, add_torrent_magnet


def test_add_torrent_file():
    """Test add a simple torrent file"""
    with open('big-buck-bunny.torrent', 'rb') as f:
        file = f.read()
    response = add_torrent_file(torrent_file=file)
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}


def test_add_torrent_file_with_path():
    """Test add a simple torrent file to a specific location"""
    with open('cosmos-laundromat.torrent', 'rb') as f:
        file = f.read()
    response = add_torrent_file(torrent_file=file, path='/data/client_6729/outp/test/')
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}


def test_add_torrent_magnet():
    """Test add a simple torrent with a magnet link"""
    magnet = 'magnet:?xt=urn:btih:08ada5a7a6183aae1e09d831df6748d566095a10' \
             '&dn=Sintel&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969' \
             '&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969' \
             '&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz' \
             '&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com' \
             '&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F' \
             '&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fsintel.torrent'
    response = add_torrent_magnet(torrent_magnet=magnet)
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}


def test_add_torrent_magnet_with_path():
    """Test add a simple torrent with a magnet link to specific location"""
    magnet = 'magnet:?xt=urn:btih:209c8226b299b308beaf2b9cd3fb49212dbd13ec' \
             '&dn=Tears+of+Steel&tr=udp%3A%2F%2Fexplodie.org%3A6969' \
             '&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969' \
             '&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337' \
             '&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969' \
             '&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337' \
             '&tr=wss%3A%2F%2Ftracker.btorrent.xyz' \
             '&tr=wss%3A%2F%2Ftracker.fastcast.nz' \
             '&tr=wss%3A%2F%2Ftracker.openwebtorrent.com' \
             '&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F' \
             '&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Ftears-of-steel.torrent'
    response = add_torrent_magnet(torrent_magnet=magnet, path='/data/client_6729/outp/test/')
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}
