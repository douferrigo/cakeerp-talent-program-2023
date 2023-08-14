from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get('/status')
def status ():
    return JSONResponse({"Status":"It´s alive"}) 
