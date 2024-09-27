import qiime2

from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()
static_file = StaticFiles(directory="/app/front/static", html=True)
app.mount("/app/front/static", static_file, name="static")

template = Jinja2Templates(directory="/app/front/templates")


@app.get("/", response_class=HTMLResponse)
def index():
    return template.TemplateResponse("index.html", {"request": Response})


@app.get("/qiime2")
def qiime2_version():
    return {"version": qiime2.__version__}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
