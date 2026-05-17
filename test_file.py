# Test File:
# To test the functionality of our program, the user should run the main Python scirpt. At the start of the game, the program should ask the user to enter thier name.
# Once the name has been entered and submitted, an directions screen will apear, explaining to the user how to play the game. There will be a start button that will begin the game. 
#Once the user has pressed the start button, the game should begin. 
#The screen should show 10 squares in teo rows of 5, each square with a diffrent color. The squares should remain visible for 1 second. 
#After the first display disappears, the squares should reappear. Exactly one square should have changed color and the user should be able to click that one square. 
#If the user then clicks the square that changed color, the program should display a message stating "correct." The score then should increase by 1. 
#If the user then clocks the wrong the swuare, the program should display a message stating "incorrect." and the score should neither decrease nor increase. 
#If the user gets to 5 points in the score, the program should end the game and display a message that the user has won the game! 
#The sqaure that changes color should be selected randomly each round. 
#Our program does not require any extra data so no test data file is needed. 

from game_logic import generate_colors, change_one_color

def test_generate_colors():
    colors = generate_colors()
    assert len(colors) == 10
  
def test_change_format():
    colors = generate_colors()
    for color in colors:
        assert isinstance(color, tuple)
        assert len(color) == 3

def test_change_one_color_changes_something():
    colors = [(100, 100, 100)] * 10
    new_colors, index = change_one_color(colors)

    assert new_colors != colors


def test_change_one_color_index_valid():
    colors = [(100, 100, 100)] * 10
    new_colors, index = change_one_color(colors)

    assert 0 <= index < len(colors)


def test_only_one_color_changes():
    colors = [(100, 100, 100)] * 10
    new_colors, index = change_one_color(colors)

    differences = 0
    for i in range(len(colors)):
        if colors[i] != new_colors[i]:
            differences += 1

    assert differences == 1