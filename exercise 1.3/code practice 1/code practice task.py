weather = int(input(" whats the temperature outside? "))

if weather >= 40: 
    print(" you are getting toasted")
    
elif weather < 35 and weather > 25: 
    print("a t-shirt is your friend today")

elif weather < 24 and weather > 20:
    print("its getting a bit cold, wear a jacket")
    
else:
    print("just stay inside")