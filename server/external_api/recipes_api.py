from statistics import mean
from xmlrpc.client import FastMarshaller
from .api import Api
from database.db_manager import recipe_valid
import json

class RecipesApi(Api):

    def __init__(self, ingredient, diary_free, gluten_free):
        self.url = f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}"
        super().__init__(self.url)
        self.raw_data = None
        self.headers = {"Content-Type": "application/json"}
        self.diary_free = json.loads(diary_free)
        self.gluten_free = json.loads(gluten_free)

    def proccess_data(self):
        results=[]
        
        results+=[{
            "title": meal["title"],
            "ingredients": meal["ingredients"],
            "img": meal["thumbnail"],
            "href": meal["href"]
            }
            for meal in self.raw_data["results"] if self.recipe_passed_validations(meal["ingredients"])]
        self.proccessed_data = results

        return results

    def recipe_passed_validations(self, ingredients):
        print((self.diary_free),)
        if not (self.diary_free) and not (self.gluten_free):
            print ("hi")
            return True
        elif (self.diary_free) and (self.gluten_free):
            return recipe_valid(ingredients, True, True)
        elif (self.diary_free) and not (self.gluten_free):
            return recipe_valid(ingredients, True, False)
        else :
            return recipe_valid(ingredients, False, True)    




