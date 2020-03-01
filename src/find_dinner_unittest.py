import unittest
import os
import src.find_dinner_helper as fh
from datetime import datetime
import pandas as pd

test_date = datetime.strptime('2020-03-01', '%Y-%m-%d')

class TestFindDinner(unittest.TestCase):
    # testing case 1
    def test_filter_out_past_ingredient(self):
        # Given
        myFridge = './input/my-fridge-1.csv'
        result = fh.preprocess_fridge(myFridge, test_date)
        
        # Expecting result
        output_csv = './output/result_1.csv'
        output = pd.read_csv(output_csv, sep=',',
                             dtype={'item': str,'quantity': int, 'unit-of-measure': str,'use-by-date': str})
        output['use-by-date'] =  pd.to_datetime(output['use-by-date'], format='%d/%m/%Y')
        pd.testing.assert_frame_equal(result, output)
        
    # testing case 2
    def test_aggregate_item(self):
        # Given
        myFridge = './input/my-fridge-2.csv'
        result = fh.preprocess_fridge(myFridge, test_date)
        
        # Expecting result
        output_csv = './output/result_2.csv'
        output = pd.read_csv(output_csv, sep=',',
                             dtype={'item': str,'quantity': int, 'unit-of-measure': str,'use-by-date': str})
        output['use-by-date'] =  pd.to_datetime(output['use-by-date'], format='%d/%m/%Y')
        pd.testing.assert_frame_equal(result, output)
        
    # testing case 3
    def test_no_recipe(self):
        # Given
        myFridge = './input/my-fridge-3.csv'
        myRecipes = './input/my-recipes-3.json'
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Call for takeout'

        self.assertEqual(result,output)
        
    # testing case 4
    def test_one_recipe(self):
        # Given
        myFridge = './input/my-fridge-4.csv'
        myRecipes = './input/my-recipes-4.json'
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Vegemite Sandwich'

        self.assertEqual(result,output)

    # testing case 5
    def test_multiple_recipes(self):
        # Given
        myFridge = './input/my-fridge-5.csv'
        myRecipes = './input/my-recipes-5.json'
        result = fh.what_is_for_dinner(myFridge, myRecipes, test_date)
        
        # Expecting result
        output = 'Peanut Butter Toast'

        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()