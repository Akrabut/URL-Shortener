# URL Shortener

**Gunicorn running the Flask backend and Vue.js in the frontend.**
**Uses SQLite as a database.**

## Setup

1. `cd .../or_hadad_nvidia/source_code/server` - change directory to the project server directory
2. `python3 -m venv venv` - create a virtual environment
3. `source venv/bin/activate` - activate the virtual environment for the backend
4. `python3 -m pip install -r requirements.txt` - install backend dependencies
5. `venv/bin/gunicorn --bind 0.0.0.0:5000 main:app` - start the backend in a gunicorn server (make sure port 5000 is free)
6. `cd ../client` in a new terminal instance - change directory to the vue app
7. `npm install` - install frontend dependencies
8. `npm run serve` - start the client
9. use the app from the vue domain - default is localhost:8080

* written and tested in python 3.7.5, vue 4.0.5
