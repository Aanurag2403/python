import random

print('''
s for snake 
w for water
g for gun
''')

# using random for selecting computer choices

computer = random.choice([-1,0,1])

# taking input
youstr = input("enter your choice: ").lower()

#taking input into numbers
youdict = {"s":1,"w":-1,"g":0}

# storing inout in 'you'
you = youdict[youstr]

#using reverse to signify what computer has selected
reverseDict={1:"snake",-1:"water",0:"gun"}
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

print("")

# checking conditions for the game
if (computer == you):
    print("its a draw")
else:
  if (computer == -1 and you ==1):
      print("You win")
  elif(computer == -1 and you ==0):
      print("you lose")
  elif (computer == 1 and you ==-1):
      print("you lose")
  elif(computer == 1 and you == 0):
      print("you win")
  elif(computer == 0 and you == -1):
      print("you win")
  elif(computer == 0 and you == 1):
      print("you lose")
  else:
      print("something went wrong")