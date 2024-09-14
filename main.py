from fastapi import FastAPI
from model import Db_connector
app = FastAPI()

postgres_service  = Db_connector("database.ini","postgresql")
postgres_service.db_conn()

@app.get("/")
async def index():
    
    
    
    # return 200,f"Hello  World"

@app.get("/{name}")
async def root(name):
    return 200, f"Hello {name}"