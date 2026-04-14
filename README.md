# memory-game

MEMORY GAME DEMO
Group; Ava Zumerchik (avazumerchik-design) and Demetra Marlantis (demetramarlantis- netizen)

What is the Memory Game? 

The Memory Game is a entertaining program that will challange your memory and help to practice your focus.  To start, you will enter your player name. There will be 10 squares, each a different color, that will be arranged in two rows of 5 squares. You will be shown all 10 squares breifly, the screen will go blank, and then the colorded sqaures will show back up, one of them with a different color than before. Your job is to select which square has changed color. If you guess correctly, you will get a point! If you guess incorrect, the program will tell you that you were incorrect and you will move on. To win the game, you need to get 5 points! Good Luck!

List of Functions & Methods:

- get_player_name ()
    - this has the user enter thier name at the start of the game, there is no parameter

- show_colors(colors)
    - this function will display the 10 colored squares for the one second 
    - the parameter is a list of colors 

- change_sqaure(colors) 
    - Randomly selects one square at a time to change the color of before redisplaying the sqaures for the player 
    - The parameter is the 10 original colors 
    - This functon returns the updated colors and the index of the sqaure that changed

- check_answer (user_choice, changed_index, streak)
    - This function checks if the user clicks the correct or incorrect square 
    - The parameters are user_choice, which is whichever square selected by the user. Changed_index is the index of the sqaure that was changed colors. score is the currect score of the correct answers the user has gotten. 
         - This function returns the updated score count 

- display_win_screen() 
    - displays the winning graphic if the player reaches 5 points 

- main()
    - runs the game loop and makes all the functions work together 

Example use cases: 
A user would use this program if they wanted to play a game for entertainment. They could also use this game as a way to challange their memory or to practice thier focus. 


Python Script File:Proposed functions and responsibilities

- get_player_name()- Demi
 (Ask the user to input their name before the game begins)

- show_directions()- Demi
(the screen with the directions of how to play the game)

- show_colors(colors)- Ava
(Display the 10 colored squared on the screen for 1 second)

- change_square(colors)- Ava
(Randomly choose one square and assign it a new color)

- check_answer(user_choice, changed_index, steak)- Demi
(determine whether the user selected the correct square and update their score accordingly)

- display_feedback(correct) - Demi
(Show a message telling the player whether their answer was correct or incorrect)

- display_win_screen() - Ava 
(Show the final winning graphic when the player wins)

- main() - Shared responsiblity
(combines all parts of the program so it is a fully working game loop)



