from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .library.client import get_data
from pyduke_energy.errors import DukeEnergyError

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """ The only page """
    return templates.TemplateResponse("index.html", { "request": request })

@app.get("/data", response_class=JSONResponse)
async def data(email: str, password: str, timezone: str):
    """ Retrieve data for email/password """
    try:
        resp = await get_data(email, password, timezone)
    except DukeEnergyError as err:
        resp = "ERROR: " + str(err)
    return { "data": resp }
