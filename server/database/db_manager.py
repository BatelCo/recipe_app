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

