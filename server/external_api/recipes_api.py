from statistics import mean
from .api import Api

class RecipesApi(Api):

    def __init__(self, ingredient, diary_free, gluten_free):
        self.url = f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}"
        super().__init__(self.url)
        self.raw_data = None
        self.headers = {"Content-Type": "application/json"}
        self.diary_free = diary_free
        self.gluten_free = gluten_free


    def proccess_data(self):
        results=[]
        results+=[{
            "title": meal["title"],
            "ingredients": meal["ingredients"],
            "img": meal["thumbnail"],
            "href": meal["href"]
            }
            for meal in self.raw_data["results"]]
         
        print(results)
        self.proccessed_data = results
        return results







