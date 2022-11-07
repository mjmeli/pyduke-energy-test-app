# pyduke-energy Test App

This is a quick web app designed to quickly get raw data from the Duke Energy API for debugging purposes.

It involves entering your username and password and then making various calls to the API to collect some data.

It is still a work-in-progress and may need to be adapted to provide more useful logging info in the future.

## Development

This repo contains a devcontainer that will setup dependencies for you. After that, you can run `run_dev.sh` or the following command to start the web server on port 8000:

    uvicorn app.main:app --reload
