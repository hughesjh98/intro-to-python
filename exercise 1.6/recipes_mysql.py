import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXIST Recipes(
    id             INT PRIMARY KEY AUTO_INCREMENT,
    name           VARCHAR(50),
    ingredients    VARCHAR(255),
    cooking_time   INT,
    difficulty     VARCHAR(20) 
    )''')

def main_menu(conn, cursor):
    choice = ''
    while choice != 'quit':
        print("="*20)
        print("\nMain Menu")
        print("what would you like to do? please enter a number below to get started - ")
        print("-"*15)
        print("  1. Create a new recipe ")
        print("  2. Search for a recipe by ingredient ")
        print("  3. Update an existing recipe ")
        print("  4. Delete a recipe ")
        print("  5. Show all recipes ")
        print("\n Type 'quit' if you would like to exit the program")
        choice = input("\nYour choice - ")
        print("="*20)
        
        if choice == '1':
            create_recipe(conn,cursor)
        elif choice == '2':
            search_recipe(conn,cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif(choice == '4'):
            delete_recipe(conn, cursor)
        elif choice == '5':
            view_all_recipes(conn,cursor)
            
        
        
def create_recipe(conn, cursor):
    
    recipe_ingredients = []
    name = str(input("enter the name of your recipe - "))
    
    cooking_time = int(input("enter the time it will take to make - "))
    
    ingredients = input("enter the ingredients for the recipe - ")
    
    recipe_ingredients.append(ingredients)
    
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    recipe_ingredients_str = ", ".join(recipe_ingredients) and ",".join(recipe_ingredients)
    
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    
    val = (name, recipe_ingredients_str, cooking_time, difficulty)
    
    cursor.execute(sql, val)
    conn.commit()
    
    print("your recipe has been added to the database ")

    
def calc_difficulty( cooking_time, recipe_ingredients):
    
    if cooking_time < 10 and len(recipe_ingredients) <= 4:
        difficulty_level = 'Easy'
    elif cooking_time < 10 and len(recipe_ingredients) >= 4:
        difficulty_level = 'Medium'
    elif cooking_time >= 10 and len(recipe_ingredients) < 4:
        difficulty_level = 'Intermediate'
    elif cooking_time >= 10 and len(recipe_ingredients) >= 4:
        difficulty_level = 'Hard'
    else:
        print("an error has ocurred, please try again")
    
    print("diffucilty level - ", difficulty_level)
    return difficulty_level


def search_recipe(conn, cursor):
    
    all_ingredients = []
    
    cursor.execute("SELECT ingredients FROM Recipes")
    
    results = cursor.fetchall();
    
    for recipe_ingredients_list in results:
        for recipe_ingredients in recipe_ingredients_list:
            recipe_ingredients_split = recipe_ingredients.split(", " or ',')
            all_ingredients.extend(recipe_ingredients_split)
            
    all_ingredients = list(dict.fromkeys(all_ingredients))
    
    all_ingredients_list = list(enumerate(all_ingredients))
    
    print("\nList of all ingredients")
    print("-"*15)
    
    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + ". " + tup[1])
    
    try:
        ingredient_searched_num = input("\nEnter the number corresponding to the ingredient you want to select from the above list - ")

        ingredient_searched_index = int(ingredient_searched_num) - 1

        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

        print("\nYou selected the ingredient: ", ingredient_searched)

    except:
        print("Make sure to select a number from the list.")

    else:
        print("\nThe recipe(s) below include(s) the selected ingredient: ")
        print("-------------------------------------------------------")

        cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient_searched + '%', ))

        
        results = cursor.fetchall()
    
        for row in results:
            print("\nID: ", row[0])
            print("Name: ", row[1])
            print("Ingredients: ", row[2])
            print("Cooking_time: ", row[3])
            print("difficulty: ", row[4])
            
def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    
    recipe_id_for_update = int(input("\nEnter the ID of the recipe you would like to update - "))

    column_for_update = str(input("\n which one of these would you like to update? 'name', 'cooking_time', or 'ingredients - ")) 
    
    updated_value = input("\nEnter the new value for the recipe -  ")
    
    print("choice - ", updated_value)
    
    if column_for_update == "name":
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
        print(column_for_update,"has been updated")
        
    elif column_for_update == "cooking_time":
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (updated_value,recipe_id_for_update))
        
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
        result_recipe_for_update = cursor.fetchall()
        
        name = result_recipe_for_update[0][1]
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s ", (updated_difficulty, recipe_id_for_update))
        print(column_for_update, " has been updated")
        
    elif column_for_update == "ingredients":
        
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_value, recipe_id_for_update))
        
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
        
        result_recipe_for_update = cursor.fetchall()
        
        name = result_recipe_for_update[0][1]
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        difficulty = result_recipe_for_update[0][4]
        
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
        print(column_for_update, " has been updated")
        
    conn.commit()
        
def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    
    recipe_to_delete = int(input("\n which recipe would you like to delete? - "))
        
    cursor.execute("DELETE FROM Recipes where id = (%s)", (recipe_to_delete, ))
    
    conn.commit()
    print("recipe has been deleted")
    
def view_all_recipes(conn,cursor):
    print("\n here is a list of all the recipes ")
    print("-"*15)
    
    cursor.execute(" SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    for row in results:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking_time: ", row[3])
        print("difficulty: ", row[4])
            
        
        
main_menu(conn, cursor)
print('bye\n')
        