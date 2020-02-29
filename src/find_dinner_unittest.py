import unittest
import os
import src.find_dinner_helper as fh
import src.find_dinner_global as fg

fg.init()

class TestFindDinner(unittest.TestCase):
    # testing case 1
    def test_filter_out_past_ingredient(self):
        # Given
        # myFridge = './input/my-fridge-1.csv'
        
        # Expecting result
        # output_csv = './output/result_1.csv'
        result = ''
        output = ''

        self.assertEqual(result,output)
        
    # testing case 2
    def test_aggregate_item(self):
        # Given
        # myFridge = './input/my-fridge-2.csv'
        
        # Expecting result
        # output_csv = './output/result_2.csv'
        result = '1'
        output = ''

        self.assertEqual(result,output)
        
    # testing case 3
    def test_no_recipe(self):
        # Given
        # myFridge = './input/my-fridge-3.csv'
        # myRecipes = './input/my-recipes-3.json'
        
        # Expecting result
        # output_csv = './output/result_3.csv'
        result = ''
        output = ''

        self.assertEqual(result,output)
        
    # testing case 4
    def test_one_recipe(self):
        # Given
        # myFridge = './input/my-fridge-4.csv'
        # myRecipes = './input/my-recipes-4.json'
        
        # Expecting result
        # output_csv = './output/result_4.csv'
        result = ''
        output = '2'

        self.assertEqual(result,output)

    # testing case 5
    def test_multiple_recipes(self):
        # Given
        # myFridge = './input/my-fridge-5.csv'
        # myRecipes = './input/my-recipes-5.json'
        
        # Expecting result
        # output_csv = './output/result_4.csv'
        result = ''
        output = ''

        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()