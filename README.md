# memory-game

MEMORY GAME DEMO
Group; Ava Zumerchik (avazumerchik-design) and Demetra Marlantis (demetramarlantis- netizen)

What is the Memory Game? 

The Memory Game is a entertaining program that will challange your memory and help to practice your focus.  
To start, you will enter your player name. There will be 10 squares, each a different color, that will be arranged in two rows of 5 squares. 
You will be shown all 10 squares breifly,
the screen will go blank, and then the colorded sqaures will show back up, one of them with a different color than before. 
Your job is to select which square has changed color. If you guess correctly, you will get a point! If you guess incorrect, 
the program will tell you that you were incorrect and you will move on. To win the game, you need to get 5 points! Good Luck!

DEMO TYPES:
1. Standard demo 
- The user inputs their name
- The directions are then displayed for the user. 
- The player observes the squares and tries to remember the colors.
- The player then selects the changed square.
- The score will update based on correctness. 

2. Feedback System
- With the correct selection, the score increases. 
- Incorrect selection will not increase the score. 
- There will be visual feedback displayed after each round. 
- Winning the game by getting 5 points will trigger a final screen. 

TESTING: 
You are able to run the tests using pytest in the root directoy as a module. 
python -m pytest
When the game runs, the player should answer correctly to earn points and stay in the game boundaies. Any  movemnet should update immediatley on the screen when selecting the sqaures. 
The visuals should appear immediately after the corrrect or incorrect square is pressed and visibly affect the game right away. 
When running the full game, the score should be disaplyed and update automatically with every correct guess. 
Once the player reaches the win conditons, the vistory screen should display. All screens and transitions should happen at the correct time and, based on the player's actions 
and be smooth. 

CODE STRUCTURE: 
Our project is organized into seperate files to help keep our code clean and easy to read. The main file is responsible for running our game loop and handling gameplay. There are additional files that are used to seperate parts of the programs, such as for player movemnet and the graphics. This structure helps to make the code more readable and allows for the game to be coded in seprate parts. 

CONTROLS: 
The player controls the game using the mouse. The escape button will force quit the game and start over. 