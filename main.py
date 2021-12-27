import uvicorn
from fastapi import FastAPI

from msbapi.api import TorrentRequest, TorrentResponse, add_new_torrent

app = FastAPI()


@app.post('/add-torrent')
def add_torrent(torrent: TorrentRequest) -> TorrentResponse:
    r = add_new_torrent(torrent)
    return r


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=5000, debug=True, reload=True)
