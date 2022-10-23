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

@app.get('/recipes')
def get_recipes(response: Response, ingredient ="cheese", is_diary=False, is_gluten=False):
    global caching_metadata
    response.headers['Access-Control-Allow-Origin'] = "*"
    print ("hi")
    caching_metadata = RecipesApi(ingredient= "cheese").get_data().proccess_data()
    return caching_metadata



# @app.get('/dreamTeam')
# def get_dream_team():
#     global caching_dreamteam
#     return list(caching_dreamteam.values())


# @app.post('/dreamTeam')
# def post_dream_team(data: Player, response: Response):
#     global caching_dreamteam
#     caching_dreamteam[data.id] = data
#     response.status_code = status.HTTP_201_CREATED
#     return data


# @app.delete('/dreamTeam/{id}')
# def delete_dream_team(id, response: Response):
#     global caching_dreamteam
#     caching_dreamteam.pop(int(id))
#     response.status_code= status.HTTP_204_NO_CONTENT


app.mount('/', StaticFiles(directory='..\client',html = True), name='client')


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
