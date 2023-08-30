# exercise 1

class ShoppingList(object):
    def __init__(self, list_name):
        self.shopping_list = [] 
        self.list_name = list_name

        
    def add_item(self, item):
        self.item = item
        if item in self.shopping_list:
            print("Item already in the list")
        else:
            self.shopping_list.append(item)
            print("Item added to the list")
            
    def remove_item(self,item):
        self.item = item
        try:
            self.shopping_list.remove(item)
        except:
            print("item not found")
            
    def view_cart(self):
        print("\nItems in " +  str(self.list_name) + "\n" + 30*" - " )
        print("--------------------")
        for item in self.shopping_list:
            print(' - ' + str(item))
    
    def merge_list(self,object):
        merged_lists_name = 'Merged List - ' + str(self.list_name) + ' + ' + str(object.list_name)
        
        merged_lists_object = ShoppingList(merged_lists_name)
        
        merged_lists_object.shopping_list = self.shopping_list.copy()
        
        for item in object.shopping_list:
            if not item in merged_lists_object.shopping_list:
                merged_lists_object.shopping_list.append(item)
        return merged_lists_object
            
            
pet_store_list = ShoppingList("pet store shopping list")
grocery_store_list = ShoppingList("grocery store shopping list")


for item in ['dog food','cat food','food bowl','treats','toys']:
    pet_store_list.add_item(item)
    
for item in ['meat', 'fruits','soap', 'skincare', 'silverware']:
    grocery_store_list.add_item(item)
    
ShoppingList.merge_list(pet_store_list, grocery_store_list)

merged_list = ShoppingList.merge_list(pet_store_list,grocery_store_list)

merged_list.view_cart()



        
        
            
                    
            
        
        
                
    
    