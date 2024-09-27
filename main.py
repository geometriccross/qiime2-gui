import qiime2
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/qiime2")
def qiime2_version():
    return {"version": qiime2.__version__}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
