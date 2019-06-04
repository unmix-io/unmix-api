# unmix-api
RESTful API to extract vocals and instrumental from audio streams.
Serves the [unmix-web](https://github.com/unmix-io/unmix-web).

The API runs on Python 3.7 with [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

## Dependencies
Install all dependencies by using `pip install -r requirements.txt`.
Most important the [unmix-net](https://github.com/unmix-io/unmix-net) engine framework has to be added as package.


## Configuration
The following environment variables have to be added:
- `UNMIX_API_PORT`: Port to run the web server on
- `UNMIX_API_CONFIGURATION`: Path to the configuration file of the unmix engine instance
- `UNMIX_API_WEIGHTS`: Path to the weights file of a trained neural network model

## Endpoints
- `/dummy/<string:name>` [GET, POST, PUT, DELETE]: Dummy to check if the application runs
- `/predict/youtube` [POST]: Starts a separation of a YouTube link by passing it as "link" parameter
- `/predict/file` [POST]: Starts a separation of an audio file by passing it as "file" parameter
- `/result/<string:identifier>/<string:type>` [POST]: Returns the result of a previously predicted song

## Response
```json
{
   "identifier":"895b92e9-9f54-4c76-8e10-03b3f90c9b37",
   "controller":"YoutTube",
   "time":"20190529-105854",
   "configuration":{
      "name":"Hourglass",
      "sample_rate":44100
   },
   "result":{
      "name":"Adele - Skyfall (Lyric Video).mp4",
      "size":520,
      "vocals":"/result/895b92e9-9f54-4c76-8e10-03b3f90c9b37/vocals",
      "instrumental":"/result/895b92e9-9f54-4c76-8e10-03b3f90c9b37/instrumental",
      "response":"/result/895b92e9-9f54-4c76-8e10-03b3f90c9b37/response"
   }
}
```
The `/predict` response object contains the referring links to request the result audio files by using the `/result` endpoint.
