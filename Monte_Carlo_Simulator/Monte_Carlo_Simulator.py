#Monte_Carlo_Simulator
"""
Classes include Die(): Making a die to roll, Game(): Creating a game of rolling dice, and Analyzer(): Looking at metrics of a Game.

Requied installations include Pandas and NumPy and Random.
"""
import numpy as np
import pandas as pd
import random



#Die Creation.
class Die():
    """
    This class is for creating a 100 sided (default count) die stored as a Pandas Dataframe. The number of faces and weights of the die will be adjustable to allow for the die to be used as any other die. 
    The die can also be customized by the weight to allow for either a fair sided die or an unfairly distributed die.The weights are just positive numbers (integers or floats, including  0).
    Die() will initialize a Pandas DataFrame to be used through the class.
    inputs: self; faces: Each face of the die will show a unique number associated with that side and its corresponding weight in a Pandas DataFrame. Created with a Numpy Array is mandatory.
    """
    
    def __init__(self, faces = np.arange(1,101)):
        """
        __init__: This intializer will serve to create the DataFrame, set the initial Face count to 100 unless otherwise fed an Numpy Array, and Weight is a distribution to 1.0 evenly.
                  It will also set the faces to the index of the DataFrame as Faces.
        inputs: self; faces: will default to a Numpy Array of 1-100.
        returns: No return values.
        """
        self.faces = faces
        
        if type(faces[1]) == np.str_:
            marker = '_str'
        else:
            marker = '_int'
            
        self.marker = marker
        
        if isinstance(faces, np.ndarray) == False:
            raise TypeError("faces object must be of data type NumPy array and nothing else.")
        
        if np.unique(faces).size != len(faces):
            raise ValueError("The values in the numpy array faces must be distinct values.")
                
        _df = pd.DataFrame({'Faces': self.faces, 'Weight': list(1.0 for i in range(len(self.faces)))}).set_index('Faces')
        self._df = _df
        
    def new_weight(self): 
        """
        new_weight: This method has user input questions used to decide which Faces to change weights for. It will then adjust the weights held for those Faces within the DataFrame.
        inputs: self
        returns: No return values.
        """
        if self.marker == '_int':
            
            chg_face = [int(float(x.strip())) for x in input("Which face would you like to change the weight? note: All faces have a default weight of 1.0.\nEnter the information in a comma seperated numerical list.").split(",")] #Can take a list of faces to change weights for.
            for i in chg_face:  #Checking each value in chg_face list
                if not(i in self._df.index.unique(level='Faces')):
                    raise IndexError("A value entered for face selection is not in the array of 1 to 100.")
                    
            weight = float(input("What would you like the new weight to be?")) #Getting input for weight then converting to float, if float fails, value error if non-numerical.
            if not type(weight) is float:
                raise TypeError("Convert to float did not work, please enter a number.")
            #Replacing the existing weights with the new weight.
            for i in chg_face:
                self._df.loc[i, 'Weight'] = weight
            print(f"Face(s) {chg_face} have a new weight of {weight}.")
            
        elif self.marker == '_str':
            
            if input("Changing all values? Enter Yes or No") == 'No': #created for entering language letters and replacing all values.
                
                chg_face = [x.strip() for x in input("Which face would you like to change the weight? note: All faces have a default weight of 1.0.\nEnter the information in a comma seperated numerical list.").split(",")] #Can take a list of faces to change weights for.
                for i in chg_face:  #Checking each value in chg_face list
                    if not(i in self._df.index.unique(level='Faces')):
                        raise IndexError("A value entered for face selection is not in the array of provided letters.")
                        
                weight = float(input("What would you like the new weight to be?")) #Getting input for weight then converting to float, if float fails, value error if non-numerical.
                if not type(weight) is float:
                    raise TypeError("Convert to float did not work, please enter a number.")
                #Replacing the existing weights with the new weight.
                for i in chg_face:
                    self._df.loc[i, 'Weight'] = weight
                print(f"Face(s) {chg_face} have a new weight of {weight}.")
            
            else:
                
                weight_list = [int(float(x.strip())) for x in input("List the weights in a comma seperated list with the total number of weights matching the order & total number of letters used to create the Die().").split(",")]
                #creating a list of weights
                if not type(weight_list[1]) is int:
                    raise TypeError("Convert to float did not work, please enter a number.")

                for i, j in enumerate(self.faces):
                        self._df.loc[j, 'Weight'] = weight_list[i]
                print(f"All faces have their new weights.")
                
        #weight = float(input("What would you like the new weight to be?")) #Getting input for weight then converting to float, if float fails, value error if non-numerical.
        #if not type(weight) is float:
        #    raise TypeError("Convert to float did not work, please enter a number.")
        #Replacing the axisting weights with the new weight.
        #for i in chg_face:
        #    self._df.loc[i, 'Weight'] = weight
        #print(f"Face(s) {chg_face} have a new weight of {weight}.")
    
    
    def die_roll(self, rolls = 1):
        """
        die_roll: This method is used for rolling the create die using the DataFrame holding the data and a Random function random.choices to produce a random Face.
                  The default version does not internally store the results, however the internally stored version is commented out if otherwise wanted.
        inputs: self; rolls: default to 1.
        returns: An instance of rolling the die a number of times.
        """
#Not stored version
        return [random.choices(self._df.index, self._df.Weight) for i in range(rolls)] 
        
#Internally stored version
#        results = []
#        for i in range(rolls):
#            roll = random.choices(self._df.index, self._df.Weight)
#            results.append(roll)
#        return results
        
    def show_data(self, highlight = False):
        """
        show_data: This method is for displaying the full table of data with its Faces and their corresponding weights with changes highlighted along with a dataframe returned value.
                   A custom function highlight_row() will also highlight any weights that do not have the default value of 1. Use display() to print this dataset.
        inputs: self; highlight: default value is False andmethod returns a dataframe, any other input returns a display of the data and highlighted rows.
        returns: A fully laid out copy of the private DataFrame if highlight = False, otherwise returns a display of the data and highlighted rows.
        """
        if highlight == False:
            return self._df.copy()
        
        pd.set_option('display.max_rows', None)   #Condition to display all rows
        def highlight_row(_df, threshold, column): #Function created to be used to highlight a specific row red if there a number not equal to default 1.0
            is_max = pd.Series(data=False, index=_df.index)
            is_max['Weight'] = _df.loc['Weight'] != threshold
            return ['background-color: red' if is_max.any() else '' for v in is_max]
        return self._df.copy().style.apply(highlight_row, threshold=1, column='Weight', axis=1) #Displaying table and highlighted rows
        
        

#Playing a Game with dice.
class Game():
    """
    This class is for creating a Die rolling game that has the same number of sides for each die but the weights can vary for the die.
    Each game is initialized with a Python list that contains one or more dice of the Die() object type.
    Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.
    Game objects only keep the results of their most recent play.
    inputs: self; dice: A Die() object wrapped in a python list to be a singular Die() or many.
    """
    
    def __init__(self, dice):
        """
        __init__: This initializer will need a list of Die in a list format. It will insure that the number of entered Faces for each Die are equal.
        inputs: self; dice: has no default as a list of Die's created through another class is required.
        returns: No return values.
        """
        self.dice = dice
        #Returning a ValueError if the input dice are not in list format.
        try:
            len(self.dice[0]._df.index)
        except TypeError as e:
            print("Your Dice must be in a list!.")
            
        #Returning a ValueError if the number of Faces do no align with each other.
        _length = len(self.dice[0]._df.index)
        for i in range(len(self.dice)):
            if i > 0:
                if _length != len(self.dice[i]._df.index):
                    raise ValueError("The number of Faces for at least one of the Die are not the same as the others!")
    
    def play(self, dice_rolls = 1):
        """
        play: This method is used for rolling all of the Dice given to the class a specified number of times and storing those results in a private dataframe.
        inputs: self; dice_rolls: defaults to 1 for 1 rolling of each Die.
        returns: No return values.
        """
        dice_rolls = abs(dice_rolls) #ensures the assumed correct number of play
        #Private dataframe instantiation
        _dice_rolling_results = pd.DataFrame()
        
        for i in range(len(self.dice)):
            _roll_result = pd.DataFrame(random.choices(self.dice[i]._df.index, self.dice[i]._df.Weight) for j in range(dice_rolls))
            _dice_rolling_results = pd.concat([_dice_rolling_results,_roll_result], axis = 1)
        _dice_rolling_results.columns = [k for k in range(len(self.dice))]
        
        self._dice_rolling_results = _dice_rolling_results
#For testing        
        #return _dice_rolling_results
        
    def results(self, df_format = 1):
        """
        results: This method is used to display the rolling results in either a Wide (default) or Narrow formatted dataframe.
        inputs: self; df_format: defaults to 1 and will only accept either 1 (corresponding to Wide) or 2 (corresponding to Narrow).
        returns: A copy of the private dataframe in the specified format.
        """
        if not(df_format in (1,2)):
            raise ValueError("Formatting can only be entered as '1' for Wide or '2' for Narrow.")
        
        copy = self._dice_rolling_results.copy(deep = True) 
        
        if df_format == 1:
            df_wide = copy.rename_axis('Roll Number').rename_axis('Die', axis = 'columns')
            return df_wide
        else:
            cols = copy.columns.to_list()
            df_narrow = pd.melt(copy, value_vars = cols).set_index('variable', append = True)
            df_narrow.index.names = ['Roll Number', 'Die']
            return df_narrow



#Analyzing a Game of rolled Dice
class Analyzer():
    """
    This class will take the results of a single game and compute various descriptive statistical properties about said game.
    inputs: self; game: A Game() object of which the play() method of Game() has been run for.
    """
    def __init__(self, game):
        """
        __init__: The initializer will require a Game instance be input and verify its correct object orientation.
        inputs: self; game: has no default as a Game object is required.
        returns: No return values.
        """
        self.game = game
        #testing will require using the two classes Die() and Game().
        if isinstance(self.game, type(Game([Die()]))) == False:
            raise ValueError("The passed object is not a Game, passing only a Game type object will work.")
        
    def jackpot(self):
        """
        jackpot: This method will be used to calculate if all the Die, when rolled, land on the same Face. This is considered a jackpot.
        inputs: self
        returns: An integer value for the number of jackpots achieved in a game.
        """
        jackpot_count = (self.game.results().nunique(axis=1) == 1).sum()
        if len(self.game.results().nunique(axis=0)) == 1:
            print('Cannot get a jackpot with 1 die! Try again with multiple.')
            return
        return int(jackpot_count)
        
    def face_count_per_roll(self):
        """
        face_count_per_roll: This method is for counting and displaying each of the times a certain face of the die is rolled for each of the rolls attempted. 
        inputs: self
        returns: A dataframe with the possible faces rolled as the columns and each roll instance of the dice as the index. The values show the number of times (count) each of the faces is rolled.
        """
        all_faces = sorted(set(face for die in self.game.dice for face in die.faces))
        face_counts = pd.DataFrame({face: self.game.results().apply(lambda row: row.tolist().count(face), axis=1) for face in all_faces}
        )
        face_counts.columns.name = 'Faces'
        return face_counts
    
    def combo_count(self):
        """
        combo_count: This method will create a new dataframe containing the counts of each distinct combination (of any order i.e. sorting each row) of faces rolled among the dice in each roll.
        inputs: self
        returns: A dataframe with a multiindex for the rows and Combination for each distinct combination, and the column Frequency for the count for how many times the combination occurs in the game.
        """
        combo_df = self.game.results().apply(lambda row: list(sorted(row)), axis = 1)
        combo_df = combo_df.value_counts().reset_index(name = 'Frequency').rename(columns = {'index': 'Combination'}) 
        return combo_df
        
    def permutation(self):
        """
        permutation: This method will create a new dataframe containing the counts of each distinct combination (of only the rolled order) of faces in their current rolled order """\
        """for each of the times rolled in the game.
        inputs: self
        returns: A dataframe with the multiindex for rows and Combination for each distinct combination, and the count Frequency for how many times that combination occurs in the game.
        """
        perm_df = self.game.results().apply(lambda row: list(row), axis = 1)
        perm_df = perm_df.value_counts().reset_index(name = 'Frequency').rename(columns = {'index': 'Combination'})
        return perm_df

        