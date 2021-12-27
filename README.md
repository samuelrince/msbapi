# MSBAPI

MSBAPI stands for "[my-seedbox.com](https://my-seedbox.com/) API" and it aims to **simplify the process of adding new 
torrents to your seedbox**. It is the standard brick to enable full automation of torrent downloading. You can request 
the API with a URL linking to a torrent file or a magnet link, and it will manage adding it to your (my-)seedbox(.com) 
instance.

The key features are:

* Auto add torrent to your seedbox given the .torrent file URL or a magnet link
* Manage download directories based on the type of torrent `movie`, `series`, etc.

## Requirements

This API is designed to be used with a **[my-seedbox.com](https://my-seedbox.com/) instance** running with the 
**ruTorrent frontend**.

## Installation

Use the package manager [poetry](https://python-poetry.org/docs/) to install msbapi.

```bash
poetry install
```

Use `--no-dev` flag if you do not need dev dependencies

## Usage

### Launch API server

The API server uses [uvicorn](https://www.uvicorn.org/) and [fastapi](https://fastapi.tiangolo.com/), you can launch 
with the following command.

```bash
uvicorn main:app --host=localhost --port 5000
```

### API Swagger

Once the API server is launched, the API Swagger will be available at [http://localhost:5000/docs/](http://localhost:5000/docs/)

### Launch using docker container

```bash
docker run -d \
  -p 5000:5000 \
  -e CLIENT_URL=$CLIENT_URL \
  -e BASE_PATH=$BASE_PATH \
  -e AUTH_TOKEN=$AUTH_TOKEN \
  --name msbapi \
  ghcr.io/samuelrince/msbapi
```

### Environment variables

| Paramter   | Function                                                                                                                |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| CLIENT_URL | The ruTorrent URL where you usually connect to add new torrents (e.g. https://seed20.my-seedbox.com:22000)              |
| BASE_PATH  | The path where torrents are downloaded by default (e.g. `/data/client_2000/outp/`)                                      |
| AUTH_TOKEN | The access token from ruTorrent interface. Please read the section "[How to get your access token](#accesstoken)" below |

## Tests

To launch tests run the following command.

```bash
python -m pytest tests/
```

## Additional setup steps

### <a name="accesstoken"></a> How to get your access token

To get you `ACCESS_TOKEN` you will need to log in your ruTorrent interface and the launch the Web Developer Tools from 
your browser. In the network tab look for a backend call (to `action.php` for instance) and check the request headers.
You will find an `Authorization` header that contains your `ACCESS_TOKEN` as following:

```
Authorization: Basic <ACCESS_TOKEN>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
