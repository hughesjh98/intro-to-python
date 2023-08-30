# exercise 2
# 
# class AddHeight(object):
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches
    
#     def __str__(self):
#         output = str(self.feet) + " feet, " + str(self.inches) + " inches"
#         return output
    
#     def __add__(self, other):
#         height_A_inches = self.feet * 12 + self.inches
#         height_B_inches = other.feet * 12 + other.inches
        
#         total_height_inches = height_A_inches + height_B_inches
        
#         output_feet = total_height_inches // 12
        
#         output_inches = total_height_inches - (output_feet * 12)
        
#         return AddHeight(output_feet, output_inches)
    
# adam = AddHeight(5, 3)
# stacy = AddHeight(4, 11)
# height_sum = stacy + adam

# print("total height:", height_sum)

# class SubHeight(object):
#     def __init__(self,feet,inches):
#         self.feet = feet
#         self.inches = inches 
        
#     def __str__(self):
#         output =  str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output
    
#     def __sub__(self, other):
#         height_A_inches = self.feet * 12 + self.inches
#         height_B_inches = other.feet * 12 + other.inches
        
#         total_height_inches = height_A_inches - height_B_inches
        
#         output_feet = total_height_inches // 12
        
#         output_inches = total_height_inches - (output_feet * 12)
        
#         return SubHeight(output_feet, output_inches)
    
# kevin = SubHeight(5, 7)
# amanda = SubHeight(5, 2)
# height_difference = kevin - amanda

# print("total_difference", height_difference)

# class OperatorHeight(object):
#     def __init__(self, feet, inches ):
#         self.feet = feet
#         self.inches = inches 
        
#     def __str__(self):
#         output =  str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output 
    
#     def __lt__(self, other):
#         height_A_inches = self.feet * 12 + self.inches 
#         height_B_inches = other.feet * 12 + other.inches 
#         return height_A_inches < height_B_inches
    
#     def __le__(self, other):
#         height_A_inches = self.feet * 12 + self.inches 
#         height_B_inches = other.feet * 12 + other.inches 
#         return height_A_inches <= height_B_inches
    
#     def __gt__(self, other):
#          height_A_inches = self.feet * 12 + self.inches 
#          height_B_inches = other.feet * 12 + other.inches 
#          return height_A_inches > height_B_inches
     
#     def __ge__(self, other):
#          height_A_inches = self.feet * 12 + self.inches 
#          height_B_inches = other.feet * 12 + other.inches 
#          return height_A_inches >= height_B_inches
     
#     def __eq__(self,other):
#         height_A_inches = self.feet * 12 + self.inches 
#         height_B_inches = other.feet * 12 + other.inches 
#         return height_A_inches == height_B_inches
    
#     def __ne__(self, other):
#         height_A_inches = self.feet * 12 + self.inches 
#         height_B_inches = other.feet * 12 + other.inches 
#         return height_A_inches != height_B_inches
    
# adam = OperatorHeight(5,11)
# stacy = OperatorHeight(4,11)
# amanda = OperatorHeight(5,5)
# carl = OperatorHeight(6,5)
# jack = OperatorHeight(7,11)
# peter = OperatorHeight(6,5)

# print( jack > carl )
# print( amanda < stacy )
# print (adam != stacy)
# print (carl == peter)

# people = [adam, stacy, amanda, carl, jack, peter]

# people = sorted(people, reverse = True)

# for OperatorHeight in people: 
#     print(OperatorHeight)
    
    






        