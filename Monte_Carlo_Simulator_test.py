#Monte_Carlo_Simulator_test.py
from unittest import mock
import unittest
import pandas as pd
from Monte_Carlo_Simulator.Monte_Carlo_Simulator import Die, Game, Analyzer
#The first Monte_Carlo_Simulator is for the directory then the python file is named Monte_Carlo_Simulator therefore Monte_Carlo_Simulator.Monte_Carlo_Simulator--
class test_objectSuite(unittest.TestCase):
    """
    This class is for testing the Project_Dice.py file and it corresponding classes and methods.
    From unittest - mock will allow for inputs made by a user to be preset for testing.
    """
    
    #Die()
    
    def test_1_Die(self):
        
        test_object = Die()
        
        self.assertIsInstance(test_object, Die)
        
    @mock.patch('Monte_Carlo_Simulator.Monte_Carlo_Simulator.input', create=True)
    def test_2_new_weight(self, mocked_input):
        
        mocked_input.side_effect = ['1,2,3', '1.5']
        
        test_object = Die()
        test_object.new_weight() #The mocked_input.side_effect is the input values 1,2,3 for the Faces selected then the input is 1.0 for what to change the weights of the faces too.
        
        default = Die()

        self.assertNotEqual(test_object._df.loc[1,'Weight'], default._df.loc[1,'Weight']) #Testing the change of weights.
        self.assertEqual(type(test_object._df), type(default._df)) #Testing the data structure output.
    
    def test_3_die_roll(self):
        
        test_object = Die()
        test_object.die_roll()
        
        self.assertTrue(isinstance(test_object.die_roll(), list))
    
    def test_4_show_data(self):
        
        test_object = Die()
        
        self.assertTrue(isinstance(test_object.show_data(), type(pd.DataFrame()))) #Testing for the regular dataframe output.
        
        self.assertEqual(type(test_object.show_data(2)), type(pd.DataFrame().style)) #Testing for the table return with styling.
    
    #Game()
    def test_5_Game(self):
        
        test_object = Game([Die()])
        
        self.assertIsInstance(test_object, Game)
        
    def test_6_play(self):
        
        test_object = Game([Die()])
        test_object.play()
        
        self.assertTrue(type(getattr(test_object,'_dice_rolling_results')), type(pd.DataFrame()))
        
    def test_7_results(self):
        
        test_object = Game([Die()])
        test_object.play()
        
        self.assertTrue(isinstance(test_object.results(), type(pd.DataFrame()))) #Testing for the wide formatted data frame.
        
        self.assertTrue(isinstance(test_object.results(2), type(pd.DataFrame()))) #Testing for the narrow formatted data frame.
    
    #Analyzer()
    def test_8_Analyzer(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertIsInstance(test_object, Analyzer)
        
    def test_9_jackpot(self):
    
        test_object = Game([Die()])
        test_object.play()
        if len(test_object.results().nunique(axis=0)) == 1:

            self.assertEqual(len(test_object.results().nunique(axis=0)), 1) #Testing code with a single die rolled.
        else:    
            test_object = Analyzer(test_object)
        
            self.assertTrue(isinstance(test_object.jackpot(), int)) #Testing code with multiple die rolled (true jackpot).
    
    def test_10_face_count_per_roll(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.face_count_per_roll(), type(pd.DataFrame())))
        
    def test_11_combo_count(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.combo_count(), type(pd.DataFrame())))
        
    def test_12_permutation(self):
        
        test_object = Game([Die()])
        test_object.play()
        test_object = Analyzer(test_object)
        
        self.assertTrue(isinstance(test_object.permutation(), type(pd.DataFrame())))
        

        
if __name__ == '__main__':
    
    unittest.main()