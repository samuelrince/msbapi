import os
import urllib.parse
from typing import Optional

import requests


HEADERS = {'Authorization': f"Basic {os.getenv('AUTH_TOKEN')}"}


# def get_torrents() -> requests.Response:
#     url = os.getenv('CLIENT_URL') + '/plugins/httprpc/action.php'
#     data = 'mode=list&cmd=d.throttle_name%3D' \
#            '&cmd=d.custom%3Dchk-state' \
#            '&cmd=d.custom%3Dchk-time' \
#            '&cmd=d.custom%3Dsch_ignore' \
#            '&cmd=cat%3D%22%24t.multicall%3Dd.hash%3D%2Ct.scrape_complete%3D%2Ccat%3D%7B%23%7D%22' \
#            '&cmd=cat%3D%22%24t.multicall%3Dd.hash%3D%2Ct.scrape_incomplete%3D%2Ccat%3D%7B%23%7D%22' \
#            '&cmd=d.custom%3Dx-pushbullet' \
#            '&cmd=cat%3D%24d.views%3D' \
#            '&cmd=d.custom%3Dseedingtime' \
#            '&cmd=d.custom%3Daddtime'
#     headers = {'Authorization': f"Basic {os.getenv('AUTH_TOKEN')}"}
#     response = requests.post(url, data=data, headers=HEADERS)
#     return response


def add_torrent_file(torrent_file: bytes, path: Optional[str] = None) -> requests.Response:
    url = os.getenv('CLIENT_URL') + '/php/addtorrent.php?json=1'
    if path:
        dir_edit = urllib.parse.quote(path, safe='') if path else ''
        url += f'&dir_edit={dir_edit}'
    data = {'torrent_file': torrent_file}
    response = requests.post(url, files=data, headers=HEADERS)
    return response
