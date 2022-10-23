from urllib import response
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/sanity')
def sanity():
    return "sanity check"

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
