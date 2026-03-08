# WordleClone

## **Description**

I created a Wordle Clone game where users have 5 chances to guess a 5-letter word. The game provides visual feedback by coloring the tiles based on how correct the letters are.

## **Features**

- Users can type letters into a grid of 5x5 tiles.
- Green tiles indicate the letter is in the correct position.
- Yellow tiles indicate the letter is in the word but in the wrong position.
- Gray tiles indicate the letter is not in the word.
- A message is displayed if the user guesses the correct word or if they run out of tries.

  
<img width="707" height="554" alt="Screenshot 2026-03-07 200941" src="https://github.com/user-attachments/assets/0102eba0-35f4-4b68-b670-54283d0c39f6" />


## **How It Works**

- I used Tkinter to create the 5x5 grid using Label widgets.
- Keyboard input is handled with root.bind("<Key>", key_pressed), which detects each key typed by the user.
- Each time the user presses Enter, the program compares their guess to the secret word and updates the tile colors:
  - Green for correct letter and correct position.
  - Yellow for correct letter but wrong position.
  - Gray for incorrect letter.
- Messages appear using a Label widget to show success or game over notifications.


## **Future Improvements**

- Allow users to choose difficulty levels with longer words.
- Save high scores or streaks for repeated gameplay.
