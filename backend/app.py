from fastapi import FastAPI,Request
import uvicorn
import os, sys
from fastapi.templating import Jinja2Templates
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
app=FastAPI()


templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
templates=Jinja2Templates(directory=templates_dir)

@app.get("/")
async def login_page(resquest:Request):
    return templates.TemplateResponse("login.html",{"request":resquest})

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0', port=8002, workers=1)



