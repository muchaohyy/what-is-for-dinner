import os
import find_dinner_helper as fh
import find_dinner_global as fg

fg.init()

# Get location of Fridge Storage File
myFridge = input('Fridge Storage File: ')
if not os.path.isfile(myFridge):
    print('Fridge Storage file cannot be found')
    exit(1)

# Get location of Recipe File
myRecipes = input('Recipe File: ')
if not os.path.isfile(myRecipes):
    print('Recipe file cannot be found')
    exit(1)

# Get recommendation for dinner
# In: (str, str, date) -> Out: str
result = fh.what_is_for_dinner(myFridge, myRecipes, fg.today)
print(result)