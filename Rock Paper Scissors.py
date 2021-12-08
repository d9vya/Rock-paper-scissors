import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images = [rock,paper,scissors]
#s is the user input
s = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
if s>2 or s<0:
  print("You gave an invalid number. You lose!")
else:
  print(images[s])

  #a is what the computer choose
  a = random.randint(0, 2) 
  print("Computer chose:")
  print(images[a])

  #checking out the outcome

  if s==0 and a==2 or s==2 and a==1 or s==1 and a==0:
    print("You win")
  elif s==a:
    print("It's a draw")
  else:
    print("You lose")






