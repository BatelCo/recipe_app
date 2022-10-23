from statistics import mean
from xmlrpc.client import FastMarshaller
from .api import Api
from database.db_manager import filter_recipe 

class RecipesApi(Api):

    def __init__(self, ingredient, diary_free, gluten_free):
        self.url = f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}"
        super().__init__(self.url)
        self.raw_data = None
        self.headers = {"Content-Type": "application/json"}
        self.diary_free = diary_free
        self.gluten_free = gluten_free
        print(diary_free, gluten_free)


    def proccess_data(self):
        results=[]
        
        results+=[{
            "title": meal["title"],
            "ingredients": meal["ingredients"],
            "img": meal["thumbnail"],
            "href": meal["href"]
            }
            for meal in self.raw_data["results"] if self.filtered_recipes(meal["ingredients"])]
        self.proccessed_data = results

        return results

    def filtered_recipes(self, ingredients):
        if not bool(self.diary_free) and not bool(self.gluten_free):
            return True
        elif bool(self.diary_free) and bool(self.gluten_free):
            return filter_recipe(ingredients, True, True)
        elif bool(self.diary_free) and not bool(self.gluten_free):
            return filter_recipe(ingredients, True, False)
        else :
            return filter_recipe(ingredients, False, True)    




