import random
import time
# App Selection
while True:
  option=input("Welcome! Would you like to 1. Use the Coin Flip App, 2. Use the Dice Rolling App, 3. Play the Number Guessing Game, or 4. Play Hangman?(Please type 1, 2, 3, or 4)")

# Coin Toss
  if option==("1"):
    while True:
      value=random.randint(0,1)
      heads=0
      tails=1
      
      print("The coin is flipping...")
      time.sleep(2)
      if value==0:
        print("The coin landed heads!")
      if value==1:
        print("The coin landed tails!")
      time.sleep(2)
      option=input("Would you like to flip again? (Yes/No)")
      if option==("No"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break
      elif option==("no"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break

# Dice Rolling
  elif option==("2"):
    while True:
      dice=random.randint(0,6)

      print("The dice is rolling...")
      time.sleep(2)
      print("The dice landed:", dice)
      time.sleep(2)
      option=input("Would you like to roll again? (Yes/No)")
      if option==("No"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break
      elif option==("no"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break

# Number Guessing Game
  elif option==("3"):
    while True:
      number=random.randint(1,100)
      # Number of Guesses
      nog=0
      print("Welcome to the Number Guessing Game! I will think of a number and then you will guess. Your score will be shown once you guess the number. Your goal is to get the lowest score possible. Thinking of a number now...")
      time.sleep(2)
      print("Alright, I have thought of a number from 1 to 100. Please guess an interger.")
      while True:
        guess=int(input())
        if number < guess:
          print("Your guess is higher than my number...please guess again!")
          nog=nog+1
        elif number > guess:
          print("Your guess is lower than my number...please guess again!")
          nog=nog+1
        elif guess==number:
          nog=nog+1
          print("You guessed correctly!!! Congratulations!")
          time.sleep(2)
          print("Your score:", nog)
          break
        else:
          print("Please enter an interger.")
      
      option=input("Would you like to play again? (Yes/No)")
      if option==("No"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break
      elif option==("no"):
        print("Returning to Selection Screen...")
        time.sleep(2)
        break

# Hangman
  elif option==("4"):
    # Hangman Drawing
    def hangman():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       \|/")
      print("     |        |")
      print("     |       / \ ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 1 turn left
    def hangman1():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       \|/")
      print("     |        |")
      print("     |       /  ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 2 turns left
    def hangman2():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       \|/")
      print("     |        |")
      print("     |        ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 3 turns left
    def hangman3():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       \|/")
      print("     |        ")
      print("     |        ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 4 turns left
    def hangman4():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       \|")
      print("     |        ")
      print("     |        ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 5 turns left
    def hangman5():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |        |")
      print("     |        ")
      print("     |        ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 6 turns left
    def hangman6():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |_|")
      print("     |       ")
      print("     |        ")
      print("     |       ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 7 turns left
    def hangman7():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       | |")
      print("     |       ")
      print("     |        ")
      print("     |       ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 8 turns left
    def hangman8():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       |")
      print("     |       ")
      print("     |        ")
      print("     |        ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 9 turns left
    def hangman9():
      print("      ________")
      print("     |        |")
      print("     |        _")
      print("     |       ")
      print("     |       ")
      print("     |        ")
      print("     |       ")
      print("     |")
      print(" ---------")
    # Hangman Drawing with 10 turns left
    def hangman10():
      print("      ________")
      print("     |        |")
      print("     |        ")
      print("     |       ")
      print("     |       ")
      print("     |        ")
      print("     |      ")
      print("     |")
      print(" ---------")
    
    turns=10
    print("Welcome to Hangman! I will think of a word and you will guess one letter at a time. You can only have 10 wrong answers, otherwise you lose.")
    time.sleep(1)
    start=input("The genre is Animals. Please type in start to begin! [All lowercase]")
    hangman10()
    # Animals Genre
    if start==("start"):
      animals=("lion", "tiger", "bear", "zebra", "alligator", "panda", "dog", "cat", "squirrel", "hyena", "fish", "shark", "koala", "snake", "lizard", "raccoon", "goat", "monkey", "gorilla", "frog", "hippo", "seal", "wolf", "coyote", "bee", "wasp", "robin", "eagle", "butterfly", "crocodile", "donkey", "armadillo", "owl", "dear", "cheetah", "lynx", "camel", "chicken", "meerkat", "sloth", "bunny", "rabbit", "penguin", "octopus", "sheep", "tortise", "turtle", "elephant", "giraffe", "lobster", "duck", "rhino", "crab", "flamingo", "bat", "lemur", "hedgehog", "scorpion", "gecko", "platypus", "whale", "dolphin", "buffalo", "bison", "gopher", "cougar", "panther", "parrot", "shrimp", "starfish", "seahorse", "manatee", "squid", "narwhal")
      word=random.choice(animals)
      letters=len(word)
      print("I will think of an animal...")
      time.sleep(2)
      print("I have thought of an animal! Please type a lowercase letter. If you think you know the word, please type the word![In lowercase letters]")
      print("By the way... there are", letters,"letters in my word.")
      while True:
        guess=input()
        guessList=[]
        guessList.append(guess)
        if guess==word:
            print("Congratulations! You guessed my word:", word)
            time.sleep(2)
            print("Returning to selection screen...")
            time.sleep(2)
            break
        elif guess in word:
          print("Correct!", guess,"is in my word!")
          print("The letter you guessed appears in the word as follows:")
          for i in range (letters):
            if word[i]==guess:
              print(guessList)
            else:
              print("_")
          time.sleep(1)
          print("Please guess again!")
        else:
          turns=turns-1
          print("Sorry", guess,"is not in my word.")
          time.sleep(1)
          print("You have", turns,"turns left...")
          if turns==0:
            hangman()
            time.sleep(2)
            print("I'm sorry, you have ran out of turns... GAME OVER")
            print("The word was:",word)
            time.sleep(3)
            print("Returning to selection screen...")
            time.sleep(3)
            break
          elif turns==1:
            hangman1()
          elif turns==2:
            hangman2()
          elif turns==3:
            hangman3()
          elif turns==4:
            hangman4()
          elif turns==5:
            hangman5()
          elif turns==6:
            hangman6()
          elif turns==7:
            hangman7()
          elif turns==8:
            hangman8()
          elif turns==9:
            hangman9()
          print("Please guess again!")
