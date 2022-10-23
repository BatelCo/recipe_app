import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")

def insert_ingredients(ingredients_arr, table_name, field_name):
    try:
        values = []
        for ingredient in ingredients_arr:
            values.append(f'("{ingredient}")')
        with connection.cursor() as cursor:
            query = f"INSERT ignore into {table_name}({field_name}) values{','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def get_ingredients(table_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)
            connection.commit()
            results = cursor.fetchall()
            ingredient = []
            for res in results:
                ingredient.append(res["name"])
            return (ingredient)
    except TypeError as e:
        print(e)

def filter_recipe(ingredients,diary_free ,gluten_free):
    is_filter_dairy = True
    is_filter_gluten = True
    if diary_free:
        is_filter_dairy = filter_dairy(ingredients)
    if gluten_free:
        is_filter_gluten = filter_gluten(ingredients)
    if(is_filter_dairy and is_filter_gluten):
        return True
    return False
    

def filter_dairy(ingredients):
    ingredient = []
    for i in ingredients:
        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM dairy_ingredients d WHERE d.dairy_name=%s;"
                cursor.execute(query, i)
                connection.commit()
                results = cursor.fetchall()
                if len(results) != 0:
                    ingredient.append(results)
        except TypeError as e:
            print(e)
        
    if len(ingredient) == 0:
        return True
    return False

def filter_gluten(ingredients):
    ingredient = []
    for i in ingredients:
        try:
            with connection.cursor() as cursor:
                query = "SELECT * FROM gluten_ingredients d WHERE d.gluten_name=%s;"
                cursor.execute(query,i)
                connection.commit()
                results = cursor.fetchall()
                if len(results) != 0:
                    ingredient.append(results)
        except TypeError as e:
            print(e)
        
    if len(ingredient) == 0:
        return True
    return False