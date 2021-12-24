from msbapi.command import add_torrent_file


def test_add_torrent_file():
    """Test add a simple torrent file"""
    with open('big-buck-bunny.torrent', 'rb') as f:
        file = f.read()
    response = add_torrent_file(torrent_file=file)
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}


def test_add_torrent_file_with_path():
    """Test add a simple torrent file"""
    with open('big-buck-bunny.torrent', 'rb') as f:
        file = f.read()
    response = add_torrent_file(torrent_file=file, path='/data/client_6729/outp/test/')
    assert response.status_code == 200
    assert response.json() == {'result': 'Success'}
