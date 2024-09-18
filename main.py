from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    firstname: str
    lastname: str
    nickname: str
    api_key: str

user1 = User(firstname='John', lastname='Doe', nickname='@Faang', api_key='test')

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "user": user1})

