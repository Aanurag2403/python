# the game() functio in aprogram lets a user play a game and returns the score as an integer. you need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. you need to write a program to update the Hi-score whenever the game()function breaks the Hi-score.

import random

def game():
    print("you are playing a game!!")
    score = random.randint(1,100)
    with open("hi-score.txt") as f:
        hi_score=f.read()
        if(hi_score != ""):
           hi_score = int(hi_score)
        else:
            hi_score = 0
    
    print(f"your score is {score}")

    if(score>hi_score):
       with open("hi-score.txt","w") as f:
          f.write(str(score))
    return score
   


game()