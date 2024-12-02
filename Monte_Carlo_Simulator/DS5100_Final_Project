#Project_Dice_test.py
from unittest import mock
import unittest
import pandas as pd
from Project_Dice import Die, Game, Analyzer

class test_objectSuite(unittest.TestCase):
    """
    This class is for testing the Project_Dice.py file and it corresponding classes and methods.
    From unittest - mock will allow for inputs made by a user to be preset for testing.
    """
    @mock.patch('Project_Dice.input', create=True)
    
    #Die()
    def test_1_new_weight(self, mocked_input):
        
        mocked_input.side_effect = ['1,2,3', '1.5']
        
        test_object = Die()
        test_object.new_weight() #The mocked_input.side_effect is the input values 1,2,3 for the Faces selected then the input is 1.0 for what to change the weights of the faces too.
        
        default = Die()

        self.assertNotEqual(test_object._df.loc[1,'Weight'], default._df.loc[1,'Weight']) #Testing the change of weights.
        self.assertEqual(type(test_object._df), type(default._df)) #Testing the data structure output.
    
    def test_2_die_roll(self):
        
        test_object = Die()
        test_object.die_roll()
        
        self.assertTrue(isinstance(test_object.die_roll(), list))
    
    def test_3_show_data(self):
        
        test_object = Die()
        
        self.assertTrue(isinstance(test_object.show_data(), type(pd.DataFrame())))
    
    #Game()
    def test_4_play(self):
        
        test_object = Game([Die()])
        test_object.play()
        
        self.assertTrue(type(getattr(test_object,'_dice_rolling_results')), type(pd.DataFrame()))
        
    def test_5_results(self):
        
        test_object = Game([Die()])
        test_object.play()
        
        self.assertTrue(isinstance(test_object.results(), type(pd.DataFrame()))) #Testing for the wide formatted data frame.
        
        self.assertTrue(isinstance(test_object.results(2), type(pd.DataFrame()))) #Testing for the narrow formatted data frame.
    
    #Analyzer()
    def test_6_jackpot(self):
    
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        self.assertTrue(isinstance(test_object.jackpot(), int))
    
    def test_7_face_count_per_roll(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.face_count_per_roll(), type(pd.DataFrame())))
        
    def test_8_combo_count(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.combo_count(), type(pd.DataFrame())))
        
    def test_9_permutation(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.permutation(), type(pd.DataFrame())))
        

        
if __name__ == '__main__':
    
    unittest.main()