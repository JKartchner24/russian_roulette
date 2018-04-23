import random
print("Hello and welcome to possibly the last thing you will ever do!")
print("Tonight we are going to use the LeMat Revolver which has 9 chambers")
print("We dont want you both to die, so we will only be using a maximum of 4 chambers")
num_bullets = input("Remember the more bullets you have the higher chance you have to lose. Now how many bullets would you like to use?")
print(num_bullets, "bullets")
playerone = input("What is player ones name?: ")
playertwo = input("What is player twos name?: ")
print("Tonights showdown will be", playerone.capitalize() + ", facing off against", playertwo.capitalize() + ", who will win?")

def onebullet():
    bullet_ammount = 0
    bullet_chamber = random.randint(1, 9)
    while bullet_chamber != bullet_ammount:
      bullet_ammount += 1
      print("Click..... but nothing happened")
      input("Press enter if you want to go again")
      if bullet_chamber == bullet_ammount and bullet_ammount % 2 == 0:
        print("POP!", playerone + "'s just lost the game")
      elif bullet_chamber == bullet_ammount and bullet_ammount % 2 == 1:
        print("PEW", playertwo + "'s just lost their head")
        play_again()
        
def twobullets():
    bullet_ammount = 0
    bullet_chamber = random.randint(1, 9)
    bullet_chamber_two = random.randint(1,9)
    while bullet_chamber != bullet_ammount and bullet_chamber_two != bullet_ammount:
      bullet_ammount += 1
      print("Click..... but nothing happened")
      input("Press enter if you want to go again")
      if bullet_chamber == bullet_ammount and bullet_ammount % 2 == 0 or bullet_chamber_two == bullet_ammount:
        print("POOMB!", playerone + "'s been eliminated")
      elif bullet_chamber == bullet_ammount and bullet_ammount % 2 == 1 or bullet_chamber_two == bullet_ammount:
        print("WHAAM", playertwo, "hit the floor")
        play_again()
        
def threebullets():
    bullet_ammount = 0
    bullet_chamber = random.randint(1, 3)
    while bullet_chamber != bullet_ammount:
      bullet_ammount += 1
      print("Click..... but nothing happened")
      input("Press enter if you want to go again")
      if bullet_chamber == bullet_ammount and bullet_ammount % 2 == 0:
        print("POP!", playerone + "'s seeing the light")
      elif bullet_chamber == bullet_ammount and bullet_ammount % 2 == 1:
        print("PEW!", playertwo + "'s going to hell")
        play_again()
        
def fourbullets():
    bullet_ammount = 0
    bullet_chamber = random.randint(1, 5)
    bullet_chamber_two = random.randint(1, 5)
    while bullet_chamber != bullet_ammount:
      bullet_ammount += 1
      print("Click..... but nothing happened")
      input("Press enter if you want to go again")
      if bullet_chamber == bullet_ammount and bullet_ammount % 2 == 0 or bullet_chamber_two == bullet_ammount:
        print("BAM!", playerone, "won't need his wallet anymore")
        play_again()
      elif bullet_chamber == bullet_ammount and bullet_ammount % 2 == 1 or bullet_chamber_two == bullet_ammount:
        print("SNAP!", playertwo, "was a great person")
        play_again()

def play_again():
  play_another = input("Congragulations on winning! If you would like to play again type 'yes' or 'no'" )
  if play_another == "yes":
    num_bullets = input("Remember the more bullets you have the higher chance you have to lose. Now how many bullets would you like to use?")
    playerone = input("What is player ones name?: ")
    playertwo = input("What is player twos name?: ")
    print("Tonights showdown will be", playerone.capitalize() + ", facing off against", playertwo.capitalize() + ", who will win?")
    game(num_bullets)
  elif play_another == "no":
    print("goodbye")
    exit()

def game(num_bullets):

  if num_bullets == "1":
      onebullet()
  
  
  elif num_bullets == "2":
      twobullets()
      
      
  elif num_bullets == "3":
      threebullets()
      
      
  elif num_bullets == "4":
      fourbullets()
      
game(num_bullets)

