# DS5100_Final_Project

## Monte Carlo Simulator
## By: Louis Cocks </b>Date: 12/2/2024

The final project for Data Science programming. Includes a module.

### Synopsis

#### Install
The Monte Carlo Simulation of Dice rolling can be installed on any platform that has python and access to the internet. The repo is public.
Installations to use the Monte Carlo Simulator are Pandas, Numpy, and Random packages are imported in 'Import'.
Installations to use the Monte Carlo Simulator Tester are unittest, Pandas, and Monte_Carlo_Simulator are imported in 'Import'.


#### Import
Imports used by the Monte Carlo Simulator are Pandas, Numpy, and Random packages:
```
import numpy as np
import pandas as pd
import random
```
Imports to use the Monte Carlo Simulator Tester are unittest, Pandas, and Monte_Carlo_Simulator:
```
from unittest import mock
import unittest
import pandas as pd
from Monte_Carlo_Simulator import Die, Game, Analyzer
```

<ins>In order to import the Monte Carlo Simulator itself please use the import function as follows:</ins>
```
from Monte_Carlo_Simulator.Monte_Carlo_Simulator import Die, Game, Analyzer
```
This will allow the use of the Die(), Game(), and Analyzer() classes.
Another option is to import the overall python file and use its name as well with:
```
import Monte_Carlo_Simulator
```

#### Need to Know

<ins>This module can be used as a Monte Carlo Simulator with the scenario of choosing a dice (weighted or not), playing a game with that dice (rolling it), and analyzing information about the game played. 
The game can be played with more than one die as long as they have the same number of faces.</ins>

In order to properly use the code a few things should be known.

The `Die()` **class** does not require any arguments to be manually input and on default will create a 100 sided die with 'fair' (equal) weights for each face. **In order to change the number of faces use the `np.arange(1,3)` function as an argument to output a 2 sided die (coin) or anything other side count you like. Remember numpy will start at 0 so 1,3 gives 2 sides. Another option is to use `np.array([])` with string inputs to create a coin with `T` and `F` or an alphabet such as `np.array(['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])`.** Things to know about the methods:
    `new_weight`: This will require user input for the faces you would like to use in comma seperate numerics (ex. 1, 2, 3) and any numeric is possible for the wieght input. This will change those listed faces (sides) to the new weight so if multiple weights are wanted please run thid method multiple times for each selection of faces.
    `die_roll`: This does not require an argument `rolls` but it is optional to test roll your die a certain number of times (preset at `1` for 1 roll). Use a integer for this argument.
    `show_data`: This does not require any arguments and will naturally show a copy of the internal Pandas dataframe representing the faces and weights of the die through the argument `highlight` with a default value of `1`. Using the method with the value of `2` will return a table of the internal Pandas dataframe but with an Numpy array assortment and rows highlighted red that have any other values than `1.0` for the weight; **`display()` is required to output this**.
    
The `Game()` **class** does require the argument `dice` have a list of `Die()` with the same number of faces. It has no default. Things to know about the methods:
    `play`: This does not require any arguments as the default for `dice_rolls` is `1` however if rolling the set of dice more than 1 time please enter another integer value for this argument.
    `results`: This does not require any arguments as the default for `df_format` is `1` indicating a 'wide' Pandas dataframe. The other option is `2` which will result in a 'narrow' Pandas dataframe.
    
The `Analyzer()` **class** does require the argument `game` have an instance of the `Game()` class that has called the `play` method. This will have created and internally stored a Pandas dataframe of play results. Things to know about the methods:
    `jackpot`: This does not require any arguments and will display an integer of the number times a jackpot has been rolled. A jackpot occurs if an instance of rolling the dice results in them all landing on the same face. If you roll a die 6 times (ex. `Game().play(6)`) then there are six chances for hitting the jackpot.
    `face_count_per_roll`: This does not require any arguments and will return a Pandas dataframe of the play data with an index of the roll number, face values as columns, and count values in the cells (i.e. it is in wide format). If there is a face that is not rolled for any of the dice in any of the rolling instances (rows) then that value will not display in the table as a column.
    `combo_count`: This does not require any arguments and will return a Pandas dataframe with a multiindex for the rows and `Combination` for each distinct combination, and the column `Frequency` for the count for how many times the combination occurs in the game. These will be combinations of any order.
    `permutation`: This does not require any arguments and will return a Pandas dataframe with the mutltiindex for rows and `Combination` for each distinct combination, and the count `Frequency` for how many times that combination occurs in the game. These will be combinations of the exact order rolled.

<ins>After follwing the install and import above, and understanding more of the different classes and their methods there is only one thing to do now. Test!</ins>
In order to best test this file working properly on your device please use the Monte_Carlo_Simulator_test.py file and run it from your command line on which you installing the package. 
After testing has been passed then running this code will create your first die, play a game with it, and display the results along with if you hit any jackpots! Remember this is using a 100-sided die so if you get a jackpot your beat the odds of a .01% chance!!!
```
from Monte_Carlo_Simulator.Monte_Carlo_Simulator import Die, Game, Analyzer
Game1 = Game([Die(), Die()])
Game1.play()
Game1.results()
```

#### API description: 
This will list all the classes and methods with their attributes along with comments and docstrings. All parameters (with data types and defaults) have been described above and will show the code referenced along with all returns. 

Classes:
    A) Die
```
class Die():
```
    This class is for creating a 100 sided (default count) die stored as a Pandas Dataframe. The number of faces and weights of the die will be adjustable to allow for the die to be used as any other die. 
    The die can also be customized by the weight to allow for either a fair sided die or a unfairly distributed die.The weights are just positive numbers (integers or floats, including  0).
    Die() will initialize a Pandas DataFrame to be used through the class.
    inputs: self; faces: Each face of the die will show a unique number associated with that side and its corresponding weight in a Pandas DataFrame. Created with a NumPy Array is mandatory.

Methods:
1) Constuctor
```
    def __init__(self, faces = np.arange(1,101)):
```
        __init__: This intializer will serve to create the DataFrame, set the initial Face count to 100 unless otherwise fed an Numpy Array, and Weight distribution to 1.0 evenly.
                  It will also set the faces to the index of the DataFrame as Faces.
        inputs: self; faces: will default to a Numpy Array of 1-100
        returns: No return values.
        
        marker: Instance variable to tell if the Die is based on letters or numbers.
2) new_weight method
```
    def new_weight(self): 
```
        new_weight: This method has user input questions used to decide which Faces to change weights for. It will then adjust the weights held for those Faces within the DataFrame.
        inputs: self
        returns: No return values.
        
        chg_face: Local variable to store user input for which faces to change weights for.
        weight: Local variable to store the user input for what the new weight(s) should be.
        weight_list: Local variable to store the list of new weights for changing the entire dataframe of faces, must be in corresponding order with the create die faces.
3) die_roll method
```
    def die_roll(self, rolls = 1):
```
        die_roll: This method is used for rolling the create die using the DataFrame holding the data and a Random function random.choices to produce a random Face.
                  The default version does not internall store the results, however the internally stored version is commented out if otherwise wanted.
        inputs: self; rolls: default to 1.
        returns: An instance of rolling the die a number of times.
```
```#Not stored version```
        return [random.choices(self._df.index, self._df.Weight) for i in range(rolls)] 
        
```#Internally stored version commented out unless but available if wanted.```
#        results = []
#        for i in range(rolls):
#            roll = random.choices(self._df.index, self._df.Weight)
#            results.append(roll)
#        return results

```
4) show_data method
```
    def show_data(self, highlight = False):
```
        show_data: This method is for displaying the full table of data with its Faces and their corresponding weights with changes highlighted along with a dataframe returned value.
                   A custom function highlight_row() will also highlight any weights that do not have the default value of 1.
        inputs: self; highlight: default value is False andmethod returns a dataframe, any other input returns a display of the data and highlighted rows.
        returns: A fully laid out copy of the DataFrame if highlight = False, otherwise returns a display of the data and highlighted rows.

B) Game
```
class Game():
```
    This class is for creating a Die rolling game that has the same number of sides for each die but the weights can vary for the die.
    Each game is initialized with a Python list that contains one or more dice of the Die() object type.
    Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.
    Game objects only keep the results of their most recent play.
    inputs: self; dice: A Die() object wrapped in a python list to be a singular Die() or many.

1) Constructor method
``` 
    def __init__(self, dice):
```
        __init__: This initializer will need a list of Die in a list format. It will insure that the number of entered Faces for each Die are equal.
        inputs: self; dice: has no default as a list of Die's created through another class is required.
        returns: No return values.   

2) play method
```
    def play(self, dice_rolls = 1):
```
        play: This method is used for rolling all of the Dice given to the class a specified number of times and storing those results in a dataframe.
        inputs: self; dice_rolls: defaults to 1 for 1 rolling of each Die.
        returns: No return values.

3) results method
```
    def results(self, df_format = 1):
```
        results: This method is used to display the rolling results in either a Wide (default) or Narrow formatted dataframe.
        inputs: self; df_format: defaults to 1 and will only accept either 1 (corresponding to Wide) or 2 (corresponding to Narrow).
        returns: A copy of the dataframe in the specified format.
        
        copy: Local variable for storing the copied dataframe.
        df_wide: Local variable for storing the wide formatted copied dataframe.
        df_narrow: Local variable for storing the narrow formatted copied dataframe.
C) Analyzer
```
class Analyzer():
```
    This class will take the results of a single game and compute various descriptive statistical properties about said game.
    inputs: self; game: A Game() object of which the play() method of Game() has been run for, to insure a .

1) Constructor method
```
    def __init__(self, game):
```
        __init__: The initializer will require a Game instance be input and verify its correct object orientation.
        inputs: self; game: has no default as a Game object is required.
        returns: No return values.

2) jackpot method
```
    def jackpot(self):
```
        jackpot: This method will be used to calculate if all the Die, when rolled, land on the same Face. This is considered a jackpot.
        inputs: self
        returns: An integer value for the number of jackpots achieved in a game.

        jackpot_count: Local variable for storing the count of jackpots made through the play.
3) face_count_per_roll method
```
    def face_count_per_roll(self):
```
        face_count_per_roll: This method is for counting and siplaying each of the times a certain face of the die is rolled for each of the rolls attempted. 
        inputs: self
        returns: A dataframe with the possible faces rolled as the columns and each roll instance of the dice as the index. The values show the number of times (count) each of the faces is rolled.

3) combo_count method
```
    def combo_count(self):
```
        combo_count: This method will create a new dataframe containing the counts of each distinct combination (of any order i.e. sorting each row) of faces rolled among the dice in each roll.
        inputs: self
        returns: A dataframe with a multiindex for the rows and Combination for each distinct combination, and the column Frequency for the count for how many times the combination occurs in the game.

        combo_df: Local variable used for holding the dataframe of combos and counts.
4) permutation method
```
    def permutation(self):
```
        permutation: This method will create a new dataframe containing the counts of each distinct combination (of only the rolled order) of faces in their current rolled order """\
        """for each of the times rolled in the game.
        inputs: self
        returns: A dataframe with the mutltiindex for rows and Combination for each distinct combination, and the count Frequency for how many times that combination occurs in the game.

        perm_df: Local variable used for holding the dataframe of permutations.




