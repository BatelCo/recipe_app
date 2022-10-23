from statistics import mean
from .api import Api

class RecipesApi(Api):

    def __init__(self, ingredient):
        self.url = f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}"
        super().__init__(self.url)
        self.raw_data = None
        self.headers = {"Content-Type": "application/json"}


    def proccess_data(self, is_diary=False, is_gluten=False):
        results=[]
        results+=[{
            "title": meal["title"],
            "ingredients": meal["ingredients"],
            "img": meal["thumbnail"]
            }
            for meal in self.raw_data["results"]]
         
        print(results)
        self.proccessed_data = results
        return results







