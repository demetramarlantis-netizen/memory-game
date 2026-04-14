# memory-game

Group; Ava Zumerchik (avazumerchik-design) and Demetra Marlantis (demetramarlantis- netizen)

Our plan for our final project is to create a memory game. There will be 10 squares, each a diffrent color that flash onto the screen for 1 second. Then, the screen will go blank. The same 10 squares will show up back on the screen, except one square will change its color. The user will have to select the corect square that changed color to receive a point. They want to get 5 rounds coreect in a row to win the game. If they select the wrong square, the game will tell them it is incorrect and will start thier score back to zero. Once the user "wins" the game, the screen will change to a fun winner graphic. 

Functions: 
1. show_colors() - display the 10 color squares on the screen for 1 second so the player can memorize them. After that 1 second, the screen clears.
2. change_squares() - Show the same 10 squares as before, but this time randomly change the color of one square. The player then must click the square that changed
3. check_answers() - Check whether the player has clicked the correct square, the one that changed color. If correct, the score increases; if not, the score resets to zero. The game ends when the player has gotten 5 consecutive correct answers. Once they have the winnning screen shows.


How we will split our work: We will work togteher to figure out our plan for our code and process. To divide the work, we will split the code in half based on the diffucltuy of each part of our project. We live in the same house, so we will be able to communicate with each other very easily and stop in out of each other's room if we need any quick communcation. For more formal time together, we will plan, as necesscary, when we can meet to sit down and work togteher. 

Project checkin #2: 

Introduction: 
For our program, you will be playing a memory game. You will start by inputting your name so that the program knows who the player is. There will be 10 squares, each a different color, that will be arranged in two rows of 5 squares. You will be shown all 10 squares breifly, the screen will go blank, and then the colorded swaures will show back up, one of them with a different color than before. Your job is to select which square has changed color. If you guess correctly, you will get a point! If you guess incorrect, the program will tell you that you were incorrect and you will move on. To win the game, you need to get 5 points! 

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



