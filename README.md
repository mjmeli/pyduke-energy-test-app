# pyduke-energy Test App

This is a quick web app designed to quickly get raw data from the Duke Energy API for debugging purposes.

It involves entering your username and password and then making various calls to the API to collect some data.

It is still a work-in-progress and may need to be adapted to provide more useful logging info in the future.

## Access

Current domain as of November 2022: http://pyduke-energy-test-app.up.railway.app/

## Development

This repo contains a devcontainer that will setup dependencies for you. If you want to install dependencies manually or use a virtualenv, you may do so using the `requirements.txt` file.

Once dependencies are setup, you can run `run_dev.sh` or the following command to start the web server on port 8000:

    uvicorn app.main:app --reload
