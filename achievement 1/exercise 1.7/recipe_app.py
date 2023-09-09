from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("mysql://cf-python:password@localhost/task_database")

Base = declarative_base()

# set up a class to create a table and accept 
class Recipe(Base):
    __tablename__ = 'final_recipes_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"

    def __str__(self):   
      output = "\nName: " + str(self.name) + \
      "\nCooking time (minutes): " + str(self.cooking_time) + \
      "\nDifficulty: " + str(self.difficulty) + \
      "\nIngredients: " + str(self.ingredients)
      return output

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# this method will take the cooking_time and ingredients and calculate the difficulty
def calc_difficulty(cooking_time, recipe_ingredients):
    
    if (cooking_time < 10) and (len(recipe_ingredients) <= 4):
        difficulty_level = 'Easy'
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = 'Medium'
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty_level = 'Intermediate'
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = 'Hard'
    else:
        print("sorry there was an error. please try again.")
    return difficulty_level
        
#create a new recipe and set up variable to check if the data is matching the mySQL database
def create_recipe():
    
    recipe_ingredients = []
    name_input_value = False
    cooking_time_input_value = False
    ingredients_quantity = False
    
    while name_input_value == False:
        
        name = input(" what is the name for this Recipe? - ")
        
        if len(name) < 50:
            
            name_input_value = True
            
        else:
            
            print("please enter a name with less than 50 characters")
    
    while cooking_time_input_value == False:
        
        cooking_time = input("how many minutes to make this recipe? - ")
                
        if cooking_time.isnumeric() == True:
            
            cooking_time_input_value = True
    
    while ingredients_quantity == False:
        
        ingredients_input = input("how many ingredients would you like to add? - ")
        
        if ingredients_input.isnumeric() == True:
            
            ingredients_quantity = True
            
            for _ in range(int(ingredients_input)):
                
                ingredient = input("add the name of the ingredient - ")
                recipe_ingredients.append(ingredient)
        else: 
            
            print("please enter a postive number")
            
    recipe_ingredients_str = ','.join(recipe_ingredients)
    print(recipe_ingredients_str)
        
    difficulty = calc_difficulty(int(cooking_time), recipe_ingredients)
    
    #create an object to add the database 
    recipe_entry = Recipe(
        name = name,
        cooking_time = int(cooking_time),
        ingredients = recipe_ingredients_str,
        difficulty = difficulty
    )
    
    session.add(recipe_entry)
    session.commit()
    
    print("recipe has been added to the database")
    
#view all of the recipes and add them to a list
def view_all_recipes():
    
    all_recipes = []
    
    all_recipes = session.query(Recipe).all()
        
    if len(all_recipes) == 0:
        
        print("sorry recipes not found")
    else:
        
        print("\nhere is a list of all the recipes")
        print("-"*15)
            
    for recipe in all_recipes:
        print(recipe)
                
    #search for recipes based on ingredients
def search_by_ingredients():
    
    check_recipes = session.query(Recipe).count()
        
    if check_recipes == 0:
        
        print("sorry there are no recipes in your database")
        return None
        
    else:
        
    # get all of the ingredients and store them in a list to loop over
        results = session.query(Recipe.ingredients).all()

        all_ingredients = []
    
        for recipe_ingredient_lists in results:
            
            for recipe_ingredients in recipe_ingredient_lists:
                recipe_ingedients_split = recipe_ingredients.split(',') 
                all_ingredients.extend(recipe_ingedients_split)
    
    #create a list of dictionaries with key - ingredients to enumerate 
        all_ingredients = list(dict.fromkeys(all_ingredients))
        all_ingredients_list = list(enumerate(all_ingredients))
           
        print("\nlist of all ingredients - ")
        print("-"*15)
           
        for index,tup in enumerate(all_ingredients_list):
            
            print(str(tup[0]+1) + "." + tup[1])
               
        try:
    #user is able to search for 1 or more ingredients
            ingredients_searched_num = input("\nEnter one or more numbers to select one or more ingredients - ")
            ingredients_list_searched = ingredients_searched_num.split(" " or "")
    #store their searched ingredients in a list
            searched_ingredients_list = []
            for ingredients_searched_num in ingredients_list_searched:
                ingredients_searched_index = int(ingredients_searched_num) - 1 
                ingredients_searched = all_ingredients_list[ingredients_searched_index][1]
                searched_ingredients_list.append(ingredients_searched)
            
            print("selected ingredients - ", searched_ingredients_list)
            
            conditions = []
            
    #for each ingredient, its stored in conditions to find recipes with the same ingredients
            for ingredient in searched_ingredients_list:
                like_term = "%"+ingredient+"%"
            
                condition = Recipe.ingredients.like(like_term)
                
                conditions.append(condition)
            
            searched_recipes = session.query(Recipe).filter(*conditions).all()
        except:
            
            print("Make sure to select a number from the list.")

        else:
            
            print("\nThe recipe(s) below include(s) the selected ingredient: ")
            print("-------------------------------------------------------")
            for recipe in searched_recipes:
                print(recipe)
           
    # update the recipe based on the users choices of name, cooking time, or ingredients
def edit_recipes():
    
    check_recipes = session.query(Recipe).count()
    
    if check_recipes == 0:
        
        print("no recipes in your database")
        return None
    else:
        
        #print the recipes in the DB that can be updated
        results = session.query(Recipe).with_entities(Recipe.id,Recipe.name).all()
        print("recipes to update")
        print("-"*10)
        for recipe in results:
            
            print("\nID - ", recipe[0])
            print("\nname - ", recipe[1])
    
        recipe_id_to_edit = int(input("please enter the id of the recipe you'd like to update - "))
        
        #store the recipes ID in a list to check if the id matches the users input
        recipe_id_tup_list = session.query(Recipe).with_entities(Recipe.id).all()
        recipe_id_list = []
        
        for recipe_tup in recipe_id_tup_list:
            
            print(recipe_tup[0])
            recipe_id_list.append(recipe_tup[0])
            
        print(recipe_id_list)
        
        if recipe_id_to_edit not in recipe_id_list:
            
            print("sorry, couldn't find your recipe by id. please try again")
        else:
            
            #get the recipes that matches the users input 
            recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).one()
            
            print("\n you are about to edit the following recipe - ")
            print(recipe_to_edit)       
            
            column_for_update = int(input("\nEnter the data you want to update among 1. name, 2. cooking time 3. ingredients -  "))
            
            updated_value = input("please enter the new value for your recipe - ")
            
            #after the user picks a Recipe ID, column to update, and new value, use if,elif to update the recipe
            if column_for_update == 1:
                session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({Recipe.name: updated_value})
                print(column_for_update, " has been updated")
                
                
            elif column_for_update == 2:
                session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({Recipe.cooking_time: updated_value})
                print(column_for_update, " has been updated")
                
                
            elif column_for_update == 3:
                session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({Recipe.ingredients: updated_value})
                
                
            else:
                print("\noops, something happened. please try again")
            
            #update the difficulty
            update_difficulty = calc_difficulty(int(recipe_to_edit.cooking_time), recipe_to_edit.ingredients)
            
            recipe_to_edit.difficulty = update_difficulty
            session.commit()
            print("Your Recipe has been updated")
            
    #delete a recipe from the list
def delete_recipe():
    
        check_recipes = session.query(Recipe).count()
        
        if check_recipes == 0:
            
            print("no recipes in your database")
            return None
        
        else:
        
        # get the name and id to be deleted
            recipe_list = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
            print("list of recipes")
            print("-"*15)
            for recipe in recipe_list:
                
                print("\nid: ", recipe[0])
                print("\nname: ", recipe[1])
                print("-"*8)
            
            recipe_id_input = input("please enter the ID of the recipe you would like to delete - ")
        
            recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id_input).one()
        
            confirm_delete = input("are you sure you want to delete this recipe? yes / no - ")
        
            if confirm_delete == 'yes':
                
                session.delete(recipe_to_delete)
                session.commit()
                print("you have successfully deleted this recipe")    
            else:
                return None
        
        
def main_menu():
    
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
            create_recipe()
        elif choice == '2':
            search_by_ingredients()
        elif choice == '3':
            edit_recipes()
        elif(choice == '4'):
            delete_recipe()
        elif choice == '5':
            view_all_recipes()
        elif choice == "quit":
            print("bye bye!")
        else:
            print("please enter a valid number")
            
            