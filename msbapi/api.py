import os
import requests
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from msbapi.command import add_torrent_file, add_torrent_magnet


class TorrentTypes(str, Enum):
    default = 'default'
    movie = 'movie'
    series = 'series'
    music = 'music'


class TorrentRequest(BaseModel):
    url: str
    type: Optional[TorrentTypes] = None

    class Config:
        use_enum_values = True


class TorrentResponse(BaseModel):
    success: bool


def download_path(torrent_type: Optional[str] = None) -> str:
    if torrent_type == TorrentTypes.movie:
        return os.path.join(os.getenv('BASE_PATH'), 'Plex', 'Films')
    elif torrent_type == TorrentTypes.series:
        return os.path.join(os.getenv('BASE_PATH'), 'Plex', 'Series')
    elif torrent_type == TorrentTypes.music:
        return os.path.join(os.getenv('BASE_PATH'), 'music')
    elif torrent_type == TorrentTypes.default:
        return os.getenv('BASE_PATH')
    else:
        return os.getenv('BASE_PATH')


def download_torrent_file(url: str) -> Optional[bytes]:
    response = requests.get(url)
    if response.ok:
        return response.content


def rt_response_success(response: requests.Response) -> bool:
    if response.ok:
        return response.json() == {'result': 'Success'}
    return False


def add_new_torrent(torrent: TorrentRequest) -> TorrentResponse:
    dl_path = download_path(torrent.type)

    # .torrent file to download and send
    if torrent.url.startswith('http'):
        file = download_torrent_file(torrent.url)
        if file:
            rutorrent_response = add_torrent_file(torrent_file=file, path=dl_path)
            if rt_response_success(rutorrent_response):
                return TorrentResponse(success=True)

    # magnet link to send
    elif torrent.url.startswith('magnet'):
        rutorrent_response = add_torrent_magnet(torrent_magnet=torrent.url, path=dl_path)
        if rt_response_success(rutorrent_response):
            return TorrentResponse(success=True)

    return TorrentResponse(success=False)
