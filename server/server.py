from urllib import response
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Response, status
from fastapi.staticfiles import StaticFiles
from external_api.recipes_api import RecipesApi 

app = FastAPI()
caching_metadata = []
caching_dreamteam = {}

@app.get('/sanity')
def sanity():
    return "sanity check"

@app.get('/recipes/{ingredient}')
def get_recipes(response: Response, ingredient, is_diary, is_gluten):
    global caching_metadata
    response.headers['Access-Control-Allow-Origin'] = "*"
    caching_metadata = RecipesApi(ingredient, is_diary, is_gluten).get_data().proccess_data()
    print (caching_metadata)
    return caching_metadata


app.mount('/', StaticFiles(directory='..\client',html = True), name='client')


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
