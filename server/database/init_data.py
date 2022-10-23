import db_manager

dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]

db_manager.insert_ingredients(dairy_ingredients, "dairy_ingredients", "dairy_name")
db_manager.insert_ingredients(gluten_ingredients, "gluten_ingredients", "gluten_name")