import pandas as pd
import json

def preprocess_fridge(fridge_file, current_date):
    # Load myFridge with column types
    df_myFridge = pd.read_csv(fridge_file, sep=',',
                            dtype={'item': str,'quantity': int, 'unit-of-measure': str,'use-by-date': str})
    df_myFridge['use-by-date'] =  pd.to_datetime(df_myFridge['use-by-date'], format='%d/%m/%Y')

    # An ingredient that is past its use-by date should not be used for cooking.
    df_myFridge = df_myFridge[df_myFridge['use-by-date'] >= current_date]

    # For same item with diffent use-by-date, sum the quantity and get the smallest use-by-date
    df_myFridge = df_myFridge.groupby(['item', 'unit-of-measure']).agg({'quantity':sum, 'use-by-date': min}).reset_index()
    
    return df_myFridge

def what_is_for_dinner(fridge_file, recipe_file, current_date):
    # Load fridge stock
    df_myFridge = preprocess_fridge(fridge_file, current_date)
    # Load myRecipes
    with open(recipe_file) as recipe_json:
        recipes = json.load(recipe_json)

    # Suggest dinner
    food_list = []
    fdd = []
    for recipe in recipes:
        name = recipe['name']
        date = '9999-12-31'
        flag = 0
        for ingredient in recipe['ingredients']:
            item = ingredient['item']
            try:
                quantity = int(ingredient['quantity'])
            except:
                flag = 1
                break
            unit_of_measure = ingredient['unit-of-measure']
            
            # Check if the stock is enough
            food = df_myFridge[(df_myFridge['item'] == item) & (df_myFridge['quantity'] >= quantity) & (df_myFridge['unit-of-measure'] == unit_of_measure)]
            if food.empty:
                flag = 1
                break

            # Get closest use-by-date
            use_by_date = food['use-by-date'].astype(str).min()
            if date > use_by_date:
                date = use_by_date
        
        if flag == 1:
            continue
        
        food_dict = {
            'name' : name,
            'date' : date
        }
        food_list.append(food_dict)

    # No recipe found
    if len(food_list) == 0:
        print('Call for takeout')
        
    # One recipe
    elif len(food_list) == 1:
        print(food_list[0]['name'])
        
    # More than one recipe found
    # Get the closest date to pick the food.
    # If dates are same, randomly pick one
    else:
        df_food = pd.DataFrame(food_list)
        print(df_food.sort_values(by ='date').iloc[0]['name'])