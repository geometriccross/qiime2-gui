import qiime2
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/qiime2")
def qiime2_version():
    return {"version": qiime2.__version__}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
