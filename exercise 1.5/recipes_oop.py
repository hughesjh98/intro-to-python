class Recipe(object):
    all_ingredients = []
    
    def __init__(self,name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ''
        
    def __str__(self):
        output = "\nRecipe name: " + str(self.name) + \
            "\nCooking time: " + str(self.cooking_time) + \
            "\nDifficulty: " + str(self.difficulty) + \
            "\nIngredients:\n" 
            
        for ingredient in self.ingredients:
            output += ' - ' + ingredient + '\n'
        return output

    def get_name(self):
        output = "Recipe name: " + str(self.name) 
        return output
    
    def set_name(self, name):
        self.name = str(name)
        
    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()
        
    def get_ingredients(self):
        print("ingredients for this recipe")
        print("-"*20)
        for ingredient in self.ingredients:
            print('-', str(ingredient))
         
        
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)
        
    def get_cooking_time(self):
        output = "Cooking_time: " + int(self.cooking_time)
        return output 
    
    def set_cooking_time(self,cooking_time):
        self.cooking_time = int(cooking_time)
        
    def get_difficulty(self):
        difficulty = self.calc_difficulty(self.cooking_time,self.ingredients)
        self.difficulty = difficulty
        output = "Difficulty level: " + str(self.difficulty)
        return output
        
        
    def calc_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) <= 4:
            difficulty_level = 'Easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty_level = 'Medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty_level = 'Intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty_level = 'Hard'
        return difficulty_level
    
    def search_ingredient(self, ingredient, ingredients):
        try:
            if ingredient in ingredients:
                 return True
        except:
                 return False
    
    def recipe_search(self, recipes_list, ingredient):
        data = recipes_list
        search_term = ingredient
        
        for recipe in data:
            if self.search_ingredient(search_term, recipe.ingredients):
                print(recipe)
                
    def view_recipe(self):
        print('Name: ' + str(self.name))
        print('Cooking time(minutes): ' + str(self.cooking_time))
        print('Difficulty: ', str(self.difficulty))
        self.get_ingredients()
        print('-'*20)
    
recipes_list = []
        
tea = Recipe('Tea')
tea.add_ingredients('tea leaves', 'sugar', 'water')
tea.set_cooking_time(5)
tea.get_difficulty()

coffee = Recipe("coffee")
coffee.add_ingredients('coffee powder', 'sugar', 'water')
coffee.set_cooking_time(5)
coffee.get_difficulty()

cake = Recipe('Cake')
cake.add_ingredients('sugar', 'eggs', 'butter', 'vanilla essence', 'flour', 'milk', 'baking powder')
cake.set_cooking_time(50)
cake.get_difficulty()

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients('bananas', 'milk', 'peanut butter', 'sugar', 'ice cubes', )
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()

recipes_list.append(tea)
recipes_list.append(coffee)
recipes_list.append(cake)
recipes_list.append(banana_smoothie)

print("here is a list of all of your recipes")
print('-'*20)
for recipe in recipes_list:
    print(recipe)

print('recipes that contain coffee powder')
print('-'*20)
coffee.recipe_search(recipes_list, 'coffee powder')

print('recipes that contain sugar')
print('-'*20)
coffee.recipe_search(recipes_list, 'sugar')

print('recipes that contain bananas')
print('-'*20)
coffee.recipe_search(recipes_list, 'bananas')

