import unittest
import os
import src.find_dinner_helper as fh
from datetime import datetime
import pandas as pd

# Setup test_date to filter out past item in the file of fridge information
test_date = datetime.strptime('2020-03-01', '%Y-%m-%d')

class TestFindDinner(unittest.TestCase):
    # Testing case 1
    # The items with past use-by-date need to be filtered out
    def test_filter_out_past_ingredient(self):
        # Given
        myFridge = './input/my-fridge-1.csv'
        # Preprocess fridge information
        # In: (str, date) -> Out: dataframe
        result = fh.preprocess_fridge(myFridge, test_date)
        
        # Expecting result
        output_csv = './output/result_1.csv'
        output = pd.read_csv(output_csv, sep=',',
                             dtype={'item': str,'quantity': int, 'unit-of-measure': str,'use-by-date': str})
        output['use-by-date'] =  pd.to_datetime(output['use-by-date'], format='%d/%m/%Y')
        pd.testing.assert_frame_equal(result, output)
        
    # Testing case 2
    # Same items need to be aggregated into one, quantities will be summed and minimum use-by-date will be chosen
    def test_aggregate_item(self):
        # Given
        myFridge = './input/my-fridge-2.csv'
        # Preprocess fridge information
        # In: (str, date) -> Out: dataframe
        result = fh.preprocess_fridge(myFridge, test_date)
        
        # Expecting result
        output_csv = './output/result_2.csv'
        output = pd.read_csv(output_csv, sep=',',
                             dtype={'item': str,'quantity': int, 'unit-of-measure': str,'use-by-date': str})
        # Convert use-by-date from str to date
        output['use-by-date'] =  pd.to_datetime(output['use-by-date'], format='%d/%m/%Y')
        pd.testing.assert_frame_equal(result, output)
        
    # Testing case 3
    # 'Callfor takeout' will be returned if item cannot be found in fridge, unit-of-measure cannot matched or quantity is not enough in fridge
    def test_no_recipe(self):
        # Given
        myFridge = './input/my-fridge-3.csv'
        myRecipes = './input/my-recipes-3.json'
        # Get recommendation for dinner
        # In: (str, str, date) -> Out: str
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Call for takeout'

        self.assertEqual(result,output)
        
    # Testing case 4
    # The name of recipe will be returned if only one recipe is matched
    def test_one_recipe(self):
        # Given
        myFridge = './input/my-fridge-4.csv'
        myRecipes = './input/my-recipes-4.json'
        # Get recommendation for dinner
        # In: (str, str, date) -> Out: str
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Vegemite Sandwich'

        self.assertEqual(result,output)

    # Testing case 5
    # the recipe with the closest use-by-date will be returned if multiple recipes are matched
    def test_multiple_recipes(self):
        # Given
        myFridge = './input/my-fridge-5.csv'
        myRecipes = './input/my-recipes-5.json'
        # Get recommendation for dinner
        # In: (str, str, date) -> Out: str
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Peanut Butter Toast'

        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()